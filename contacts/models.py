from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _
from django_countries.fields import CountryField
from accounts.models import Profile
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    """Contact model."""
    prenom = models.CharField(_('prenom'), max_length=100)
    nom = models.CharField(_('nom'), max_length=200)
    about = models.TextField(_('about'), blank=True)
    photo = models.ImageField(_('photo'), upload_to='contacts/person/', blank=True)
    pays = CountryField(blank_label='Pays')
    phone_regex = RegexValidator(regex=r'^(7\d{8},?)+$', message="Phone number must be entered in the format: '7xxxxxxxx'. Up to 9 digits allowed.")
    #numero_telephone = models.CharField('Numero Téléphone', validators=[phone_regex], max_length=1000)
    numero_telephone = PhoneNumberField()
    email_address = models.EmailField(_('Adresse Email'))
    contact_utilisateur = models.ForeignKey(Profile)
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    date_modified = models.DateTimeField(_('date modified'), auto_now=True)

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
        managed = True

    def __str__(self):
        return " {} {} {}".format(self.nom, self.prenom, self.numero_telephone)


class Groupe(models.Model):
    """Group model."""
    nom_groupe = models.CharField(_('Nom'), max_length=200)
    about = models.TextField(_('about'), blank=True)
    contact = models.ManyToManyField(Contact, verbose_name='Contacts', blank=True)
    groupe_utilisateur = models.ForeignKey(Profile)

    class Meta:
        db_table = 'contacts_groups'
        ordering = ('nom_groupe',)
        verbose_name = _('groupe')
        verbose_name_plural = _('groupes')
        managed = True

    def __str__(self):
        return "%s" % self.nom_groupe
