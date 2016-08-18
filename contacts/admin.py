from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline
#from django_comments.models import Comment

from contacts.models import Contact, Groupe


# class EmailAddressInline(GenericTabularInline):
#   model = EmailAddress


# class PhoneNumberInline(GenericTabularInline):
#    model = PhoneNumber

# class InstantMessengerInline(GenericTabularInline):
#	model = InstantMessenger


# class WebSiteInline(GenericTabularInline):
#    model = WebSite


# class StreetAddressInline(GenericStackedInline):
#    model = StreetAddress


# class SpecialDateInline(GenericStackedInline):
#    model = SpecialDate


class ContactAdmin(admin.ModelAdmin):
   # inlines = [
        # PhoneNumberInline,
        # EmailAddressInline,
        # InstantMessengerInline,
        # WebSiteInline,
        # StreetAddressInline,
        # SpecialDateInline,
        # CommentInline,
   # ]

    list_display_links = ('prenom', 'nom',)
    list_display = ('prenom', 'nom',)
    list_filter = ('groupe',)
    ordering = ('prenom', 'nom')
    search_fields = ['^prenom', '^nom']


class GroupAdmin(admin.ModelAdmin):
    list_display_links = ('nom_groupe',)
    list_display = ('nom_groupe', 'date_modified')
    ordering = ('-date_modified', 'nom_groupe',)
    search_fields = ['^nom_groupe', '^about', ]

admin.site.register(Contact, ContactAdmin)
admin.site.register(Groupe, GroupAdmin)
