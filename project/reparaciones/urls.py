from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('perfil/', views.perfil, name='perfil'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('crear_reparacion/', views.crear_reparacion, name='crear_reparacion'),
    path('editar_reparacion/<int:pk>/', views.editar_reparacion, name='editar_reparacion'),
    path('eliminar_reparacion/<int:pk>/', views.eliminar_reparacion, name='eliminar_reparacion'),
]
