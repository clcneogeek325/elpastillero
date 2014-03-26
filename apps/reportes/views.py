#!/usr/bin/env python
#-*- coding:utf-8 -*-
from django.db import connection
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render_to_response
from apps.ventas.models import Venta
from django.db.models import Sum
from apps.ventas.models import Productos_vendidos


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

	ctx = {'status_mejor_prov':"active"}
	return render_to_response('reportes/mejorProveedor.html',ctx,
			context_instance=RequestContext(request))
			
def view_report_today(request):
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
			
def view_report_week(request):
	consulta = 'fecha_venta BETWEEN SUBDATE(CURDATE(), INTERVAL 8 DAY) AND CURDATE()'
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
			
def view_report_month(request):
	consulta = 'fecha_venta BETWEEN SUBDATE(CURDATE(), INTERVAL 8 DAY) AND CURDATE()'
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
