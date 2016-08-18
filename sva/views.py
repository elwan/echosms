from django.shortcuts import render,HttpResponseRedirect,get_object_or_404,HttpResponse
from sva.forms import MessageMultiForm
from sva.models import Reponse,Pays_Destination,Message_Erreur,Message_Multi
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required #Verification  des utilisateurs connectés pour les fonctions de vue 
#from django.utils.decorators import method_decorator
from django.db.models import Q
from accounts.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin #verification des utilisateurs connectés pour les class built-in views
import nexmo 
import requests
import json



s= requests.Session() #connection persistante pour l'envoi de plusieur messages (keep a live http)
# Create your views here

#views générique pour lister les messages enregistrés
#Toutes les classes  vues Génériques necessite un utilisateur logué pour pouvoir etre utiliser et ce grace à au premier paramettre LoginRequiredMixin 
#@login_required(login_url="login/")

#class ListeMessage(LoginRequiredMixin,ListView):
#    login_url='/login/'
#    model = Message
#    context_object_name ="derniers_messages"
#    template_name ="sva/messages.html"
#    paginate_by = 10

   
#views générique pour la creation  des messages
#class MessageCreate(LoginRequiredMixin,CreateView):
#    login_url='/login/'
#    model = Message
#    template_name = "sva/msgcreate.html"
#    form_class = MessageForm
#    success_url= reverse_lazy("lister_message")
    #Ajouter le usermane et le userid de l'utilisateur connecté 
#    def form_valid(self,form):
#        object=form.save(commit=False)
#        object.utilisateur = self.request.user.username
#        object.utilisateur_id= self.request.user.id 
#        object.save()
#        return super(MessageCreate,self).form_valid(form)
        
#views générique pour la mise à jour  des messages
#class MessageUpdate(LoginRequiredMixin,UpdateView):
#    login_url='/login/'
#    model = Message
#    template_name= "sva/msgcreate.html"
#    form_class = MessageForm
#    success_url = reverse_lazy("lister_message")

#    def get_object(self,queryset=None):
#        code= self.kwargs.get('code',None) #Recuperer le code pour trouver l'object 
#        return get_object_or_404(Message,code=code) # #Recuperer l'object message 
#    
#    def form_valid(self,form):
#        self.object= form.save()
#        return HttpResponseRedirect(self.get_success_url())

 #views générique pour la suppression des messages    
#class MessageDelete(LoginRequiredMixin,DeleteView):
#    login_url='/login/'
#    model = Message
#    context_object_name ="delete_message"
#    template_name = "sva/deletemsg.html"
#    success_url = reverse_lazy("lister_message")
#    form_class = MessageForm
#
#    def get_object(self,queryset=None):
#        code= self.kwargs.get('code',None)
#        return get_object_or_404(Message,code=code)


#fonction d'envoi de message
#@login_required(login_url="/login/") 
#def envoi_message(request,code):
#    client = nexmo.Client(key='852f8fa2',secret='aa4fcec9ead8902b') #Api de nexmo
#    message=Message.objects.get(code=code)# recuper l'object à travers son code unique 
#    numero=message.pays.indicatif_pays+message.numero # associer l'indicatif du pays avec le numéro de téléphone 
#    numero_valide = numero.strip('+') # retirer le '+' devant l'indicatif 
#    reponse=client.send_message({'from':message.sender,'to':numero_valide,'text':message.msg})#envoyer le message 
#    #Enregistrer la réponse du message dans la base de donnée
#    valide = reponse['messages'][0]['status']
    
#    if valide == '0':  # Si le message est envoyé  enregistrer dans la base et changer son status 
#        enregister_reponse(request,reponse,code)
#        Message.objects.filter(code=code).update(status_message=True)
#    else:                                        #sinon enregistrer le message d'erreur et retourer 
#        enregister_message_erreur(request,reponse,code)  
    
#    return render(request,'sva/envoi_sms.html',locals())
    #msg={'from':message.sender,'to':numero_valide,'text':message.msg}
    #return HttpResponse(msg.values())



#zone envoi multiple ###############################
#views générique pour lister  les messages Envoyés
class ListeMessageEnvoyes(LoginRequiredMixin,ListView):
    login_url='/login/'
    model = Message_Multi
    context_object_name ="messages_envoyes"
    template_name ="sva/messages_envoyes.html"
    #queryset=Message_Multi.objects.filter(utilisateur_id=request.user)
    paginate_by = 10
    def get_queryset(self):
        return Message_Multi.objects.filter(status_message=True).filter(utilisateur=self.request.user).order_by('-date')
    

class ListeMultiMessage(LoginRequiredMixin,ListView):
    login_url='/login/'
    model = Message_Multi
    context_object_name ="multi_messages"
    template_name ="sva/messages_multi.html"
    #queryset=Message_Multi.objects.filter(status_message=False)
    paginate_by = 10
    def get_queryset(self):
        return Message_Multi.objects.filter(Q(status_message=False) & Q(utilisateur=self.request.user)).order_by('-date')


    
class MessageMultiCreate(LoginRequiredMixin,CreateView):
    login_url='/login/'
    model = Message_Multi
    template_name = "sva/msgcreate.html"
    form_class = MessageMultiForm
    success_url= reverse_lazy("lister_message_multi")
    #Ajouter le usermane et le userid de l'utilisateur connecté 
    def form_valid(self,form):
        object=form.save(commit=False)
        object.utilisateur = self.request.user
        #object.utilisateur_id= self.request.user.id 
        object.save()
        return super(MessageMultiCreate,self).form_valid(form)
        
