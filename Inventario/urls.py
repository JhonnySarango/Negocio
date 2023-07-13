from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns=[
    path('',views.index, name="index"),
    path('<int:id>', views.view_libro, name='view_libro'),
    path('add', views.add, name='add'),
    path('edit/<int:id>/', views.edita, name='edit'),
    path('eliminar/<int:id>/', views.delete, name='eliminar'),
    path('register/',views.registra, name='register'),
    path('login/',LoginView.as_view(template_name='Inventario/login.html'), name='login'),
    path('logout/',LogoutView.as_view(template_name='Inventario/logout.html'), name='logout'),
] 