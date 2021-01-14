from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

from .models import UserInfo
from .forms import Register_form,UserInfoForm

def home(request):
    return render(request, 'base.html')

def biodata(request):
    objects = UserInfo.objects.all()
    return render(request, 'biodata.html',{'objects':objects})

def register(request):
    if request.method == 'POST':
        form = Register_form(data=request.POST)
        profile_form = UserInfoForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile =profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)

            login(request, user)
            messages.info(request,'Register successfully!')

            return redirect('home')
        else:
            messages.info(request,'Invalid credentials')   
    else:
        form = Register_form()
        profile_form = UserInfoForm()

    context = {'form':form,'profile_form':profile_form}
    return render(request,'register.html',context)


def logindata(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user:
                login(request, user)
                user.save()
                messages.info(request,'Login successfully!')
                return redirect('biodata')
        
    return render(request,'login.html')


def logoutdata(request):
    logout(request)
    return redirect('home')