#views générique pour la mise à jour  des messages
class MessageMultiUpdate(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    model = Message_Multi
    template_name= "sva/msgcreate.html"
    form_class = MessageMultiForm
    success_url = reverse_lazy("lister_message_multi")

    def get_object(self,queryset=None):
        code= self.kwargs.get('code',None) #Recuperer le code pour trouver l'object 
        return get_object_or_404(Message_Multi,code=code) # #Recuperer l'object message 
    
    def form_valid(self,form):
        self.object= form.save()
        return HttpResponseRedirect(self.get_success_url())

class MessageMultiDelete(LoginRequiredMixin,DeleteView):
    login_url='/login/'
    model = Message_Multi
    context_object_name ="delete_message"
    template_name = "sva/deletemsg.html"
    success_url = reverse_lazy("lister_message_multi")
    form_class = MessageMultiForm

    def get_object(self,queryset=None):
        code= self.kwargs.get('code',None)
        return get_object_or_404(Message_Multi,code=code)


@login_required(login_url="/login/")
def envoi_message_multi(request,code):

    message=Message_Multi.objects.get(code=code)# recuper l'object à travers son code unique
    liste_numero=message.numero.split(',')  #mettre les numeros dans la liste 
    liste_numero_indicatif = [ message.pays.indicatif_pays+num  for num in set(liste_numero)] #ajouter l'indicatif du pays sur chaque numéro dans la liste
                                                                                              #enlever les doublons de numéros avec la fonction set() 
    liste_numero_valide = [num.strip('+') for num in liste_numero_indicatif] # enlever de la liste le '+' devant l'indicatif
    
    #reponse=client.send_message({'from':message.sender,'to':numero_valide,'text':message.msg})#envoyer le message 
    #Enregistrer la réponse du message dans la base de donnée
    #playload={'api_key':'852f8fa2' ,'api_secret':'aa4fcec9ead8902b'}
    #preparer la liste de dictionnaire pour l'envoi des messages
    #En ajoutant le message et les numeros et le sender 
    liste_dico_msg =[]   #Liste pour contenir les dico en mettre en paramettre dans l'url  
    liste_numero_envoi_echec=[] #Liste contenant les numéros des messages qui ont échoués 
    liste_numero_envoi_reussi=[] #Liste contenant les numérosn des messages envoyés avec succes 
    for num in liste_numero_valide:
        playload={'api_key':'852f8fa2' ,'api_secret':'aa4fcec9ead8902b'}
        playload['from']=message.sender
        playload['to']=num 
        playload['text']=message.message
        liste_dico_msg.append(playload) #Ajouter le dictonnaire complete a la liste
     
    for dico_msg in liste_dico_msg: #iterer la liste pour placer chaque dico dans l'url 
        data = send_sms(dico_msg) # recuperer la reponse sous format json 
        valide = data['messages'][0]['status'] #Recuperer le status du message 
        if valide == '0':  # Si le message est envoyé  enregistrer dans la base et changer son status
            enregister_reponse(request,data,code) 
            Message_Multi.objects.filter(code=code).update(status_message=True)
            liste_numero_envoi_reussi.append(data['messages'][0]['to'])#ajout du numéro dans la liste 
        else:                                        #sinon enregistrer le message d'erreur et retourer
            enregister_message_erreur(request,data,code)
            liste_numero_envoi_echec.append(data['messages'][0]['to']) #ajout du numéro dans la liste 
            
    return render(request,'sva/envoi_sms.html',locals())
    
    #return HttpResponse(liste_dico_msg)

 #sauvegarder les reponses en cas d'envoi réussi du message

def send_sms(message):
    
    nexmo_url = 'https://rest.nexmo.com/sms/json'
    reponse = s.post(nexmo_url,json=message) #Recuper la réponse de l'envoi

    return reponse.json()
     
@login_required(login_url="/login/") 
def enregister_reponse(request,reponse,code):

    rep = Reponse()                                 #Créér un object reponse et remplir des elemets contenue dans le liste 
    rep.reseau=str(reponse['messages'][0]['network'])
    rep.cout_message=str(reponse['messages'][0]['message-price'])
    rep.message_id=str(reponse['messages'][0]['message-id'])
    rep.numero_telephone=str(reponse['messages'][0]['to'])
    rep.status_reponse=str(reponse['messages'][0]['status'])
    rep.credit_restant=str(reponse['messages'][0]['remaining-balance'])
    rep.compteur_message=str(reponse['message-count'])      #Mettre le deuxieme élément qui correspond à l'extraction du premier dict
    rep.code_message = code     #Mettre le code du message qui a été envoyer pour retrouver facile sa réponse
    rep.reponse_utilisateur=request.user
    #rep.reponse_utilisateur_id=request.user.id
    
    rep.save()  #Sauvegarder dans le base  

    return True

#Enregister les messages d'erreur quand le sms n'est pas envoyé

@login_required(login_url="/login/") 
def enregister_message_erreur(request,reponse,code):
    message_erreur = Message_Erreur()

    message_erreur.message_erreur=str(reponse['messages'][0]['error-text'])
    message_erreur.status= str(reponse['messages'][0]['status'])
    message_erreur.numero= str(reponse['messages'][0]['to'])
    message_erreur.code_message=code
    message_erreur.msg_erreur_utilisateur=request.user
    #message_erreur.msg_erreur_utilisateur_id=request.user.id 
    message_erreur.save()

    return True
##
@login_required(login_url="/login/")
def tableau_de_bord(request):

    return render(request,'sva/dashbord.html',locals())
