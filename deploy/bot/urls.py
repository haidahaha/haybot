from django.conf.urls import patterns, url
from bot import views

urlpatterns = patterns('',
    url(r'^talk/$', views.talk, name='talk'),
    url(r'^greeting/$', views.greeting, name='greeting'),
    url(r'^done/$', views.done, name='done'),
    url(r'^doing/$', views.doing, name='doing'),
    url(r'^skipping/$', views.skipping, name='skipping'),

)