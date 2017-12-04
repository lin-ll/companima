from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^team/$', views.team, name='team'),
	url(r'^pets/$', views.pets, name='pets'),
	url(r'^volunteer/$', views.volunteer, name='volunteer'),
	url(r'^donate/$', views.donate, name='donate'),
	url(r'^contact/$', views.contact, name='contact'),
]