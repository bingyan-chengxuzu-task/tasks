from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.blog_list', name='blog_list'),
    # url(r'^w/', include('w.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^comments/', include('django.contrib.comments.urls')),

    url(r'^detail/$', 'blog.views.blog_detail'),

    url(r'^account/login/$','blog.views.alogin'),
        url(r'^account/register/$','blog.views.register'),  
        url(r'^account/logout/$','blog.views.alogout'),  
                       
)
