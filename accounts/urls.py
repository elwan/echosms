from django.conf.urls import patterns, url,include 
from django.contrib.auth import views as views_auth
from . import views
from . forms import LoginForm
from sva  import views as views_sva

urlpatterns = [
   # url(r'^login/$','django.contrib.auth.views.login',name='login',
   #             kwargs={'template_name': 'comptes/login.html'}),
    #url(r'^logout/$','django.contrib.auth.views.logout',name='logout',
    #                kwargs={'next_page': '/'}),
    #url('^',include('django.contrib.auth.urls')),
    #url(r'^login/',auth_views.login,{'template_name':'accounts/login.html'},name='login'),
    url(r'^login/$',views_auth.login,{'template_name':'accounts/login.html','authentication_form':LoginForm},name="user_login"), #views provenant des vues générique d'authentication de django (built-in)
    url(r'^logout/$',views_auth.logout,{'next_page':'/login'}), #views provenant des vues générique d'authentication de django (built-in)
    #url(r'^$',views.home,name="home"),
    url(r'^$',views_sva.tableau_de_bord),#definir la premiére page comme page d'accueil 
    url(r'^signup/',views.Register.as_view(),name="registration"),
    #url(r'^home/',views.home),
    
]
