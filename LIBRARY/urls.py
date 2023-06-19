from LIBRARY.views.lecteure import delete
from django.contrib import admin
from django.urls import path
from LIBRARY.views import *


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', sigmup.signup, name='signup'),
    path('sigmup/', sigmup.signin, name='signin'),
    path('home/', home.index, name='home_index'),
    path('contact', home.contact, name='contact'),
    path('ajout_lecteur/', lecteure.add, name='lecteur_add'),
    path('lecteurs/', lecteure.index, name='lecteur_index'),
    path('emprunts/', emprunts.index, name='emprunt_index'),
    path('lecteur_edit/<id>', lecteure.edit, name='lecteur_edit'),
    path('lecteur_delete/<id>', lecteure.delete, name='lecteur_delete'),
    path('lecteur_updat/<id>', lecteure.update, name='lecteur_update'),
    path('emprunts/index', emprunts.index, name='emprunt_index'),
    path('emprunts/ajout_emprunt',emprunts.ajout_emprunt, name='emprunts_ajout'),
    path('emprunts/ajout_emprunt',emprunts.ajout_emprunt, name='emprunts_ajout'),
    path('livre/ajouter_livre',livre.ajouter_livre, name='livre_ajout') ,

    

]