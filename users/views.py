from django.shortcuts import render, redirect
from django.contrib.auth.forms  import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.

def users_main_view(request):
    return render(request, 'user_main.html')

def user_registration_view(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('journal:journal_list')
        
    else:
        form = UserCreationForm()
    
    return render(request, 'user_registration.html' , {"form":form})


def user_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            # If you tried to access a protected resource before logging this sends you to that resource after login
            if 'next' in request.POST:
                return redirect (request.POST.get("next")) 
            else:
                return redirect('journal:journal_list')
    else:
        form = AuthenticationForm(request.GET)
    return render(request, 'user_login.html', {"form": form})

        
def user_logout_view(request):
    if request.method =="POST":
        logout(request)
        return redirect('users:user_main')