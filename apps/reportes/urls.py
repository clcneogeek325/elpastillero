from django.conf.urls import patterns, include, url


urlpatterns = patterns('apps.reportes.views',
    # Examples:
    url(r'^pdf/$', 'view_hello_pdf', name='vista_pdf'),
)
