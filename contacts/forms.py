from django import forms
from django.forms import ModelForm, Form
from contacts.models import Contact, Groupe
from intl_tel_input.widgets import IntlTelInputWidget


class CreateContactForm(ModelForm):
    nom = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'nom', 'placeholder': 'Nom', 'required': 'True', 'autofocus': 'True'}))
    prenom = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'prenom', 'placeholder': 'Prenom', 'required': 'True', 'autofocus': 'True'}))
    numero_telephone = forms.CharField(label="", widget=IntlTelInputWidget())
    #numero_telephone = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'numero_telephone', 'placeholder': 'Numero Telephone', 'required': 'True', 'autofocus': 'True'}))
    email_address = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email_address', 'placeholder': 'Adresse email', 'autofocus': 'True'}))

    class Meta:
        model = Contact
        fields = ('nom', 'prenom', 'numero_telephone', 'photo', 'email_address')

   # def __init__(self, *args, **kwargs):
   #     self.user = kwargs.pop('user')
   #     super(CreateContactForm, self).__init__(*args, **kwargs)
   #     self.fields['contact_groupe'].queryset = Groupe.objects.filter(groupe_utilisateur=self.user)


class CreateGroupeForm(ModelForm):
    nom_groupe = forms.CharField(label=" ", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du groupe', 'required': 'True', 'autofocus': 'True', 'name': 'nom_groupe'}))
    about = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'about', 'placeholder': 'Apropos du groupe', 'required': 'True', 'autofocus': 'True'}))
    contacts = forms.ModelMultipleChoiceField(label="La liste des Numeros de Telephone", widget=forms.CheckboxSelectMultiple(), queryset=Contact.objects.all())

    class Meta:
        model = Groupe
        fields = ('nom_groupe', 'image_groupe', 'contacts', 'about')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CreateGroupeForm, self).__init__(*args, **kwargs)
        self.fields['contacts'].queryset = Contact.objects.filter(contact_utilisateur=self.user)
