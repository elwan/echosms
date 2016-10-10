from django.conf.urls import patterns, url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # url(r'^ajouter/',views.MessageCreate.as_view(),name="nouveau_message"),
    # url(r'^liste/',views.ListeMessage.as_view(),name="lister_message"),
    # url(r'^msgenvoyer/',views.ListeMessageEnvoyes.as_view(),name="lister_message_envoyer"),
    # url(r'^editer/(?P<code>\w{6})$',views.MessageUpdate.as_view(),name="update_message"),
    # url(r'^delete/(?P<code>\w{6})$',views.MessageDelete.as_view(),name="delete_message"),
    # url(r'^envoi/(?P<code>\w{6})$',views.envoi_message,name="envoyer_message"),
    # zone messages multiple
    url(r'^ajouter_contact/', views.ContactCreate.as_view(), name="nouveau_contact"),
    url(r'^ajouter_groupe/', views.GroupeCreate.as_view(), name="nouveau_groupe"),
    url(r'^liste_contact/', views.ListeContact.as_view(), name="lister_contact"),
    url(r'^liste_groupe/', views.ListeGroupe.as_view(), name="lister_groupe"),
    url(r'^editer_contact/(?P<pk>\d+)$', views.UpdateContact.as_view(), name="editer_contact"),
    url(r'^editer_groupe/(?P<pk>\d+)$', views.UpdateGroupe.as_view(), name="editer_groupe"),
    url(r'^supp_contact/(?P<pk>\d+)$', views.DeleteContact.as_view(), name="supprimer_contact"),
    url(r'^supp_groupe/(?P<pk>\d+)$', views.DeleteGroupe.as_view(), name="supprimer_groupe"),

    # url(r'editer_multi/(?P<code>\w{7})$',views.MessageMultiUpdate.as_view(),name="update_message_multi"),
    # url(r'liste_multi/',views.ListeMultiMessage.as_view(),name="lister_message_multi"),
    # url(r'^delete_multi/(?P<code>\w{7})$',views.MessageMultiDelete.as_view(),name="delete_message_multi"),
    # url(r'^envoi_multi/(?P<code>\w{7})$',views.envoi_message_multi,name="envoyer_message_multi"),
    # url(r'^dashbord/',views.tableau_de_bord,name="tableau_de_bord"),
]
