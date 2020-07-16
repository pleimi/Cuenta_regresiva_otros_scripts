# Muesta la fecha de hoy
import time 
from datetime import date
today = date.today()
print(today)

# Muesta la fecha de hoy
import datetime
print(datetime.date.today())#el método es date y el parámetro es today
# Muesta la fecha de hoy
from  datetime import date
print(date.today())

#converts minutes to hours
import datetime
print(datetime.timedelta(minutes=100))#convert minutes to hours
print(datetime.timedelta(days=1))
print(datetime.timedelta(weeks=1))#shows 7 days
print(datetime.timedelta(hours=100))#shows 4 days 4:00:00 hours
print(datetime.timedelta(seconds=100))#converts seconds to minutes

# importamos nuestro módulo con sus dos funciones 
import fmath 
fmath.add(3,2)#devuelve 5
fmath.substract(3,2)#devuelve 1

# Importo un módulo propio
from fmath import add, substract
add(5,3)# shows 
substract(5,3)

