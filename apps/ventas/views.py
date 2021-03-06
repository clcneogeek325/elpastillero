from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.ventas.forms import ventasForm,finVentaForm
from apps.ventas.models import Tabla_temporal,Venta,Productos_vendidos
from apps.productos.models import Producto
from datetime import datetime
from django.http import HttpResponseRedirect
from apps.Personal.models import Personal


def view_tiket(request):
	personal = obt_personal(request)
	productos = Tabla_temporal.objects.filter(personal_id=personal.id)
	total = obtener_total_venta(personal)
	ctx = {'lista_p':productos,'total':total}
	return render_to_response('ventas/tiket.txt',ctx,
			context_instance=RequestContext(request))


def obt_personal(request):
	return Personal.objects.get(user_id=request.user.id)
	
def personal_existe(request):
	return Personal.objects.filter(user_id=request.user.id)


def porce(parte,total):
	return 100 * float (parte ) /float ( total)
	

def p(parte,total):
	return (total /100) * parte


def view_add_p_sin_cod(request,id_producto):
	if request.user.is_authenticated():
		if request.method == "POST":
			print "Fue un POST"
		else:
			print "Fue un GET"
			form = ventasForm(initial={'codigo_producto':id_producto})
			ctx = {'form':form}
		return render_to_response('ventas/addProdSinCod.html',ctx,
				context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')

def view_ls_p_sin_cod(request):
	if request.user.is_authenticated():
		if request.method == "POST":
			print "Fue un POST"
		else:
			ls_prods = Producto.objects.all()
			if ls_prods:
				print "Fue un GET"
				lista_productos = Producto.objects.filter(tiene_codigo=False)
				msg = "Elija un producto para agregar al carrtio"
				titulo = "Elegir un producto"
				status_add_producto = "active"
				ctx = {'status_add_producto':status_add_producto,
						'titulo':titulo,
						'msg':msg,
						'lista_productos':lista_productos}
				return render_to_response('ventas/lstProductos.html',ctx,
						context_instance=RequestContext(request))
			else:
				return HttpResponseRedirect('/addVentas/0/')
	else:
		return HttpResponseRedirect('/login')

def view_delt_producto(request,id_producto):
	if request.user.is_authenticated():
		if request.method == "POST":
			print "Fue un POST"
			prod = Tabla_temporal.objects.get(pk=id_producto)
			prod.delete()
			return HttpResponseRedirect('/addVentas/0/')
		else:
			print "Fue un GET"
			msg = "De Verdad desea eliminar este proucto de la venta actual"
			titulo = "Eliminar un producto del carrito"
			ctx = {'titulo':titulo,
					'msg':msg}
			return render_to_response('ventas/delProduc.html',ctx,
					context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')




def view_add_ventas(request,id_producto):
	if request.user.is_authenticated():
		if Personal.objects.exists() and personal_existe(request):
			personal = obt_personal(request)
			lista_tabla = Tabla_temporal.objects.filter(personal_id=personal.id)
			form = ventasForm()
			if id_producto != "0":
				form = ventasForm(initial={'codigo_producto':id_producto})
			if request.method == "POST":
				formulario = ventasForm(request.POST)
				if formulario.is_valid():#obtenemos los datos del formulario
					id_producto = formulario.cleaned_data['codigo_producto']
					cantidad_solicitada = formulario.cleaned_data['cantidad']
					existe_codigo = Producto.objects.filter(pk=id_producto)
					if existe_codigo:#comprobamos que de verdad exista en la tabla productos
						datos_producto = Producto.objects.get(pk=id_producto)
						cantidad_existente = datos_producto.total_piezas
						existe_enTabla = Tabla_temporal.objects.filter(producto=id_producto,personal_id=personal.id)
						precio_de_venta = 0.0
						#saber si tiene descuento
						P = obt_personal(request)
						if P.pc.categoria == datos_producto.categoria:
							precio_de_venta = p(P.pc.porcentage_descuento,datos_producto.precio_venta)
							print "es generico"
						else:
							precio_de_venta = datos_producto.precio_venta
							#====================
						if existe_enTabla:#comprobamos si el producto exite y ane la tabla temporal
							datos_prod_exist = Tabla_temporal.objects.get(producto=id_producto,personal_id=personal.id)
							cantidad_en_tabla = datos_prod_exist.numero_piezas
							cantidad_total_solicitada = cantidad_en_tabla + cantidad_solicitada
							if cantidad_total_solicitada < cantidad_existente:#comprobamos que la las piezas solicitadas sea menor
								datos_prod_exist.numero_piezas = cantidad_total_solicitada# que las piezas existenetes
								datos_prod_exist.valor_piezas_vendidas = cantidad_total_solicitada * precio_de_venta
								datos_prod_exist.utilidad = (precio_de_venta - datos_producto.precio_compra)* cantidad_total_solicitada
								datos_prod_exist.save()
								return HttpResponseRedirect('/addVentas/0/')
							else:
								cuenta_total = obtener_total_venta(personal.id)
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
									precio_venta=precio_de_venta,
									valor_piezas_vendidas=cantidad_solicitada*precio_de_venta,
									utilidad=(precio_de_venta-datos_producto.precio_compra)*cantidad_solicitada,
									personal_id=personal.id,
									porcentage_descuento=0)
							padd.save()
							return HttpResponseRedirect('/addVentas/0/')
					else:
						cuenta_total = obtener_total_venta(personal.id)
						msg = "El codigo de barrras ingresado no existe o aun no se ha ingresado en el sistema"
						ctx = {'lista_tabla':lista_tabla,
								'form':form,
								'msg':msg,
								'venta_total':cuenta_total}
						return render_addVentas(request,ctx)
				else:
					cuenta_total = obtener_total_venta(personal.id)
					msg = "Los datos del formulario no son corectos, revise bien por fabor"
					ctx = {'lista_tabla':lista_tabla,
							'form':form,
							'msg':msg,
							'venta_total':cuenta_total}
					return render_addVentas(request,ctx)
			else:
				cuenta_total = obtener_total_venta(personal.id)
				print "Fue un GET"
				msg = "Agregar productos al carrito de compras"
				ctx = {'lista_tabla':lista_tabla,
						'form':form,
						'msg':msg,
						'venta_total':cuenta_total}
				return render_addVentas(request,ctx)
		else:
			return render_to_response('ventas/errorPersonal.html',context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')


def obtener_total_venta(personal):
	t = Tabla_temporal.objects.filter(personal_id=personal)
	cuenta_total = 0
	if t:
		for x in t:
			cuenta_total += x.valor_piezas_vendidas
	str_cuenta_total = str(cuenta_total)
	return str_cuenta_total

def obtener_total_utilidad_venta(personal):
	t = Tabla_temporal.objects.filter(personal_id=personal)
	cuenta_total = 0
	if t:
		for x in t:
			cuenta_total += x.utilidad
	utilidad_total = str(cuenta_total)
	return utilidad_total


def view_vender(request):
	if request.user.is_authenticated():
		personal = obt_personal(request)
		if request.method == "POST":
			form = ventasForm()
			lista_tabla = Tabla_temporal.objects.filter(personal_id=personal.id)
			print "Fue un POST"
			cuenta_total = obtener_total_venta(personal.id)
			utilidad_total = obtener_total_utilidad_venta(personal.id)
			venta = Venta(personal_id=personal.id,total_venta=cuenta_total,utilidad=utilidad_total)
			venta.save()
			lista_productos = Tabla_temporal.objects.filter(personal_id=personal.id)
			for p in lista_productos:
				ps = Productos_vendidos()
				ps.venta_id = venta.id
				ps.producto_id = p.producto_id
				ps.precio_compra = p.precio_compra
				ps.precio_venta = p.precio_venta
				ps.piezas_vendias = p.numero_piezas
				ps.valor_piezas_vendidas = p.valor_piezas_vendidas
				ps.porcentage_descuento = p.porcentage_descuento
				ps.save()
				datos_p = Producto.objects.get(pk=p.producto_id)
				datos_p.total_piezas -= p.numero_piezas
				datos_p.save()
			
			limpiar_tabla_temporal = Tabla_temporal.objects.filter(personal_id=personal.id)
			limpiar_tabla_temporal.delete()
			return HttpResponseRedirect('/addVentas/0/')
		else:
			lista_prodts = Tabla_temporal.objects.filter(personal_id=personal.id)
			if lista_prodts:
				print "Fue un GET"
				productos = Tabla_temporal.objects.filter(personal_id=personal.id)
				total_v = obtener_total_venta(personal)
				form = finVentaForm(initial={'total_venta':total_v})
				msg = "Esta seguro(a) de querer finalizar la venta"
				titulo = "Venta de productos"
				ctx = {'msg':msg,
						'titulo':titulo,'form':form}
				return render_to_response('ventas/finVenta.html',ctx,context_instance=RequestContext(request))
			else:
				return HttpResponseRedirect('/addVentas/0/')
	else:
		return HttpResponseRedirect('/login')
	
	
def view_cancel_venta(request):
	if request.user.is_authenticated():
		personal = obt_personal(request)
		if request.method == "POST":
			print "Fue un POST"
			form = ventasForm()
			lista_productos = Tabla_temporal.objects.filter(personal_id=personal.id)
			lista_productos.delete()
			return HttpResponseRedirect('/addVentas/0/')
		else:
			lista_prodts = Tabla_temporal.objects.filter(personal_id=personal.id)
			if lista_prodts:
				print "Fue un GET"
				msg = "Esta seguro(a) de quierer cancelar la venta"
				titulo = "Venta de productos"
				ctx = {'msg':msg,
						'titulo':titulo}
				return render_to_response('ventas/cancelVenta.html',ctx,
												context_instance=RequestContext(request))
			else:
				return HttpResponseRedirect('/addVentas/0/')
	else:
		return HttpResponseRedirect('/login')


def render_addVentas(request,ctx):
	if request.user.is_authenticated():
		return render_to_response('ventas/addVentas.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')
