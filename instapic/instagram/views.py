from django.shortcuts import render
from .models import Image,Profile,Comment
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def index(request):
    
    current_user=request.user
    update= Image.objects.order_by('-postdate')
    profile= Profile.objects.order_by('-update_time')
    comments=Comment.objects.order_by('-timecomment')
    
    

    return render(request,'all-temps/index.html',{"update":update,"profile":profile,"comments":comments})

@login_required(login_url='/accounts/login/')
def profile(request):

    profile=Profile.get_profile()   

    return render(request,'all-temps/profile.html',{"profile":profile}) 