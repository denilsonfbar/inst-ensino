from django.urls import path
from academico import views

urlpatterns = [
    path('', views.index, name='index'),
]
