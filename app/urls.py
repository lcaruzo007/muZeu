from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_objetos, name='lista_objetos'),
    path('<int:pk>/', views.detalhe_objeto, name='detalhe_objeto'),
]
