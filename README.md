elpastillero
============

Trabajando ya con django


============
Acciones Para los modelos

__class__
__delattr__
__dict__
__doc__
__format__
__getattribute__
__hash__
__init__
__module__
__new__
__reduce__
__reduce_ex__
__repr__
__setattr__
__sizeof__
__str__
__subclasshook__
__weakref__
_copy_to_model
_db
_inherited
_insert
_set_creation_counter
_update
aggregate
all
annotate
bulk_create
complex_filter
contribute_to_class
count
create
creation_counter
dates
db
db_manager
defer
distinct
exclude
exists
extra
filter
get
get_empty_query_set
get_or_create
get_query_set
in_bulk
iterator
latest
model
none
only
order_by
prefetch_related
raw
reverse
select_for_update
select_related
update
using
values
values_list
================================== USOS DE LA LIBRERIA DATETIME

import time
import datetime

print "Time in seconds since the epoch: %s" %time.time()
print "Current date and time: " , datetime.datetime.now()
print "Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M")


print "Current year: ", datetime.date.today().strftime("%Y")
print "Month of year: ", datetime.date.today().strftime("%B")
print "Week number of the year: ", datetime.date.today().strftime("%W")
print "Weekday of the week: ", datetime.date.today().strftime("%w")
print "Day of year: ", datetime.date.today().strftime("%j")
print "Day of the month : ", datetime.date.today().strftime("%d")
print "Day of week: ", datetime.date.today().strftime("%A")
