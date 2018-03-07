from django.shortcuts import render,redirect
from .models import Image,Profile,Comment
from django.contrib.auth.decorators import login_required
from .forms import UploadForm

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


@login_required(login_url='/accounts/login')
def user_profile(request, user_id):
    profile = Profile.objects.get(id=user_id)
    images = Image.objects.all().filter(user_id=user_id)
    return render(request, 'all-temps/singleprofile.html', {'profile':profile, 'images':images})    


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
        else:
            form = UploadForm()
    return render(request,'all-temps/upload.html',{"title":title, "user":current_user,"form":form})




@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    title = 'Instagrum | Profile'
    profiles = Profile.objects.all()
    return render(request,'all-temps/single_profile.html',{"title":title,"profiles":profiles,"user":current_user,})