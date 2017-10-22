from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'testing101.views.home', name='home'),
    url(r'^base/', include('base.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
