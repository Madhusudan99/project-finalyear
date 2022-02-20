from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib import messages

# Create your views here.
def register(requests):
    if requests.method == "POST":
        form = UserCreationForm(requests.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            messages.success(requests, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(requests, 'users/register.html', context={'form': form}) 