function validarFormulario() {
  // Obtener el formulario y los valores de los campos de entrada
  var form = document.getElementById('login-form');
  var nombres = form.elements['Nombres'].value;
  var apaterno = form.elements['ApellidoPA'].value;
  var amaterno = form.elements['ApellidoMa'].value;
  var gender = form.elements['Genero'].value;
  var rut = form.elements['rut'].value;
  var direccion = form.elements['Direccion'].value;
  var correo = form.elements['Correo'].value;
  var cell = form.elements['Cell'].value;

  // Verificar que todos los campos estén llenos
  if (nombres == '' || apaterno == '' || amaterno == '' || gender == '' || rut == '' || direccion == '' || correo == '' || cell == '') {
    alert('Por favor, complete todos los campos');
    return false;
  } else {
    // Redireccionar al usuario a index.html
    window.location.href = 'index.html';
  }
}
