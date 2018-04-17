from django.conf.urls import patterns, include, url
from django.contrib import admin
from Minimum_Operations import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Jubilant_Pancake.views.home', name='home'),
    # url(r'^Jubilant_Pancake/', include('Jubilant_Pancake.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.minOps, name='minOps'),
)
