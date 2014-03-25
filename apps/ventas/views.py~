from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.ventas.forms import ventasForm,finalizarVentaForm
from apps.ventas.models import Tabla_temporal,Venta,Productos_vendidos
from apps.productos.models import Producto
from datetime import datetime


def view_add_ventas(request):
	cuenta_total = obtener_total_venta()
	lista_tabla = Tabla_temporal.objects.all()
	form = ventasForm()
	if request.method == "POST":
		formulario = ventasForm(request.POST)
		if formulario.is_valid():#obtenemos los datos del foemulario
			id_producto = formulario.cleaned_data['codigo_producto']
			cantidad_solicitada = formulario.cleaned_data['cantidad']
			existe_codigo = Producto.objects.filter(pk=id_producto)
			if existe_codigo:#comprobamos que de verdad exista en la tabla productos
				datos_producto = Producto.objects.get(pk=id_producto)
				cantidad_existente = datos_producto.total_piezas
				existe_enTabla = Tabla_temporal.objects.filter(producto=id_producto)
				if existe_enTabla:#comprobamos si el producto exite y ane la tabla temporal
					datos_prod_exist = Tabla_temporal.objects.get(producto=id_producto)
					cantidad_en_tabla = datos_prod_exist.numero_piezas
					cantidad_total_solicitada = cantidad_en_tabla + cantidad_solicitada
					if cantidad_total_solicitada < cantidad_existente:#comprobamos que la las piezas solicitadas sea menor
						datos_prod_exist.numero_piezas = cantidad_total_solicitada# que las piezas existenetes
						datos_prod_exist.valor_piezas_vendidas = cantidad_total_solicitada * datos_producto.precio_venta
						datos_prod_exist.utilidad = (datos_producto.precio_venta - datos_producto.precio_compra)* cantidad_total_solicitada
						datos_prod_exist.save()
						msg = "Muy bien puedes agregar mas productos al carrito"
						ctx = {'lista_tabla':lista_tabla,
								'form':form,
								'msg':msg,
								'venta_total':cuenta_total}
						return render_addVentas(request,ctx)
					else:
						msg = "No se puede agregar %i piezas ya que solo existen %i \
								piezas del producto"%(cantidad_total_solicitada,cantidad_existente)
						ctx = {'lista_tabla':lista_tabla,
								'form':form,
								'msg':msg,
								'venta_total':cuenta_total}
						return render_addVentas(request,ctx)
				else:
					padd = Tabla_temporal(producto_id=id_producto,
							numero_piezas=cantidad_solicitada,
							precio_compra=datos_producto.precio_compra,
							precio_venta=datos_producto.precio_venta,
							valor_piezas_vendidas=cantidad_solicitada*datos_producto.precio_venta,
							utilidad=(datos_producto.precio_venta-datos_producto.precio_compra)*cantidad_solicitada)
					padd.save()
					msg = "El producto se a agregado correctamante"
					ctx = {'lista_tabla':lista_tabla,
							'form':form,
							'msg':msg,
							'venta_total':cuenta_total}
					return render_addVentas(request,ctx)
			else:
				msg = "El codigo de barrras ingresado no existe o aun no se ha ingresado en el sistema"
				ctx = {'lista_tabla':lista_tabla,
						'form':form,
						'msg':msg,
						'venta_total':cuenta_total}
				return render_addVentas(request,ctx)
		else:
			msg = "Los datos del formulario no son corectos, revise bien por fabor"
			ctx = {'lista_tabla':lista_tabla,
					'form':form,
					'msg':msg,
					'venta_total':cuenta_total}
			return render_addVentas(request,ctx)
	else:
		print "Fue un GET"
		msg = "Agregar productos al carrito de compras"
		ctx = {'lista_tabla':lista_tabla,
				'form':form,
				'msg':msg,
				'venta_total':cuenta_total}
		return render_addVentas(request,ctx)


def obtener_total_venta():
	t = Tabla_temporal.objects.all()
	cuenta_total = 0
	if t:
		for x in t:
			cuenta_total += x.valor_piezas_vendidas
	str_cuenta_total = str(cuenta_total)
	return str_cuenta_total

def obtener_total_utilidad_venta():
	t = Tabla_temporal.objects.all()
	cuenta_total = 0
	if t:
		for x in t:
			cuenta_total += x.utilidad
	utilidad_total = str(cuenta_total)
	return utilidad_total


def view_vender(request):
	if request.method == "POST":
		form = ventasForm()
		lista_tabla = Tabla_temporal.objects.all()
		print "Fue un POST"
		cuenta_total = obtener_total_venta()
		utilidad_total = obtener_total_utilidad_venta()
		id_personal = request.user.id
		venta = Venta(personal_id=id_personal,total_venta=cuenta_total,utilidad=utilidad_total)
		venta.save()
		lista_productos = Tabla_temporal.objects.all()
		for p in lista_productos:
			ps = Productos_vendidos()
			ps.venta_id = venta.id
			ps.producto_id = p.producto_id
			ps.precio_compra = p.precio_compra
			ps.precio_venta = p.precio_venta
			ps.piezas_vendias = p.numero_piezas
			ps.valor_piezas_vendidas = p.valor_piezas_vendidas
			ps.save()
			datos_p = Producto.objects.get(pk=p.producto_id)
			datos_p.total_piezas -= p.numero_piezas
			datos_p.save() 
			
		limpiar_tabla_temporal = Tabla_temporal.objects.all()
		limpiar_tabla_temporal.delete()
		cuenta_total = "00.0"
		msg = "La venta se llevo a cabo correctamante"
		ctx = {'lista_tabla':lista_tabla,
				'form':form,
				'msg':msg,
				'venta_total':cuenta_total}
		return render_addVentas(request,ctx)
	else:
		print "Fue un GET"
		msg = "Esta seguro(a) de querer finalizar la venta"
		titulo = "Venta de productos"
		ctx = {'msg':msg,
				'titulo':titulo}
		return render_to_response('ventas/finVenta.html',ctx,context_instance=RequestContext(request))
	
def view_cancel_venta(request):
	if request.method == "POST":
		print "Fue un POST"
		form = ventasForm()
		lista_productos = Tabla_temporal.objects.all()
		lista_productos.delete()
		cuenta_total = obtener_total_venta()
		msg = "No hay productos en el carrito de compras"
		ctx = {'lista_tabla':lista_productos,
				'form':form,
				'msg':msg,
				'venta_total':cuenta_total}
		return render_addVentas(request,ctx)
	else:
		print "Fue un GET"
		msg = "Esta seguro(a) de quierer cancelar la venta"
		titulo = "Venta de productos"
		ctx = {'msg':msg,
				'titulo':titulo}
		return render_to_response('ventas/cancelVenta.html',ctx,
										context_instance=RequestContext(request))

def render_addVentas(request,ctx):
	return render_to_response('ventas/addVentas.html',ctx,context_instance=RequestContext(request))
