from tkinter.font import names

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('skills', views.skill, name='skill'),
    path('hh_p', views.hh_p, name='hh_p'),
    path('geography', views.geography, name='geography')
]
