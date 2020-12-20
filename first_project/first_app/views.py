from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from first_app.forms import UserForm,UserProfileInfoForm
# or you can say from first_app import forms
# Create your views here.

def index(request):
    return(render(request,'first_app/index.html'))

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request, user)
                return(HttpResponseRedirect(reverse('index')))
            else:
                return(HttpResponse("Account not active"))
        else:
            print("Incorrect Username or Password")
            print("Username: {} and Password: {}".format(username,password))
            return(HttpResponse("Invalid Username or Password"))
    else:
        return(render(request,"first_app/login.html"))

@login_required
def user_logout(request):
    logout(request)
    return(HttpResponseRedirect(reverse("index")))

@login_required
def special(request):
    return(HttpResponse("Login Required"))

def signup(request):
    userform = UserForm()
    userprofile = UserProfileInfoForm()
    registered = False
    if request.method == 'POST':
        userform = UserForm(request.POST)
        userprofile = UserProfileInfoForm(request.POST)
        if userform.is_valid() and userprofile.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()

            profile = userprofile.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            return(render(request,'first_app/index.html',context={'registered':registered}))
        else:
            print(userform.errors,userprofile.errors)
    return(render(request,'first_app/register.html',context = {'userform':userform,'userprofile':userprofile}))



'''
def index(request):
    return(HttpResponse("Hello World!"))

def index(request):
    my_dict = {"insert_me":"Sajan"}
    return(render(request,'first_app/index.html',context=my_dict))

def index(request):
    webpage_list = AccessRecord.objects.order_by("date")
    # It contains objects
    date_dict = {'accessrecord':webpage_list}
    return(render(request,'first_app/index.html',context=date_dict))

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Success")
            print("Name : " + form.cleaned_data['name'])
            print("Email : " + form.cleaned_data['email'])
    return(render(request,'first_app/form_page.html',context={"form":form}))
'''
