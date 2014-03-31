$(document).ready(function(){
					$("#id_descuento_compra").keyup(function(evento){
						var precio_farmacia=$("#id_precio_farmacia").attr("value");
						var descuento_compra=$("#id_descuento_compra").attr("value");
						var descuento=(precio_farmacia/100)*descuento_compra;
						$("#id_precio_compra").attr("value",precio_farmacia-descuento);
					});
					
					$("#id_descuento_venta").keyup(function(evento){
						var precio_compra=$("#id_precio_compra").attr("value");
						var descuento_venta=$("#id_descuento_venta").attr("value");
						var set_porcentege=(precio_compra/100)*descuento_venta;
						$("#id_precio_venta").attr("value",parseInt(precio_compra)+parseInt(set_porcentege));
						$("#id_ganancia").attr("value",parseInt(set_porcentege));
					});

				});

			
				
				
