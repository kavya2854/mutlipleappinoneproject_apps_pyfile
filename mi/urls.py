from django.urls import path
from mi.views import *
app_name = 'anything'
urlpatterns = [
path('rohit/',rohit,name='rohit'),
path('bumrah/',bumrah,name='bumrah'),
]