from django import forms
from sva.models import Message_Multi

#class MessageForm(forms.ModelForm):
#    class Meta:
#        model=Message
#        fields=('numero','sender','msg','pays')


class MessageMultiForm(forms.ModelForm):
    class Meta:
        model = Message_Multi
        fields=('numero','sender','message','pays')
        


        
