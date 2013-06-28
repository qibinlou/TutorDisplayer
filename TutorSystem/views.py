from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.template import RequestContext
from django.db.models import Q



def home(request):
    user = request.user
    return render_to_response('home.html',locals(),context_instance=RequestContext(request))
    
def login(request):
    path = request.get_full_path()
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect("/login_success/")
        else:
            return render_to_response('login.html',{'errors':'True'},context_instance=RequestContext(request))
        request.session.modified = True
    return render_to_response('login.html', context_instance=RequestContext(request))
    
#@login_required
def login_success(request):
    return render_to_response('login_success.html',locals(),context_instance=RequestContext(request))
