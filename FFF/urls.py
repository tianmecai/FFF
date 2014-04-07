from django.conf.urls import patterns, include, url

from django.contrib import admin

from FFF.user_information import login,register
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FFF.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^login/(\d{11,11})/([A-Za-z0-9_]+)',login), 
    (r'^register/(\d{11,11})/([A-Za-z0-9_]+)',register),
    url(r'^admin/', include(admin.site.urls)),
)
