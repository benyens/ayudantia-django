// Aquí se pueden crear funciones JavaScript para manejar la lógica de la aplicación

// Pequeño ejemplo de función que muestra un mensaje en pantalla
function mostrarMensaje(tipo, mensaje) {
    const contenedor = document.getElementById('mensajes');
    const nuevoMensaje = document.createElement('div');
    nuevoMensaje.className = `alert alert-${tipo}`;
    nuevoMensaje.textContent = mensaje;
    contenedor.appendChild(nuevoMensaje);
}
