# Creamos un archivo decorators.py para definir decoradores personalizados que revisen los request.session.
from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse 

# Esta función verifica si el usuario está autenticado
def login_required(view_func): # Decorador para requerir inicio de sesión
    @wraps(view_func) # Mantiene la información de la función original
    def _wrapped_view(request, *args, **kwargs): # Función envolvente
        if not request.session.get('user_id'): # Verifica si el usuario está autenticado
            return redirect(reverse('proyecto:login')) # Redirige a la página de inicio de sesión
        return view_func(request, *args, **kwargs) # Llama a la función de vista original
    return _wrapped_view # Devuelve la función envolvente