from django.db import models
from django.core.validators import RegexValidator
import random
import string
from accounts.models import Profile
from contacts.models import Groupe
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
#  sauvegarde de tous les reponses des messages qui sont envoyés via nexmo


class Reponse(models.Model):
    reseau = models.CharField('Reseau', max_length=10)
    cout_message = models.CharField('Prix_message', max_length=5)
    message_id = models.CharField('Message_id', max_length=15)
    numero_telephone = models.CharField('Numero de Téléphone', max_length=15)
    status_reponse = models.CharField('Status', max_length=10)
    credit_restant = models.CharField('Crédit restant', max_length=5)
    compteur_message = models.CharField('Compteur Message', max_length=10)
    code_message = models.CharField('Code Message', max_length=10)
    date_reponse = models.DateTimeField('Date', auto_now_add=True)
    reponse_utilisateur = models.ForeignKey(Profile)
    #reponse_utilisateur_id=models.IntegerField('ID Utilisateur',default=0)

    def __str__(self):
        return "{0} {1} {2}".format(self.numero_telephone, self.credit_restant, self.status_reponse)


class Message_Erreur(models.Model):
    message_erreur = models.CharField('Message', max_length=50)
    status = models.CharField('Status', max_length=5)
    numero = models.CharField('Numero Téléphone', max_length=15)
    code_message = models.CharField('Code Message', max_length=10)
    date = models.DateTimeField('Date', auto_now_add=True)
    msg_erreur_utilisateur = models.ForeignKey(Profile)
    #msg_erreur_utilisateur_id=models.IntegerField('ID Utilisateur',default=0)

    def __str__(self):
        return " {0} {1}".format(self.status, self.message_erreur)


class Message_Multi(models.Model):
    #phone_regex = RegexValidator(regex=r'^(7\d{8},?)+$', message="Phone number must be entered in the format: '7xxxxxxxx'. Up to 9 digits allowed.")
    #numero = models.CharField('Numero Téléphone', validators=[phone_regex], max_length=1000)
    numero = PhoneNumberField(blank=True)
    sender = models.CharField('From', max_length=15)
    groupe_numeros = models.ManyToManyField(Groupe, blank=True)
    message = models.TextField('Message', max_length=160)
    utilisateur = models.ForeignKey(Profile)
    status_message = models.BooleanField(default=False)
    date = models.DateTimeField('Date', auto_now_add=True, editable=False)
    code = models.CharField('Code', max_length=7)

    def __str__(self):
        return "{0} {1} {2}".format(self.numero, self.message, self.sender)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.code_generator(7)
        super(Message_Multi, self).save(*args, **kwargs)

    def code_generator(self, nb_caractere):
        car = string.ascii_letters + string.digits
        aleatoire = [random.choice(car) for _ in range(nb_caractere)]
        self.code = ''.join(aleatoire)
