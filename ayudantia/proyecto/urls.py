from django.urls import path
from . import views

# Namespace de la app (para usar 'proyecto:login', etc.)
app_name = 'proyecto'

# Lista de rutas específicas de esta app
urlpatterns = [
    path('', views.index, name='index'),                     # Página de inicio
    path('login/', views.login_view, name='login'),          # Formulario de inicio de sesión
    path('register/', views.register, name='register'),      # Formulario de registro de usuario
    path('logout/', views.logout_view, name='logout'),       # Cerrar sesión
    path('profile/', views.profile, name='profile'),         # Ver perfil (requiere login)
    path('edit_profile/', views.edit_profile, name='edit_profile'),   # Editar perfil (requiere login)
    path('delete_profile/', views.delete_profile, name='delete_profile'), # Eliminar cuenta (requiere login)
    path('change_password/', views.password_change, name='change_password'), # Cambiar contraseña (requiere login)
]