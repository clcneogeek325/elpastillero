#!/usr/bin/env python
#-*- coding:utf-8 -*-

import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from django.template import RequestContext
from django.template.loader import render_to_string
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render_to_response


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
	return render_to_response('reportes/mejorProveedor.html',
			context_instance=RequestContext(request))
