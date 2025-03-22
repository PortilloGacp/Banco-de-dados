
from django.conf import settings
from django.conf.urls.static import static
from app_projeto import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),

    path('dados', views.dados,name='dados_usuarios' ),

]


 


