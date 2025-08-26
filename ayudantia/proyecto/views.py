# Funciones para renderizar HTML y redirigir
from django.shortcuts import render, redirect
# Construir URLs por nombre (reverse) y mostrar mensajes (éxito/error)
from django.urls import reverse
from django.contrib import messages

# Funciones de autenticación: autenticar credenciales, iniciar y cerrar sesión
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Decorador que exige que el usuario esté logueado para acceder a una vista
from django.contrib.auth.decorators import login_required
# Formulario de login listo para usar (pide username y password)
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
# Modelo de usuario clásico de Django
from django.contrib.auth.models import User

# Nuestros formularios definidos arriba
from .forms import RegisterForm, EditProfileForm

def index(request):
    """
    Página de inicio simple.
    Si el usuario ya está autenticado, lo mandamos a su perfil.
    """
    if request.user.is_authenticated:              # ¿Ya está logueado?
        return redirect('proyecto:profile')        # Sí → ir a /profile
    return render(request, 'proyecto/index.html')  # No → mostrar portada

def register(request):
    """
    Muestra y procesa el formulario de registro.
    """
    if request.user.is_authenticated:
        # Si ya está logueado, no tiene sentido registrarse otra vez → ir al perfil
        return redirect('proyecto:profile')

    if request.method == 'POST':
        # Si viene por POST, el usuario envió el formulario → vincular datos
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Si todos los datos son válidos, creamos el usuario
            user = form.save(commit=False)            # crea instancia sin guardar aún
            # UserCreationForm ya se encarga de hashear la contraseña
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data.get('first_name', '')
            user.last_name = form.cleaned_data.get('last_name', '')
            user.save()                                # guarda en la base de datos (SQLite)
            messages.success(request, "Cuenta creada. ¡Ahora inicia sesión!")  # mensaje flash
            return redirect('proyecto:login')          # redirige a /login
        # Si no es válido, el template mostrará los errores automáticamente
    else:
        # Si es GET, solo mostramos el formulario vacío
        form = RegisterForm()

    # Renderiza el HTML del formulario de registro
    return render(request, 'proyecto/register.html', {'form': form})

def login_view(request):
    """
    Muestra y procesa el formulario de login.
    """
    if request.user.is_authenticated:
        # Si ya está logueado, no necesita ver el login → perfil
        return redirect('proyecto:profile')

    if request.method == 'POST':
        # Vincula los datos enviados por el usuario
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Si las credenciales son correctas, obtiene el usuario autenticado
            user = form.get_user()
            # Registra al usuario en la sesión (request.session) y marca request.user
            login(request, user)
            messages.success(request, "Has iniciado sesión.")
            # Si venía de una página protegida, respeta ?next=/ruta
            next_url = request.GET.get('next') or reverse('proyecto:profile')
            return redirect(next_url)
        else:
            # Si las credenciales fallan, se lo indicamos
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        # GET: mostramos formulario vacío de login
        form = AuthenticationForm(request)

    # Renderiza el HTML con el formulario
    return render(request, 'proyecto/login.html', {'form': form})

def logout_view(request):
    """
    Cierra la sesión del usuario actual.
    """
    logout(request)                             # Elimina datos de sesión
    messages.info(request, "Sesión cerrada.")  # Mensaje informativo
    return redirect('proyecto:index')          # Volver a la portada

@login_required  # Obliga a que el usuario esté logueado; si no, redirige a LOGIN_URL
def profile(request):
    """
    Muestra los datos del usuario logueado.
    """
    return render(request, 'proyecto/profile.html', {'usuario': request.user})

@login_required
def edit_profile(request):
    """
    Permite editar nombre, apellido y email del usuario logueado.
    """
    if request.method == 'POST':
        # Vincula los datos al formulario y a la instancia actual (request.user)
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            # Valida que no exista otro usuario con el mismo email
            email = form.cleaned_data['email'].strip().lower()
            if User.objects.filter(email=email).exclude(pk=request.user.pk).exists():
                # Si ya hay otro con ese email, error
                form.add_error('email', "Este correo ya está en uso.")
            else:
                # Si todo ok, guarda cambios
                form.instance.email = email
                form.save()
                messages.success(request, "Perfil actualizado.")
                return redirect('proyecto:profile')
    else:
        # GET: muestra el formulario pre-llenado con datos actuales del usuario
        form = EditProfileForm(instance=request.user)
    # Renderiza el formulario (con errores si los hubo)
    return render(request, 'proyecto/edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    """
    Pide confirmación y, si aceptan, elimina la cuenta del usuario logueado.
    """
    if request.method == 'POST':
        # Si el usuario confirma (envía el formulario), borramos la cuenta
        request.user.delete()
        messages.warning(request, "Tu cuenta ha sido eliminada.")
        return redirect('proyecto:index')
    # GET: muestra la página de confirmación
    return render(request, 'proyecto/delete_profile.html', {'usuario': request.user})

@login_required
def password_change(request):
    """
    Vista para cambiar la contraseña del usuario actual.
    - Requiere estar logueado (@login_required).
    - Verifica la contraseña actual y que las dos nuevas coincidan.
    """
    if request.method == 'POST':
        # Vinculamos los datos enviados al formulario
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()                        # guarda nueva contraseña (hasheada)
            update_session_auth_hash(request, user)   # mantiene la sesión activa tras el cambio
            messages.success(request, "Contraseña actualizada correctamente.")
            return redirect('proyecto:profile')       # volver al perfil
    else:
        # GET: mostramos formulario vacío asociado al usuario actual
        form = PasswordChangeForm(user=request.user)

    return render(request, 'proyecto/password_change.html', {'form': form})