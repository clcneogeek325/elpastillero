$(document).ready(function(evento){
        
        $('#id_compania').change(function(e){
                var id_proveedor = $('#id_compania').val();
                $.ajax({
                                        url: "/ws/prov/"+id_proveedor,
                                        type:"GET",
                                        contentType:"application/json; charset=utf-8",
                                        dateType:"json",
                                        success: function(respuesta) {
                                              var proveedor = respuesta;
                                              $('#id_proveedor').val(proveedor[0].pk);
                                        }
                });
                
        });

});

