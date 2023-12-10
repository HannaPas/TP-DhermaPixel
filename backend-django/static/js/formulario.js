const formulario = document.getElementById('formulario');

formulario.addEventListener('submit', (e) => {
    e.preventDefault();

    fetch('https://sheet.best/api/sheets/e394b8e0-102f-4bed-bfba-c9ebf3cec357', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "nombre": formulario.nombre.value,
            "apellido": formulario.apellido.value,
            "dni": formulario.dni.value,
            "genero": formulario.genero.value,
            "correo": formulario.correo.value,
            "contraseña": formulario.contraseña.value,
            "fnacimiento": formulario.fNacimiento.value
        })
    })
        .then(response => response.json())
        .then(data => {
            formulario.reset();
            alert('Registro exitoso');  // Mostrar una alerta
        })
        .catch(error => {
            console.error('Hubo un error al enviar los datos:', error);
        });
});
