from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.reportes.views',
    # Examples:
    url(r'^pdf/$', 'view_ejemplo_pdf', name='vista_pdf'),
    url(r'^getCodMejProv/$', 'view_mejorProv', name='vista_mejor_proveedor'),
    url(r'^reporteDiario/$', 'view_report_today', name='vista_reporte_diario'),
    url(r'^reporteSemanal/$', 'view_report_week', name='vista_reporte_semanal'),
    url(r'^reporteMensual/$', 'view_report_month', name='vista_reporte_mensual'),
    url(r'^unaFecha/$', 'view_uniq_fecha', name='vista_reporte_un_dia'),
    url(r'^rangoFechas/$', 'view_rango_fechas', name='vista_rango_dos_fechas'),
    url(r'^lstCaducados/$', 'view_prodcts_caducados', name='vista_productos_caducados'),
    url(r'^lstAgotados/$', 'view_prodcts_agotados', name='vista_productos_agotados'),
    
)
