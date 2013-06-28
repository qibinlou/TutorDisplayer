from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.template import RequestContext
from django.db.models import *
from db.models import *
from db.forms import *



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
    
@login_required
def login_success(request):
    return render_to_response('login_success.html',locals(),context_instance=RequestContext(request))

    
@login_required
def passwordchange(request):
    user = request.user
    if request.method == 'POST':     
        if request.POST['origin'] != '' :
            if not user.check_password(request.POST['origin']):
                return render_to_response('password_change.html',{'passerror':'True'}, context_instance=RequestContext(request))    
            if request.POST['word1'] !=  request.POST['word2']:
                return render_to_response('password_change.html',{'sameerror':'True'}, context_instance=RequestContext(request))   
            if len(request.POST['word1']) < 6:
                return render_to_response('password_change.html',{'short':'True'}, context_instance=RequestContext(request))    
            user.set_password(request.POST['word1'])
            user.save()
            return render_to_response('password_change.html',{'change':'True'}, context_instance=RequestContext(request))
        else:
            return render_to_response('password_change.html',{'blank':'True'}, context_instance=RequestContext(request))
    
    return render_to_response('password_change.html',context_instance=RequestContext(request))
    
    
@login_required
def profilechange(request):
    user = request.user
    profile = user.get_profile()
    change = False
    form = ProfileChangeForm(request.POST)
    if request.method == 'POST':   
       if form.is_valid():
            cd = form.cleaned_data
            course.prerequisites = cd['prerequisites']
            course.max_student = cd['max_student']
            course.save()              
        
       
    else:
        form = ProfileChangeForm()
       
       
       
        user.save()
        profile.save()
        change = True
        return render_to_response('profile_change.html',locals(), context_instance=RequestContext(request))             
    return render_to_response('profile_change.html',locals(), context_instance=RequestContext(request))
    
    

