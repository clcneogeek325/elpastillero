
$(document).ready(function(){
					$("#id_recibi").keyup(function(evento){
						var totalVenta = $("#id_total_venta").attr("value");
						var recibi  = $("#id_recibi").attr("value");
						$("#id_cambio").attr("value",parseInt(recibi)-parseInt(totalVenta));
					});
				});

			
				