$(document).ready(function() {
    $('#FormComentario').formValidation({
        framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            usuario: {
                validators: {
                    notEmpty: {
                        message: 'El nombre es requerido'
                    },
                    stringLength: {
                        min: 5,
                        max: 30,
                        message: 'Por favor escriba correctamente su nombre'
                    },
                    regexp: {
                        regexp: /^[a-zA-Z]+$/,
                        message: 'Por favor escriba correctamente su nombre'
                    }
                }
            },
            comentario: {
                validators: {
                    notEmpty: {
                        message: 'El comentario es requerido'
                    }
                }
            }
        }
    });
});