myStr = "pleimi es mi 23 8 9nicknaesme"

print("My name is " + myStr)
print(f"My name is {myStr}")# la f significa que hay una variable en el texto
print("My name is {0}".format(myStr))
print (dir(myStr)) # con dir vemos los métodos 
print(myStr.upper()) # upper me cambia la palabra a mayuscula print(myStr.title()) # sirve para volver mi string en titulo
print(myStr.lower()) # todo en minuscula print(myStr.capitalize())# coloca la primera letra en minúscula
print(myStr.swapcase()) # cambia las mayusculas a minusculas
# print(myStr.strip()) # me muestra el string original
# print(myStr.startswith('a')) # me devuelve un boolean False
# print(myStr.endswith("e")) # termina mi string en la letra e? True print(myStr.split(' ')) # separe a partir de un espacio y da una list[]
# print(myStr.split("i")) #separa a partir de la letra i
# print(myStr.split("2")) # separa a partir del 2
# print(myStr.count("es"))# cuenta las veces en las que está "es"
# print(myStr.replace("23","22"))# reemplaza el 23 por el 22  
# print(len(myStr))# me da la longitud de la todo el string 29 caracteres
# print(myStr.find("8")) # me da el indice o posición del caracter "8" ej.16
# print(myStr.index("8"))# como el anterior me da el indice ej. 16
# print(myStr[0])# que valor está en la posición 0? la p
# print(myStr[1])# que valor está en la posición 0? la l
# print(myStr[2])# que valor está en la posición 0? la e
# print(myStr[3])# que valor está en la posición 0? la i
# print(myStr[-2])# quien es el penúltimo caracter? la m
# print(myStr.isnumeric())# me devuelve un boolean  
# print(myStr.isalpha())# me devuelve un boolean ej. False

