from django.contrib import admin
from django.urls import path
from LIBRARY.views import *


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', home.index, name='home'),
    path('contact', home.contact, name='contact'),
    path('emprunts/', emprunts.index, name='emprunt_index'),
]