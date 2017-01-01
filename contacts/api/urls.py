from django.conf.urls import url
from .views import ContactListApiView, ContactDetailApiView, GroupeDetailApiView, GroupeListApiView

urlpatterns = [
    url(r'^$', ContactListApiView.as_view(), name='api_liste_contact'),
    url(r'^(?P<pk>\d+)/$', ContactDetailApiView.as_view(), name='api_detail_contact'),
    #url(r'^(?P<code>\w{7})/$', MessageDetailApiView.as_view(), name="api_detail_message"),
    url(r'^groupe/$', GroupeListApiView.as_view(), name='api_liste_groupe'),
    url(r'^groupe/(?P<pk>\d+)/$', GroupeDetailApiView.as_view(), name='api_detail_groupe')

]
