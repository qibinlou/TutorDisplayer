from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.conf.urls.defaults import *
import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TutorSystem.views.home', name='home'),
    # url(r'^TutorSystem/', include('TutorSystem.foo.urls')),
    url(r'^submittutorrequest/$', views.submit_tutor_request),
    url(r'^filltutorrequest/$', views.fill_tutor_request),
    url(r'^tutordisplay/$', views.tutordisplay),
    url(r'^detailed_info/$', views.tutorinfo),
    url(r'^home/$',views.home),
    url(r'^login/$',views.login),
    url(r'^login_success/$',views.login_success),
    url(r'^accounts/logout/$', logout,{'next_page':'/home/'}), 
    url(r'profile_change/',views.profilechange),
    url(r'password_change/',views.passwordchange),
    url(r'imagehandle/',views.imagehandle),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
