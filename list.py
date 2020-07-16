#demo_list = [1, "hello", 2.5, True, [1, 2, 3]]# aqui hay una lista dentro de otras
#print(dir(demo_list))
#print(demo_list)

#colors = (["red", "green","blue"])# me imprime una lista []
# print(colors)

# number_list= list((1, 2, 3, 4)) # esto es una tuple, datos inmutables
# print(number_list)

# print(type(number_list))# me muestra el tipo de la variable

estadistica = list(range(1, 109))# me da la cantidad menos el último
print(estadistica)
numero_ganador = input("el numero ganador es: ")
print(numero_ganador)
estadistica.insert(0, int(numero_ganador))#inserte en el indice 0 "numero_ganador"
estadistica.pop()# me quita el último elemento
print(estadistica)
numero_ganador = input("el numero ganador es: ")
print(numero_ganador)
estadistica.insert(0, int(numero_ganador))#inserte en el indice 0 "numero_ganador"
estadistica.pop()# me quita el último elemento
print(estadistica)
numero_ganador = input("el numero ganador es: ")
print(numero_ganador)
estadistica.insert(0, int(numero_ganador))#inserte en el indice 0 "numero_ganador"
estadistica.pop()# me quita el último elemento
print(estadistica)

#estadistica[0] = 108 # cambie del indice 0 el elemento por 108


# print(len(ruleta))

#print('red' in colors) # está red in la variable colors? True

#colors[1] = "yelow" # cambie el indice 1 a yellow
#print(colors)

