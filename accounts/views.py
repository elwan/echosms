from django.shortcuts import render
from . forms  import UserCreation # importer le formulaire modifier pour la creation des users 
from django.views.generic import CreateView # import  de la vue générique pour créer des users 
from . models import Profile  # import le nouveau type d'utilisateurs 

# Create your views here.
from  django.contrib.auth.decorators import login_required

@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")


#une vue générique pour créer des utilisateurs  
class  Register(CreateView):
    form_class = UserCreation
    model = Profile
    template_name = 'accounts/signup.html'
    success_url = '/login/'

    
    
    
