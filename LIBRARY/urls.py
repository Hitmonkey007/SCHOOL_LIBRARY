from django.contrib import admin
from django.urls import path
from LIBRARY.views import *
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', home.index, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('contact', home.contact, name='contact'),
    path('ajout_lecteur', lecteure.ajout_lecteur, name='ajout_lecteur'),
    path('lecteurs', lecteure.lecteurs, name='lecteurs'),
    path('emprunts/index', emprunts.index, name='emprunt_index'),
    path('emprunts/ajout_emprunt',emprunts.ajout_emprunt, name='emprunts_ajout'),
    path('signout', views.signout, name='signout'),
]