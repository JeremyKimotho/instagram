from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url('^$', views.default, name='home'),
  url(r'^new/post$', views.new_post, name='new_post'),
  url('^search$', views.search, name='search'),
  url(r'^(?P<id>[0-9]+)/results/$', views.profile, name='profile'),
  url(r'^like/$', views.like, name='like')
]

if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)