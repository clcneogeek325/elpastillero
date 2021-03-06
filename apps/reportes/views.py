#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.db import connection
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect,HttpResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render_to_response
from apps.ventas.models import Venta
from django.db.models import Sum
from apps.ventas.models import Productos_vendidos
from apps.reportes.forms import getMejorProveedor
from apps.productos.models import Mejor_proveedor
from django.db.models import Avg, Max, Min, Count
from apps.reportes.forms import getFechaForm,getRangoFechaForm,getCampoForm,getDosFechasForm
from apps.productos.models import Producto
from datetime import datetime,timedelta
from apps.mercancia.models import Mercancia
from django.shortcuts import render_to_response





def view_corte_de_caja(request):
	if request.method == "POST":
		print "Esto fuen un post"
		form = getDosFechasForm(request.POST) 
		if form.is_valid():
			tipo_de_turno = form.cleaned_data['tipo_turno']
			fecha = str(form.cleaned_data['fecha'])
			hora1 = 0
			hora2 = 0
			if tipo_de_turno == "vt":
				hora1  = 7
				hora2 = 18
			else:	
				hora1  = 18
				hora2 = 22
 			dt_hora1 = datetime.strptime(("%s %i:00"%(fecha,hora1)), "%Y-%m-%d %H:%M")
 			dt_hora2 = datetime.strptime(("%s %i:00"%(fecha,hora2)), "%Y-%m-%d %H:%M")
			ps = Productos_vendidos.objects.filter(fecha_venta__gte=dt_hora1,fecha_venta__lte=dt_hora2)
			lista = ps.values_list('producto', flat=True).distinct().order_by()
			ls_cantidad_prodts = []
			ls_efectivo_generado = []
			for x in lista:
				ls_cantidad_prodts.append(ps.filter(producto=x).aggregate(Sum('piezas_vendias')).__getitem__(0))
				ls_efectivo_generado.append(ps.filter(producto=x).aggregate(Sum('valor_piezas_vendidas')).__getitem__(0))
				
			titulo = "Corte de Caja"
			msg = "Estos son los productos vendidos"
			ctx = {'productos':lista,
					'msg':msg,
					'ls_cantidad_prodts':ls_cantidad_prodts,
					'ls_efectivo_generado':ls_efectivo_generado,
					'titulo':titulo}
			return render_to_response('reportes/pdf/corte_pdf.html',ctx,
					context_instance=RequestContext(request))
		
		else:
			form = getDosFechasForm()
			ctx = {'form':form}
			return render_to_response('reportes/cortecaja.html',ctx,
				context_instance=RequestContext(request))
	else:
		form = getDosFechasForm()
		ctx = {'form':form}
		return render_to_response('reportes/cortecaja.html',ctx,
			context_instance=RequestContext(request))


def view_search_mercancia(request):
	if request.method == "POST":
		print "Fue un POST"
		form = getRangoFechaForm(request.POST)
		formcampo = getCampoForm(request.POST)
		if form.is_valid() and formcampo.is_valid():
			fechainicio = form.cleaned_data['fechauno']
			fechafin = form.cleaned_data['fechados']
			tipobusqueda = formcampo.cleaned_data['campo']
			busqueda = formcampo.cleaned_data['busqueda']
			dt_fecha1 = datetime.strptime(str(fechainicio), "%Y-%m-%d")
			dt_fecha2 = datetime.strptime(str(fechafin), "%Y-%m-%d")
			
			print 'buscar',busqueda,' en ',tipobusqueda
			if tipobusqueda == "fecha":
				merca = Mercancia.objects.filter(fecha_ingreso__gte=dt_fecha1,
								fecha_ingreso__lte=dt_fecha2)
			else:
				if tipobusqueda == "factura" and busqueda != "":
					merca = Mercancia.objects.filter(fecha_ingreso__gte=dt_fecha1,
									fecha_ingreso__lte=dt_fecha2,
									factura=busqueda)
				elif tipobusqueda == "categoria" and busqueda != "":
					merca = Mercancia.objects.filter(fecha_ingreso__gte=dt_fecha1,
								fecha_ingreso__lte=dt_fecha2,
								categoria=busqueda)
				elif tipobusqueda == "compania" and busqueda != "":
					merca = Mercancia.objects.filter(fecha_ingreso__gte=dt_fecha1,
								fecha_ingreso__lte=dt_fecha2,
								compania=busqueda)
				else:
					merca = {}

			titulo = "Estos son los resultado encontrados"
			msg = "Esta es la lista de la mercancia ingresada por este periodo de tiempo"
			ctx = {'titulo':titulo,
				'msg':msg,
				'lista_merca':merca}
			html = render_to_string('reportes/pdf/pdfMercancia.html',ctx,
								context_instance=RequestContext(request))
			return generar_pdf(html)
		else:
			print "El formulrio no es valido"
			form = getRangoFechaForm()
			formcampo = getCampoForm()
			ctx = {'form':form,'formcampo':formcampo}
			return render_to_response('reportes/buscarMercancia.html',ctx,
							context_instance=RequestContext(request))
			
	else:
		print "Fue un GET"
		form = getRangoFechaForm()
		formcampo = getCampoForm()
		ctx = {'form':form,'formcampo':formcampo}
		return render_to_response('reportes/buscarMercancia.html',ctx,
							context_instance=RequestContext(request))


