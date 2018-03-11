from django.shortcuts import render,redirect,get_object_or_404
from .models import Image,Profile,Comment
from django.contrib.auth.decorators import login_required
from .forms import UploadForm,CommentForm
from django.http import HttpResponse, Http404
from django.contrib import messages


@login_required(login_url='/accounts/login/')
def index(request):
    
    current_user=request.user
    update= Image.objects.all()
    profile= Profile.objects.all()
   
   

    
    

    return render(request,'all-temps/index.html',{"update":update,"profile":profile})

@login_required(login_url='/accounts/login/')
def profile(request):

    profile=Profile.get_profile()   

    return render(request,'all-temps/profile.html',{"profile":profile}) 




def search_results(request):
    
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'all-temps/search.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-temps/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    title = 'Instagrum | Upload'
    profiles = Profile.get_profile()
    for profile in profiles:
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.profile = profile
            upload.save()
            
            return redirect('index')
            messages.success(request, 'Status  updated '\
                                      'successfully')
        else:
            form = UploadForm()
    return render(request,'all-temps/upload.html',{"title":title, "user":current_user,"form":form})


@login_required(login_url='/accounts/login/')
def single_profile(request):
    current_user = request.user
    title = 'Instagrum | Profile'
    profiles = Profile.objects.all()
    images=Image.objects.filter(user=request.user)

    return render(request,'all-temps/single_profile.html',{"title":title,"profiles":profiles,"user":current_user,"images":images})


def user(request,user_id):
    current_user = request.user
    
    try:
        user=Profile.objects.get(id=user_id)
        images=Image.objects.filter(user=request.user)
        
    except Image.DoesNotExist:
        raise Http404()

    return render(request,"all-temps/user.html",{"user":user,"images":images})        
        

@login_required(login_url='/accounts/login/')
def comment(request, id):
    post = get_object_or_404(Image, id=id)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.writer = current_user
            comment.post = post
            comment.save()
            return redirect('index')
    else:
        form = CommentForm()
    return render(request, 'all-temps/comments.html',{"form":form})
