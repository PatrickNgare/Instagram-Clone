from django.shortcuts import render
from .models import Image,Profile,Comment


def index(request):
    
    updates=Image.get_image_by_id()
    

    return render(request,'all-temps/index.html',{"updates":updates})
