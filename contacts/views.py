from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from contacts.forms import CreateContactForm, CreateGroupeForm
# from sva.models import Reponse,Pays_Destination,Message_Erreur,Message_Multi
from django.views.generic import View, CreateView, DeleteView, ListView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required  # Verification  des utilisateurs connectés pour les fonctions de vue
from django.db.models import Q
from accounts.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin  # verification des utilisateurs connectés pour les class built-in views
from contacts.models import Contact, Groupe

# views générique pour lister  les contacts deja enregistrer


# class CreateContactFormMod(CreateContactForm, View):

#    def __init__(self, *args, **kwargs):
#user = self.request.user
#        super(CreateContactFormMod, self).__init__(*args, **kwargs)
#       self.fields['contact_groupe'].queryset = Groupe.objects.filter(groupe_utilisateur=user)
#       # return CreateContactFormMod

# def clean_contact_groupe(self):
#    super(CreateContactFormMod, self).__init__(*args, **kwargs)
#    self.fields['contact_groupe'].queryset = Groupe.objects.filter(groupe_utilisateur=self.request.user)


class ListeContact(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Contact
    context_object_name = "contact_enregistrer"
    template_name = "contacts/liste_contact.html"
    # queryset=Message_Multi.objects.filter(utilisateur_id=request.user)
    paginate_by = 10

    def get_queryset(self):
        return Contact.objects.filter(contact_utilisateur=self.request.user).order_by('-date_modified')


class ListeGroupe(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Groupe
    context_object_name = "groupe_enregistrer"
    template_name = "contacts/liste_groupe.html"
    # queryset=Message_Multi.objects.filter(status_message=False)
    paginate_by = 10

    def get_queryset(self):
        return Groupe.objects.filter(groupe_utilisateur=self.request.user)

    def get_form_kwargs(self):
        kwargs = super(GroupeCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ContactCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Contact
    template_name = "contacts/create_contact.html"
    form_class = CreateContactForm
    success_url = reverse_lazy("lister_contact")

    # Ajouter le usermane et le userid de l'utilisateur connecté
    # def get_queryset(self):
    #    return Groupe.objects.filter(groupe_utilisateur=self.request.user)
    # passe au formulaire le request.user
    # def get_form_kwargs(self):
    #    kwargs = super(ContactCreate, self).get_form_kwargs()
    #    kwargs.update({'user': self.request.user})
    #    return kwargs

    def form_valid(self, form):
        object = form.save(commit=False)
        object.contact_utilisateur = self.request.user
        #object.contact_groupe = Groupe.objects.filter(groupe_utilisateur=0)
        # object.utilisateur_id= self.request.user.id
        object.save()
        return super(ContactCreate, self).form_valid(form)


class GroupeCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Groupe
    template_name = "contacts/create_groupe.html"
    form_class = CreateGroupeForm
    success_url = reverse_lazy("lister_groupe")
    # Ajouter le usermane et le userid de l'utilisateur connecté

    def form_valid(self, form):
        object = form.save(commit=False)
        object.groupe_utilisateur = self.request.user
        # object.utilisateur_id= self.request.user.id
        object.save()
        return super(GroupeCreate, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(GroupeCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


# views générique pour la mise à jour  des messages


class UpdateContact(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Contact
    template_name = "contacts/create_contact.html"
    form_class = CreateContactForm
    success_url = reverse_lazy("lister_contact")


class UpdateGroupe(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Groupe
    template_name = "contacts/create_groupe.html"
    form_class = CreateGroupeForm
    success_url = reverse_lazy("lister_groupe")

   # def get_object(self, queryset=None):
   #     code = self.kwargs.get('code', None)  # Recuperer le code pour trouver l'object
  #      return get_object_or_404(Message_Multi, code=code)  # Recuperer l'object message

  #  def form_valid(self, form):
  #      self.object = form.save()
  #      return HttpResponseRedirect(self.get_success_url())
    def get_form_kwargs(self):
        kwargs = super(UpdateGroupe, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class DeleteContact(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Contact
    context_object_name = "contact_supprimer"
    template_name = "contacts/supprimer_contact.html"
    success_url = reverse_lazy("lister_contact")
    form_class = CreateContactForm


class DeleteGroupe(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Groupe
    context_object_name = "groupe_supprimer"
    template_name = "contacts/supprimer_groupe.html"
    success_url = reverse_lazy("lister_groupe")
    form_class = CreateGroupeForm

    # def get_object(self, queryset=None):
    #   code = self.kwargs.get('code', None)
    #   return get_object_or_404(Message_Multi, code=code)
