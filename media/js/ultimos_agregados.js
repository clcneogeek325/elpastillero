$(document).ready(function(e){
 
$.ajax({
                  type:"GET",
                  contentType:"application/json; charset=utf-8",
                  dateType:"json",
                  url:"/ws/mercancia/",

                  success: function(respuesta) {
                          var lista = respuesta;
                          for (var i = 0; i < lista.length; i++) {
                            $.ajax({
                                                 type:"GET",
                                                 contentType:"application/json; charset=utf-8",
                                                 dateType:"json",
                                                 url:"/ws/producto/"+lista[i].fields.producto,
                                                 success: function(data) {
                                                        var datos = data;
                                                 $('#prod').append("<p> Codigo: "+data[0].pk+"</p>");
                                                 $('#prod').append("<p> Nombre: "+data[0].fields.nombre_producto+"</p>");

                                                    }
                            });
                            
                          };
                        }
});


});
