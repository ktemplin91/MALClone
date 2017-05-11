from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^anime$', views.animepage, name='animepage'),
    url(r'^manga$', views.mangapage, name='mangapage'),
    url(r'^community$', views.communitypage, name='communitypage'),
    url(r'^industry$', views.industrypage, name='industrypage'),
    url(r'^watch$', views.watchpage, name='watchpage'),
    url(r'^help$', views.helppage, name='helppage'),
    url(r'^userprofile$', views.profilepage, name='profilepage'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^user/create/$', views.create_user),

]