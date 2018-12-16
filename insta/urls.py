from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from instagram import views as view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {'next_page':'/accounts/register/'}),
    url(r'', include('instagram.urls')),
    url(r'^account_activation_sent/$', view.default, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        view.activate, name='activate')
]
