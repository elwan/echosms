from django.conf.urls import url
from .views import MessageListApiView, MessageDetailApiView

urlpatterns = [
    url(r'^$', MessageListApiView.as_view(), name='api_liste_message'),
    #url(r'^(?P<pk>\d+)/$', MessageDetailApiView.as_view(), name='api_detail_message')
    url(r'^(?P<code>\w{7})/$', MessageDetailApiView.as_view(), name="api_detail_message"),
]
