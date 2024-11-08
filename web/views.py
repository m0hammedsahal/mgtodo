from django.shortcuts import render, redirect, reverse

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from users.models import User
from django.contrib.auth.decorators import login_required
from customer.models import *

from web.models import *
from customer.models import Cart


from django.shortcuts import redirect





@login_required(login_url='web:login')
def index(request):
   

    context = {
    }
    return render(request, 'web/index.html', context=context)
