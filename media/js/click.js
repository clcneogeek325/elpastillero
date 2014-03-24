$(document).ready(function(){
					$("#id_siguiente").click(function(evento){
						alert("Se ha dado un click");
						var dato1=$("#id_codigo").attr("value");
						var dato2="/rmProducto/";
						suma=dato2+dato1;
						$("#id_href").attr("href",suma)
						
					});
				});

