from django import forms
from sva.models import Message_Multi
from contacts.models import Groupe, Contact
from django.forms import ModelForm


class MessageMultiForm(ModelForm):
    numero = forms.CharField(label="", max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'numero', 'placeholder': 'Numero Telephone', 'autofocus': 'True'}))
    sender = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'sender', 'placeholder': 'sender', 'required': 'True', 'autofocus': 'True'}))
    message = forms.CharField(label="", max_length=160, widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'message', 'placeholder': 'Entrer votre message', 'required': 'True', 'autofocus': 'True'}))
    groupe_numeros = forms.ModelMultipleChoiceField(label="Mes groupes :", widget=forms.CheckboxSelectMultiple(), queryset=Groupe.objects.all())

    class Meta:
        model = Message_Multi
        fields = ('numero', 'sender', 'message', 'groupe_numeros')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(MessageMultiForm, self).__init__(*args, **kwargs)
        self.fields['groupe_numeros'].queryset = Groupe.objects.filter(groupe_utilisateur=self.user)
