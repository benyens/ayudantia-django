# Formularios HTML en Django
from django import forms
# Formulario ya hecho por Django para crear usuarios correctamente (valida contraseñas)
from django.contrib.auth.forms import UserCreationForm
# Modelo User de Django (usuario estándar)
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    """
    Formulario de registro que extiende el de Django para añadir email/nombre.
    """
    # Campo email obligatorio
    email = forms.EmailField(required=True)
    # Nombre y apellido (opcionales)
    first_name = forms.CharField(label="Nombre", required=False, max_length=30)
    last_name = forms.CharField(label="Apellido", required=False, max_length=30)

    class Meta:
        # Indica que este formulario crea/edita instancias del modelo User
        model = User
        # Campos que se mostrarán en el formulario y en este orden
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def clean_email(self):
        """
        Valida que el email no esté repetido en otro usuario.
        """
        email = self.cleaned_data['email'].strip().lower()  # normaliza
        if User.objects.filter(email=email).exists():       # consulta en DB
            raise forms.ValidationError("Este correo ya está registrado.")
        return email

class EditProfileForm(forms.ModelForm):
    """
    Formulario para editar el perfil (nombre, apellido, email).
    """
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")  # Campos editables

