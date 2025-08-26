# Proyecto Django - Ayudantía (Borrador)

Este proyecto es un ejemplo didáctico para entender cómo funciona la autenticación básica en Django.  
La idea es que sirva como guía de apoyo en la ayudantía, no como un sistema final.

## Objetivo

- Mostrar cómo crear un proyecto Django con una aplicación (`proyecto`).
- Implementar las funciones más comunes de gestión de usuarios usando `django.contrib.auth`:
  - Registro de usuario
  - Inicio de sesión (login)
  - Cierre de sesión (logout)
  - Visualización del perfil
  - Edición del perfil
  - Eliminación de la cuenta
  - Cambio de contraseña

Todo esto usando la base de datos SQLite que viene por defecto en Django.

## Requisitos

- Python 3.x  
- pip (gestor de paquetes)  
- [Django](https://www.djangoproject.com/) instalado

Instalación rápida de Django:

```bash
pip install django
```

## Cómo ejecutar el proyecto

1. Clonar o copiar este repositorio.
2. Entrar a la carpeta del proyecto.
3. Crear la base de datos y aplicar migraciones:

```bash
python manage.py migrate
```

4. Ejecutar el servidor de desarrollo:

```bash
python manage.py runserver
```

5. Abrir en el navegador:  
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Funcionalidades principales

- `/register/` → Registro de nuevos usuarios  
- `/login/` → Inicio de sesión  
- `/logout/` → Cerrar sesión  
- `/profile/` → Ver perfil (requiere login)  
- `/edit_profile/` → Editar datos básicos del usuario  
- `/delete_profile/` → Eliminar cuenta (con confirmación)  
- `/password_change/` → Cambiar la contraseña

## Notas importantes

- Este es solo un borrador para que puedan utilizar como base o inspiración.  
- Se utilizó `django.contrib.auth`, lo que facilita el manejo de usuarios y contraseñas seguras.  

## Qué se aprende con este proyecto

- Cómo organizar un proyecto Django con apps, urls, views y templates.  
- Cómo trabajar con sesiones e inicio/cierre de sesión.  
- Cómo usar formularios integrados de Django (`UserCreationForm`, `AuthenticationForm`, `PasswordChangeForm`).  
- Cómo mostrar mensajes al usuario con `django.contrib.messages`.  

## Estado del proyecto

Este proyecto no está pensado para ser usado tal cual, sino como un ejemplo de referencia durante la ayudantía.  
Puede servir como base para otros proyectos más completos.
