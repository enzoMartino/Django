from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from first_app.models import Topic, WebPage, AccessRecord, User
from . import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
 
def index(request):
    context_dict = {'text':'hello world', 'number':100}
    
    return render(request, 'index.html', context=context_dict)


@login_required
def sign_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def sign_in(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print("Username {}, Password {}".format(username,password))
            return HttpResponse("Invalid login credentials supplied")
    else:

        return render(request, 'sign_in.html', context=None)


def sign_up(request):

    isRegistered = False    

    if request.method == 'POST' :
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            
            # do something code
            
            # save user in the db
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                print(request.FILES['profile_picture'])
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()
            profile_form.save_m2m() # needs to be called when commit=False is used
            isRegistered = True
            print('Validation successed')

        else:
            
            print(user_form.errors, profile_form.errors)

    else:
        
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, 'sign_up.html', {'user_form': user_form, 'profile_form': profile_form, 'isRegistered': isRegistered})


def access_records(request):
    webpages_list = AccessRecord.objects.order_by('date')
    
    date_dict = {'access_records': webpages_list}

    return render(request, 'access_records.html', context=date_dict)


def users(request):
    users_list = User.objects.order_by('first_name', 'last_name')

    users_dict = {'users': users_list}

    return render(request, 'users.html', context=users_dict)


def image(request):
    my_dict = {

    }
    return render(request, 'image.html', context=my_dict)


def help(request):
    mydict = {

    }

    return render(request, 'help.html', context=mydict)