def view_prodcts_agotados(request):
	if request.user.is_authenticated() and request.user.is_staff:
		consulta = ' total_piezas <= numero_minimo_piezas'
		lista_agotados = Producto.objects.extra(where=[consulta])
		ctx = {'status_agotados':'active',
				'lista_productos':lista_agotados}
		return render_to_response('reportes/lstAgotados.html',ctx,
		context_instance=RequestContext(request))
	else:
		HttpResponseRedirect('/login')

def view_prodcts_caducados(request):
	if request.user.is_authenticated() and request.user.is_staff:
		consulta = " fecha_caducidad >= subdate(curdate(),interval 1 month) and fecha_caducidad<= curdate()"
		lista_caducados = Mercancia.objects.extra(where=[consulta])
		ctx = {'status_caducados':'active',
				'lista_productos':lista_caducados}
		return render_to_response('reportes/lstCaducados.html',ctx,
		context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')

def view_rango_fechas(request):
	if request.user.is_authenticated() and request.user.is_staff:
		if request.method == "POST":
			print "Fue un POST"
			form = getRangoFechaForm(request.POST)
			if form.is_valid():
				fechauno = form.cleaned_data['fechauno']
				fechados = form.cleaned_data['fechados']
				consulta = "fecha_venta >= '%s' and fecha_venta <= '%s'"%(fechauno,fechados)
				p = Productos_vendidos.objects.extra(where=[consulta])
				u = Venta.objects.extra(where=[consulta]).aggregate(Sum('utilidad')).values().__getitem__(0)
				print "est es la utilidad : ",u
				form = getRangoFechaForm()
				titulo = "Este es un reporte especial"
				msg = "Esta es la utilidad generada por las ventas "
				ctx = {'form':form,
					   'productos':p,
					   'status_reporte_rango':'active',
					   'titulo':titulo,
					   'msg':msg,
					   'total_utilidad':u}
				html = render_to_string('reportes/pdf/pdf.html',ctx,context_instance=RequestContext(request))
				return generar_pdf(html)
			else:
				titulo = "Reporte de de un rango de fechas"
				msg = "Revise bien por fabor talves se equiboco al poner algunos datos"
				ctx = {'status_reporte_rango':'active',
						'titulo':titulo,
					   'msg':msg}
				html = render_to_string('reportes/pdf/pdf.html',ctx,context_instance=RequestContext(request))
				return generar_pdf(html)
		else:
			print "Fue un GET"
			form = getRangoFechaForm()
			msg = "Ingrese una fecha y presione siguinete"
			ctx = {'form':form,
					'msg':msg,
				   'status_reporte_rango':'active'}
			return render_to_response('reportes/getDosFechas.html',ctx,context_instance=RequestContext(request))
	else:
		HttpResponseRedirect('/login')


def view_uniq_fecha(request):
	if request.user.is_authenticated() and request.user.is_staff:
		if request.method == "POST":
			print "Fue un POST"
			form = getFechaForm(request.POST)
			if form.is_valid():
				fecha = form.cleaned_data['fecha']
				consulta = "fecha_venta >= '%s' and fecha_venta <= adddate('%s',1)"%(fecha,fecha)
				p = Productos_vendidos.objects.extra(where=[consulta])
				u = Venta.objects.extra(where=[consulta]).aggregate(Sum('utilidad')).values().__getitem__(0)
				print "est es la utilidad : ",u
				form = getFechaForm()
				msg = "Esta es la utilidad generada por las ventas "
				titulo = "Usted ha seleccionado unafecha en especifica"
				ctx = {'form':form,
					   'productos':p,
					   'titulo':titulo,
					   'status_reporte_fecha':'active',
					   'msg':msg,
					   'total_utilidad':u}
				html = render_to_string('reportes/pdf/pdf.html',ctx,context_instance=RequestContext(request))
				return generar_pdf(html)
			else:
				print "Error de formulrio"
				titulo = "Usted ha seleccionado unafecha en especifica"
				msg = "Tal vez llenaste mal la fecha revisa bien por fabor"
				ctx = {'form':form,
						'msg':msg,
						'titulo':titulo,
						'status_reporte_fecha':'active'}
				html = render_to_string('reportes/pdf/pdf.html',ctx,context_instance=RequestContext(request))
				return generar_pdf(html)
		else:
			print "Fue un GET"
			form = getFechaForm()
			msg = "No se ha encontrado ningun producto"
			ctx = {'form':form,
					'msg':msg,
				   'status_reporte_fecha':'active'}
			return render_to_response('reportes/getUnaFecha.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')

def generar_pdf(html):
    # Función para generar el archivo PDF y devolverlo mediante HttpResponse
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))

