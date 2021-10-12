from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth


def accounts(request):
    return render(request, 'jobs/base.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html')
    elif request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])
            return render(request, 'accounts/signup.html', {'error': 'The user already exists'})
        except User.DoesNotExist:
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(
                    request.POST['username'], password=['password2'])
                return redirect('accounts')
            else:
                return render(request, 'accounts/signup.html', {'error': 'Inconsistent entry password'})


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return render (request, 'dash/dash.html')
        else:
            return render(request, 'accounts/login.html',{'error': 'Inconsistent entry password'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request, 'accounts/login.html')
