from django.shortcuts import render
from .models import Image,Profile,Comment


def index(request):
    
    # update=Image.objects.order_by('-postdate')
    update=Image.objects.all()
    print(update)
    

    return render(request,'all-temps/index.html',{"update":update})