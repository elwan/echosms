from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Profile(AbstractUser):

    #phone_regex = RegexValidator(regex=r'^7\d{8}$', message="Phone number must be entered in the format: '7xxxxxxxx'. Up to 9 digits allowed.")
    quota = models.IntegerField(default=0)
    nombre_sms_envoye = models.IntegerField(default=0)
    nombre_sms_restant = models.IntegerField(default=0)
    numero_telephone = PhoneNumberField()
    #date_naissance = models.DateField()
    #email = models.EmailField(unique=True)

#    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['numero_telephone', 'email']
    # USERNAME_FIELD = 'email'  # Utiliser l'email comme  paramettre de connexion
