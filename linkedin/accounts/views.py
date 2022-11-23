from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        customer = User.objects.create_user(username,email,password)
        customer.save()

        messages.success(request, "Your Account is has been created")

        return redirect('/')

    # events = Event.objects.all()
    context = {}

    return render(request, 'accounts/signup.html', context)

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            username = user.username

            return redirect('home')
        else:
            messages.error(request, "Bad Credentials")
            return redirect('/')

    # events = Event.objects.all()
    context = {}

    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('/')

def handler404(request,exception):
    return render(request,'404.html')