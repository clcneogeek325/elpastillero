elpastillero
============

Trabajando ya con django


============
Acciones Para los modelos


class="vDateField" # ene l input

class="datetime" #en un <p>
================

import time
import datetime

print "Time in seconds since the epoch: %s" %time.time()
print "Current date and time: " , datetime.datetime.now()
print "Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M")

dia = datetime.now().day
mes = datetime.now().month
año = datetime.now().year

print v[0].fecha_venta.date() #mostrar la fecha

print "Current year: ", datetime.date.today().strftime("%Y")
print "Month of year: ", datetime.date.today().strftime("%B")
print "Week number of the year: ", datetime.date.today().strftime("%W")
print "Weekday of the week: ", datetime.date.today().strftime("%w")
print "Day of year: ", datetime.date.today().strftime("%j")
print "Day of the month : ", datetime.date.today().strftime("%d")
print "Day of week: ", datetime.date.today().strftime("%A")




from django.db.models import Sum

total_utilidad = Venta.objects.all().aggregate(total_utilidad=Sum('utilidad'))

total = Task.objects.filter(your-filter-here).aggregate(total=Sum('progress', field="progress*estimated_days"))['total']