def pdf(request):
    # vista de ejemplo con un hipotético modelo Libro
    ctx = {'pagesize':'A4'}
    html = render_to_string('reportes/datos_pdf.html', ctx,
    		context_instance=RequestContext(request))
    return generar_pdf(html)
    
def view_mejorProv(request):
	if request.user.is_authenticated() and request.user.is_staff:
		f = getMejorProveedor()
		if request.method == "POST":
			form  = getMejorProveedor(request.POST)
			if form.is_valid():
				cod_prod = form.cleaned_data['codigo']
				lst_provrs = Mejor_proveedor.objects.filter(producto_id=cod_prod)
				if lst_provrs:
					precio_min = lst_provrs.aggregate(Min('precio')).values().__getitem__(0)
					mp = lst_provrs.get(precio=precio_min)
					msg = "Este es el mejor proveedor"
					ctx = {'status_mejor_prov':"active",
							'msg':msg,
							'lista_proveedores':lst_provrs,
							'mp':mp}
					return render_to_response('reportes/lstProveedores.html',ctx,
							context_instance=RequestContext(request))
				else:
					f = getMejorProveedor()
					msg = "Tal vez no se encontra ningun registro"
					ctx = {'status_mejor_prov':"active",
						   'form':f}
					return render_to_response('reportes/mejorProveedor.html',ctx,
							context_instance=RequestContext(request))
			print "Fue un POST"
		else:
			print "Fue un GET"
			ctx = {'status_mejor_prov':"active",
				   'form':f}
			return render_to_response('reportes/mejorProveedor.html',ctx,
					context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login')
		
		
		
def view_report_today(request):
	if request.user.is_authenticated() and request.user.is_staff:
		conusulta = 'fecha_venta >= CURDATE()'
		list_p = Productos_vendidos.objects.extra(where=[conusulta])
		list_v = Venta.objects.extra(where=[conusulta])
		u = list_v.aggregate(u=Sum('utilidad'))
		titulo = "ESte es el reporte del dia de hoy"
		msg = "Esta es la utilidad generada por todas la ventas"
		l =u.values()
		t_u = str(l[0]) 
		
		ctx = {'msg':msg,'titulo':titulo,
			   'status_reporte_diario':'active',
			   'productos':list_p,
			   'total_utilidad':t_u,
			   'pagesize':'A4'}
		html = render_to_string('reportes/reporteDiario.html',ctx,
				context_instance=RequestContext(request))
		return generar_pdf(html)
		
	else:
		return HttpResponseRedirect('/login')
			
def view_report_week(request):
	if request.user.is_authenticated() and request.user.is_staff:
		consulta = 'fecha_venta >= SUBDATE(CURDATE(), INTERVAL 8 DAY)'
		list_p = Productos_vendidos.objects.extra(where=[consulta]) 
		list_v = Venta.objects.extra(where=[consulta])
		u = list_v.aggregate(u=Sum('utilidad'))
		titulo = "ESte es el reporte desde hace una semana hasta el dia de hoy"
		msg = "Estos son las utilidades generadas por las ventas"
		l =u.values()
		t_u = l[0] 
		ctx = {'msg':msg,'titulo':titulo,
		'status_reporte_semanal':'active',
		'productos':list_p,
		'total_utilidad':t_u,
		'pagesize':'A4'}
		
		html = render_to_string('reportes/reporteSemanal.html',ctx,
				context_instance=RequestContext(request))
		return generar_pdf(html)
	else:
		HttpResponseRedirect('/login')
		
		
def view_report_month(request):
	if request.user.is_authenticated() and request.user.is_staff:
		consulta = 'fecha_venta >= SUBDATE(CURDATE(), INTERVAL 30 DAY)'
		list_p = Productos_vendidos.objects.extra(where=[consulta]) 
		list_v = Venta.objects.extra(where=[consulta])
		u = list_v.aggregate(u=Sum('utilidad'))
		titulo = "ESte es el reporte desde hace un mes  hasta hoy "
		msg = "Estos son las utilidades genradas dpor las ventas"
		l =u.values()
		t_u = l[0] 
		ctx = {'msg':msg,'titulo':titulo,
		'status_reporte_mensual':'active',
		'productos':list_p,
		'total_utilidad':t_u,
		'pagesize':'A4'}
		html = render_to_string('reportes/reporteMensual.html',ctx,
				context_instance=RequestContext(request))
		return generar_pdf(html)
	else:
		HttpResponseRedirect('/login')
