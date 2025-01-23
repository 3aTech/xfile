function cne() {
    // Obtener el valor seleccionado del radio button
    var nacionalidad = $('input[name="nacionalidad"]:checked').val();
    // Obtener el valor del input
    var dni = document.getElementById("CI-RIF").value;
    
    $.ajax({
        url: "cne",
        type: "GET",
        data: {
            nacionalidad: nacionalidad,
            dni: dni
        },
        
        success: function(response) {
            if (response.result) {
                document.getElementById("desc_user").value = response.result;
            } else if (response.error) {
                alert(response.error);
            }
        },
        error: function(response) {
            alert("Ocurrió un error");
        }
    });
}

function genCodes() {
     // Obtener el valor del input
    var nacionalidad = document.getElementById("co_user").value;
    
    $.ajax({
        url: "cne",
        type: "GET",
        data: {
            nacionalidad: nacionalidad,
            dni: dni
        },
        
        success: function(response) {
            if (response.result) {
                document.getElementById("co_user").value = response.result;
            } else if (response.error) {
                alert(response.error);
            }
        },
        error: function(response) {
            alert("Ocurrió un error");
        }
    });
}

$(document).ready(function() {
    $('#button-addon2').on('click', function(event) {
        event.preventDefault();  // Previene la recarga de la página
        executeFunction();
    });
});