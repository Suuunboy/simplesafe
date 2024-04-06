from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testpage', views.testpage, name='testpage'),
    path('advices', views.advices, name='advices'),
    path('materials', views.materials, name='materials'),
    path('results', views.results, name='results'),
]