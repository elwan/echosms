"""textma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from accounts.forms import LoginForm
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sva/', include('sva.urls')),
    url(r'^api/message/', include('sva.api.urls')),
    url(r'^api/contact/', include('contacts.api.urls')),
    # url(r'^sva/login/$',views.login,{'template_name':'login.html','authentication_form':LoginForm}),
    url(r'', include('accounts.urls', namespace='accounts')),
    url(r'^contacts/', include('contacts.urls')),
    # url(r'^login/$',views.login,{'template_name':'login.html','authentication_form':LoginForm}),
    # url(r'^logout/$',views.logout,{'next_page':'/login'}),
    # url(r'^register/$',views.register),
    # url(r'^compte/',include('comptes.urls',namespace='comptes')),
]
