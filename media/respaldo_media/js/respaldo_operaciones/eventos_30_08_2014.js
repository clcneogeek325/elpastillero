function tipo_compania(){

	var prov=$("#id_compania").attr("value");
	if(prov == "6" || prov == "7"){
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
		var precio_compra = $("#id_precio_compra").attr("value");
		var precio_farmacia = $("#id_precio_farmacia").attr("value");
		$("#id_ganancia").attr("value",parseInt(precio_venta)-parseInt(precio_compra));

	});


	}
	if(prov == "11" || prov == "12"){
			$("#id_descuento_compra").keyup(function(evento){
			
			if(parseInt($("#id_descuento_compra").attr("value")) == 0)
					{
					var precio_farmacia = $("#id_precio_farmacia").attr("value");
					$("#id_precio_compra").attr("value",precio_farmacia);
		
					}else{
					var precio_farmacia=$("#id_precio_sugerido").attr("value");
					var descuento_compra=$("#id_descuento_compra").attr("value");
					var descuento=(precio_farmacia/100)*descuento_compra;
					$("#id_precio_compra").attr("value",precio_farmacia-descuento);
					}


			});
		

		$("#id_descuento_venta").keyup(function(evento){
			var precio_sugerido=$("#id_precio_sugerido").attr("value");
			var descuento_venta=$("#id_descuento_venta").attr("value");
			var set_porcentege=(precio_sugerido/100)*descuento_venta;
			$("#id_precio_venta").attr("value",parseInt(precio_sugerido)-parseInt(set_porcentege));
			var precio_venta=$("#id_precio_venta").attr("value");
			var precio_compra=$("#id_precio_compra").attr("value");
			$("#id_ganancia").attr("value",(parseInt(precio_venta))-(parseInt(precio_compra)));
		});
	}
	if(prov == "13" || prov == "14" || prov == "10" || prov == "25"){
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
						var precio_compra = $("#id_precio_compra").attr("value");
						var precio_venta = $("#id_precio_venta").attr("value");
						$("#id_ganancia").attr("value",parseInt(precio_venta)-parseInt(precio_compra));

					});

	}
	}
	
$(document).ready(function(){
	
			$("#id_descuento_compra").keyup(function(evento){
			tipo_compania();
			});

			$("#id_descuento_venta").keyup(function(evento){
			tipo_compania();
			
		});
		
	});
