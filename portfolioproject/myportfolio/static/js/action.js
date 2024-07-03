document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('contactForm');

    form.addEventListener('submit', function(event) {
        // Evitar el envío del formulario
        event.preventDefault();

        // Capturar los valores de los campos
        const name = document.getElementById('name').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const email = document.getElementById('email').value.trim();
        const message = document.getElementById('Mensaje').value.trim();

        // Variables para controlar la validación
        let isValid = true;

        // Validar nombre (no vacío)
        if (name === "") {
            isValid = false;
            alert("El campo de nombre no puede estar vacío.");
        }

        // Validar teléfono (formato correcto)
        const phonePattern = /^\([0-9]{2}\) [0-9]{3}-[0-9]{4}$/;
        if (!phonePattern.test(phone)) {
            isValid = false;
            alert("El teléfono debe seguir el formato (XX) XXX-XXXX.");
        }

        // Validar email (formato correcto)
        const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        if (!emailPattern.test(email)) {
            isValid = false;
            alert("Por favor, ingresa un correo electrónico válido.");
        }

        // Validar mensaje (no vacío)
        if (message === "") {
            isValid = false;
            alert("El campo de mensaje no puede estar vacío.");
        }

        // Si todo es válido, enviar el formulario
        if (isValid) {
            form.submit();
        }
    });
});
