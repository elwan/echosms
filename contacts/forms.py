from django import forms
from django.forms import ModelForm, Form
from django.contrib.contenttypes.forms import generic_inlineformset_factory as inlineformset_factory
# from django.forms.models import inlineformset_factory
from contacts.models import Contact, Groupe


class CreateContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ('nom', 'prenom', 'contact_groupe', 'numero_telephone', 'email_address', 'photo', 'pays')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CreateContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_groupe'].queryset = Groupe.objects.filter(groupe_utilisateur=self.user)


class CreateGroupeForm(ModelForm):

    class Meta:
        model = Groupe
        fields = ('nom_groupe', 'about')


# PhoneNumberFormSet = inlineformset_factory(PhoneNumber, extra=1)
# EmailAddressFormSet = inlineformset_factory(EmailAddress, extra=1)
# InstantMessengerFormSet = inlineformset_factory(InstantMessenger, extra=1)
# WebSiteFormSet = inlineformset_factory(WebSite, extra=1)
# StreetAddressFormSet = inlineformset_factory(StreetAddress, extra=1)
# SpecialDateFormSet = inlineformset_factory(SpecialDate, extra=1)
