from django.shortcuts import render

# Create your views here.
from accounts.forms import LoginForm


def user_login(request):
    form = LoginForm()
    return render(request, 'accounts/user_login.html', {
        'form': form,
    })
