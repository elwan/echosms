from django import forms
from sva.models import Message_Multi

# class MessageForm(forms.ModelForm):
#    class Meta:
#        model=Message
#        fields=('numero','sender','msg','pays')


class MessageMultiForm(forms.ModelForm):
    numero = forms.CharField(label="", max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'numero', 'placeholder': 'Numero Telephone', 'required': 'True', 'autofocus': 'True'}))
    sender = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'sender', 'placeholder': 'sender', 'required': 'True', 'autofocus': 'True'}))
    message = forms.CharField(label="", max_length=160, widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'message', 'placeholder': 'Entrer votre message', 'required': 'True', 'autofocus': 'True'}))

    class Meta:
        model = Message_Multi
        fields = ('numero', 'sender', 'message')
