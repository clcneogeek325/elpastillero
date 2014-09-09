$(document).ready(function(){
        
        $('#id_codigo').keyup(function(){
        var dato=$('#id_codigo').val();
                $.ajax({
                                     
                          type:"GET",
                          contentType:"application/json; charset=utf-8",
                          dateType:"json",
                          url:"/ws/prod/buscar"+dato,
                                        success: function(respuesta) {
                                                
                                        }
                });
                
        });
        
});
