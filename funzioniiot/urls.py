from django.urls import path, include
from . import views
from funzioniiot.views import AboutView

from funzioniiot.views import titoloDetailView, TitoloDetailViewCB, home, Titoli_list_view, Clienti_list_view

from django.views.generic import TemplateView

from django.urls import path
from . import views  

app_name = 'titol'
urlpatterns = [
    # post views
    path('', views.titoli_list, name='titoli_list'),
    path('clienti', views.Clienti_list_view, name='clienti_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.titoli_detail, name='titoli_detail'),
    path('titoli2/titolosingolo/<int:pk>', TitoloDetailViewCB.as_view(), name ='titolo_detail'),
    path('lista_titoli', Titoli_list_view.as_view(), name ='titolo_detail'),
    path('lista_clienti', Clienti_list_view.as_view(), name ='cliente_detail'),
    
]