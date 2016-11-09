from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from sva.forms import MessageMultiForm
from sva.models import Reponse, Message_Erreur, Message_Multi
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required  # Verification  des utilisateurs connectés pour les fonctions de vue
#from django.utils.decorators import method_decorator
from django.db.models import Q
from accounts.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin  # verification des utilisateurs connectés pour les class built-in views
import nexmo
import requests
import json


# nous allons utiliser la fonctionnalite keep-alive pour l'envoi de plusieurs message en meme temps
# d'apres la documentation de nexmo avec la connection persistante nous pouvont envoyer jusqu'a 30sms/s

s = requests.Session()  # connection persistante pour l'envoi de plusieur messages (keep a live http)
#zone envoi multiple ###############################
# views générique pour lister  les messages Envoyés


class ListeMessageEnvoyes(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Message_Multi
    context_object_name = "messages_envoyes"
    template_name = "sva/messages_envoyes.html"
    # queryset=Message_Multi.objects.filter(utilisateur_id=request.user)
    paginate_by = 10

    def get_queryset(self):
        return Message_Multi.objects.filter(status_message=True).filter(utilisateur=self.request.user).order_by('-date')

# views generic pour lister les messages qui sont deja enregister


class ListeMultiMessage(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Message_Multi
    context_object_name = "multi_messages"
    template_name = "sva/messages_multi.html"
    # queryset=Message_Multi.objects.filter(status_message=False)
    paginate_by = 10

    def get_queryset(self):
        return Message_Multi.objects.filter(Q(status_message=False) & Q(utilisateur=self.request.user)).order_by('-date')


# Views generic pour creer un message
class MessageMultiCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Message_Multi
    template_name = "sva/msgcreate.html"
    form_class = MessageMultiForm
    success_url = reverse_lazy("lister_message_multi")

    def form_valid(self, form):
        #form = MessageMultiForm(self.request.POST)
        object = form.save(commit=False)
        object.utilisateur = self.request.user  # chaque message creer doit porter l'identifiant du createur
        object.save()
        form.save_m2m()
        return super(MessageMultiCreate, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(MessageMultiCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

# views générique pour la mise à jour  des messages


class MessageMultiUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Message_Multi
    template_name = "sva/msgcreate.html"
    form_class = MessageMultiForm
    success_url = reverse_lazy("lister_message_multi")

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)  # Recuperer le code pour trouver l'object
        return get_object_or_404(Message_Multi, code=code)  # Recuperer l'object message

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self):
        kwargs = super(MessageMultiUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


# views generic pour supprimer un message deja creer
class MessageMultiDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Message_Multi
    context_object_name = "delete_message"
    template_name = "sva/deletemsg.html"
    success_url = reverse_lazy("lister_message_multi")
    form_class = MessageMultiForm

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(Message_Multi, code=code)

# cette fonction permet d'envoyer le message deja creer qui comporte plusieurs numeros


@login_required(login_url="/login/")
def envoi_message_multi(request, code):
    liste_numero_valide = []
    message = Message_Multi.objects.prefetch_related('groupe_numeros__contacts').get(code=code)  # recuper l'object à travers son code unique
    for groupe in message.groupe_numeros.all():
        for num in groupe.contacts.all():
            liste_numero_valide.append(str(num.numero_telephone.country_code) + str(num.numero_telephone.national_number))

    # supprimer les doublons dans la liste de numeros valide
    liste_numero = list(set(liste_numero_valide))
    # preparer la liste de dictionnaire pour l'envoi des messages
    # En ajoutant le message et les numeros et le sender
    liste_dico_msg = []  # Liste pour contenir les dico en mettre en paramettre dans l'url
    liste_numero_envoi_echec = []  # Liste contenant les numéros des messages qui ont échoués
    liste_numero_envoi_reussi = []  # Liste contenant les numérosn des messages envoyés avec succes
    for num in liste_numero:
        playload = {'api_key': '852f8fa2', 'api_secret': 'aa4fcec9ead8902b'}
        playload['from'] = message.sender
        playload['to'] = num
        playload['text'] = message.message
        liste_dico_msg.append(playload)  # Ajouter le dictonnaire complete a la liste

    for dico_msg in liste_dico_msg:  # iterer la liste pour placer chaque dico dans l'url
        data = send_sms(dico_msg)  # recuperer la reponse sous format json
        valide = data['messages'][0]['status']  # Recuperer le status du message
        if valide == '0':  # Si le message est envoyé  enregistrer dans la base et changer son status
            enregister_reponse(request, data, code)
            Message_Multi.objects.filter(code=code).update(status_message=True)
            liste_numero_envoi_reussi.append(data['messages'][0]['to'])  # ajout du numéro dans la liste
        else:  # sinon enregistrer le message d'erreur et retourer
            enregister_message_erreur(request, data, code)
            liste_numero_envoi_echec.append(data['messages'][0]['to'])  # ajout du numéro dans la liste

    return render(request, 'sva/envoi_sms.html', locals())

    # return HttpResponse(liste_dico_msg)

 # sauvegarder les reponses en cas d'envoi réussi du message

# Envoyer un message en utlisant l'API de nexmo chaque message envoyé retourne une reponse avec les details de la transaction


def send_sms(message):

    nexmo_url = 'https://rest.nexmo.com/sms/json'
    reponse = s.post(nexmo_url, json=message)  # Recuper la réponse de l'envoi

    return reponse.json()

# la fonction pour enregister la reponse  si le message a ete bien envoyé


@login_required(login_url="/login/")
def enregister_reponse(request, reponse, code):

    rep = Reponse()  # Créér un object reponse et remplir des elemets contenue dans le liste
    rep.reseau = str(reponse['messages'][0]['network'])
    rep.cout_message = str(reponse['messages'][0]['message-price'])
    rep.message_id = str(reponse['messages'][0]['message-id'])
    rep.numero_telephone = str(reponse['messages'][0]['to'])
    rep.status_reponse = str(reponse['messages'][0]['status'])
    rep.credit_restant = str(reponse['messages'][0]['remaining-balance'])
    rep.compteur_message = str(reponse['message-count'])  # Mettre le deuxieme élément qui correspond à l'extraction du premier dict
    rep.code_message = code  # Mettre le code du message qui a été envoyer pour retrouver facile sa réponse
    rep.reponse_utilisateur = request.user
    # rep.reponse_utilisateur_id=request.user.id

    rep.save()  # Sauvegarder dans le base

    return True

# Enregister les messages d'erreur quand le sms n'est pas envoyé


@login_required(login_url="/login/")
def enregister_message_erreur(request, reponse, code):
    message_erreur = Message_Erreur()

    message_erreur.message_erreur = str(reponse['messages'][0]['error-text'])
    message_erreur.status = str(reponse['messages'][0]['status'])
    message_erreur.numero = str(reponse['messages'][0]['to'])
    message_erreur.code_message = code
    message_erreur.msg_erreur_utilisateur = request.user
    # message_erreur.msg_erreur_utilisateur_id=request.user.id
    message_erreur.save()

    return True
#
# Le tableau de bord permettant de founir les statistiques sur l'utilisation du systeme


@login_required(login_url="/login/")
def tableau_de_bord(request):

    return render(request, 'sva/dashbord.html', locals())
