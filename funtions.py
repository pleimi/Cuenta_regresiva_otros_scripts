
# las funciones sirven para encapsular código y para reutilizarlo
# hay que LLAMAR la función
# las funciones reciben un PARAMETRO o valor
# puedo construir mis propias funciones 
def hello(name): 
    print("Hellow Juanita " + name)
hello("Durán")
hello("Bonita")

#FUNCIÓN POR DEFECTO
def hello(name="person"): 
    print("Hellow" , name)
hello("Durán")
hello("Bonita")
hello()# si no recibe nada entonces POR DEFECTO muestra el parámetro

# la función add es suma
def add(n1, n2):
    return n1 + n2
print(add(10, 20))# me devuelve 30 
print(add(600, 20))

# esta función se llama LAMBDA
# son funciones ANÓNIMAS
# toman un solo parámetro
add = lambda n1, n2 : n1 + n2
print(add(10, 20))

# terminamos en 2:56



