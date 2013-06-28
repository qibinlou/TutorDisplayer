from django.conf.urls import patterns, include, url
import views




# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TutorSystem.views.home', name='home'),
    # url(r'^TutorSystem/', include('TutorSystem.foo.urls')),
    url(r'^home',views.home),
    url(r'^login',views.login),
    url(r'^login_success',views.login_success),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
