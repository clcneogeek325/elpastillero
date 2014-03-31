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
from apps.reportes.forms import getFechaForm,getRangoFechaForm
from apps.productos.models import Producto
from datetime import datetime
from apps.mercancia.models import Mercancia
from django.shortcuts import render_to_response



def view_prodcts_agotados(request):
	consulta = ' total_piezas <= numero_minimo_piezas'
	lista_agotados = Producto.objects.extra(where=[consulta])
	ctx = {'status_agotados':'active',
			'lista_productos':lista_agotados}
	return render_to_response('reportes/lstAgotados.html',ctx,
	context_instance=RequestContext(request))

def view_prodcts_caducados(request):
	consulta = " fecha_caducidad >= subdate(curdate(),interval 1 month) and fecha_caducidad<= curdate()"
	lista_caducados = Mercancia.objects.extra(where=[consulta])
	ctx = {'status_caducados':'active',
			'lista_productos':lista_caducados}
	return render_to_response('reportes/lstCaducados.html',ctx,
	context_instance=RequestContext(request))

def view_rango_fechas(request):
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
			msg = "Esta es la utilidad generada por las ventas "
			ctx = {'form':form,
				   'productos':p,
				   'status_reporte_fecha':'active',
				   'msg':msg,
				   'total_utilidad':u}
			return render_to_response('reportes/getDosFechas.html',ctx,context_instance=RequestContext(request))
	else:
		print "Fue un GET"
		form = getRangoFechaForm()
		msg = "Ingrese una fecha y presione siguinete"
		ctx = {'form':form,
			   'status_reporte_rango':'active'}
		return render_to_response('reportes/getDosFechas.html',ctx,context_instance=RequestContext(request))



def view_uniq_fecha(request):
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
			ctx = {'form':form,
				   'productos':p,
				   'status_reporte_fecha':'active',
				   'msg':msg,
				   'total_utilidad':u}
			return render_to_response('reportes/getUnaFecha.html',ctx,context_instance=RequestContext(request))
	else:
		print "Fue un GET"
		form = getFechaForm()
		msg = "No se ha encontrado ningun producto"
		ctx = {'form':form,
				'msg':msg,
			   'status_reporte_fecha':'active'}
		return render_to_response('reportes/getUnaFecha.html',ctx,context_instance=RequestContext(request))

def generar_pdf(html):
    # Función para generar el archivo PDF y devolverlo mediante HttpResponse
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))

def view_ejemplo_pdf(request):
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
		t_u = l[0] 
		ctx = {'msg':msg,'titulo':titulo,
			   'status_reporte_diario':'active',
			   'productos':list_p,
			   'total_utilidad':t_u}
		return render_to_response('reportes/reporteDiario.html',ctx,
				context_instance=RequestContext(request))
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
		'total_utilidad':t_u}
		return render_to_response('reportes/reporteSemanal.html',ctx,
				context_instance=RequestContext(request))
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
		'total_utilidad':t_u}
		return render_to_response('reportes/reporteMensual.html',ctx,
				context_instance=RequestContext(request))
	else:
		HttpResponseRedirect('/login')
