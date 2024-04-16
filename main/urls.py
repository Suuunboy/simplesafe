from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('testpage', views.testpage, name='testpage'),
    path('advices', views.advices, name='advices'),
    path('materials', views.materials, name='materials'),
    path('result', views.result, name='result'),
    path('results', views.result, name='results'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)