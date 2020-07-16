# los sets  tienen un indice para poder acceder a el 
colors = {'Red', 'Green', 'Blue'}
print(type(colors))
print('Red' in colors)# esta el Red en la varuable colors? me devuelve True
colors.add('violet')# agrega el dato aleatoriamente
colors.add('pink')
colors.remove('Blue')#remueve el elemento Blue
print(colors)
colors.clear()
print(colors)
del (colors)# borra el archivo colors
