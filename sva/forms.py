from django import forms
from sva.models import Message_Multi
from contacts.models import Groupe, Contact
from django.forms import ModelForm

# class MessageForm(forms.ModelForm):
#    class Meta:
#        model=Message
#        fields=('numero','sender','msg','pays')


class MessageMultiForm(ModelForm):
    numero = forms.CharField(label="", max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'numero', 'placeholder': 'Numero Telephone', 'required': 'True', 'autofocus': 'True'}))
    sender = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'sender', 'placeholder': 'sender', 'required': 'True', 'autofocus': 'True'}))
    message = forms.CharField(label="", max_length=160, widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'message', 'placeholder': 'Entrer votre message', 'required': 'True', 'autofocus': 'True'}))
    groupe_numero = forms.ModelMultipleChoiceField(label="Mes groupes :", widget=forms.CheckboxSelectMultiple(attrs={'class': '', 'name': 'groupe', 'autofocus': 'True'}), queryset=Groupe.objects.all())

    class Meta:
        model = Message_Multi
        fields = ('numero', 'sender', 'message', 'groupe_numero')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(MessageMultiForm, self).__init__(*args, **kwargs)
        self.fields['groupe_numero'].queryset = Groupe.objects.filter(groupe_utilisateur=self.user)
