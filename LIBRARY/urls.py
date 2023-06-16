from LIBRARY.views.lecteure import delete
from django.contrib import admin
from django.urls import path
from LIBRARY.views import *


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', home.index, name='home'),
    path('contact', home.contact, name='contact'),
    path('ajout_lecteur/', lecteure.add, name='lecteur_add'),
    path('lecteurs/', lecteure.index, name='lecteur_index'),
    path('emprunts/', emprunts.index, name='emprunt_index'),
    path('lecteur_edit', lecteure.edit, name='lecteur_edit'),
    path('lecteur_delete', lecteure.delete, name='lecteur_delete'),
    path('lecteur_update', lecteure.update, name='lecteur_update'),
]