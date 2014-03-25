from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.reportes.views',
    # Examples:
    url(r'^pdf/$', 'view_ejemplo_pdf', name='vista_pdf'),
    url(r'^mejorProveedor/$', 'view_mejorProv', name='vista_mejor_proveedor'),
    url(r'^reporteDiario/$', 'view_report_today', name='vista_reporte_diario'),
    url(r'^reporteSemanal/$', 'view_report_week', name='vista_reporte_semanal'),
    url(r'^reporteMensual/$', 'view_report_month', name='vista_reporte_mensual'),
    
)
