$(document).ready(function(){
					$("#id_descuento_compra").keyup(function(evento){
						var precio_farmacia=$("#id_precio_farmacia").attr("value");
						var descuento_compra=$("#id_descuento_compra").attr("value");
						var descuento=(precio_farmacia/100)*descuento_compra;
						$("#id_precio_compra").attr("value",precio_farmacia-descuento);
					});
					
					$("#id_descuento_venta").keyup(function(evento){
						var descuento_venta = $("#id_descuento_venta").attr("value");
						var precio_sugerido=$("#id_precio_sugerido").attr("value");
						
						var porcentage=(precio_sugerido/100)*descuento_venta;
						$("#id_precio_venta").attr("value",precio_sugerido);
						$("#id_precio_venta").attr("value",parseInt(precio_sugerido)-parseInt(porcentage));
						var precio_venta = $("#id_precio_venta").attr("value");
						var precio_farmacia = $("#id_precio_farmacia").attr("value");
						$("#id_ganancia").attr("value",parseInt(precio_venta)-parseInt(precio_farmacia));

					});

/*
					$("#id_descuento_venta").keyup(function(evento){
						var precio_compra=$("#id_precio_compra").attr("value");
						var descuento_venta=$("#id_descuento_venta").attr("value");
						var set_porcentege=(precio_compra/100)*descuento_venta;
						$("#id_precio_venta").attr("value",parseInt(precio_compra)+parseInt(set_porcentege));
						$("#id_ganancia").attr("value",parseInt(set_porcentege));
					});
*/                               
                               
				});

			
				
				
