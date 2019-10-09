from django.urls import path

from . import views

app_name = 'listas'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('personas/', views.PersonaList.as_view(), name='personasList'),
    path('congresos/', views.CongresoList.as_view(), name='congresosList'),
    path('personas/<int:pk>', views.PersonaDetail.as_view(), name='personaDetail'),
    path('congresos/<int:pk>', views.CongresoDetail.as_view(), name='congresoDetail'),
]