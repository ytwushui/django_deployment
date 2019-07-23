from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileForm
# setup login and logout
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    # add contex dictionary
    context_dict = {'text': 'hello world', 'number':100}
    return render(request, 'basic_app/index.html',context_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')

@login_required
def special(request):
    return HttpResponse('you are longed in')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            print('Faild login')
            print('username:{}'.format(username))
            return HttpResponse('invalid login')
    else: # is requst not posted
        return render(request,'basic_app/login.html')

def register(request):
    registered = False
    if request.method == "POST":
        # this will send back to web by dict
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        # check the form validation
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        # no post
        user_form = UserForm()
        profile_form = UserProfileForm()
    dict = {'user_form':user_form, 'profile_form':profile_form, 'registered':registered}
    return render(request, 'basic_app/registration.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})
