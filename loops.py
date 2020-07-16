foods = ['apples', 'bread', 'cheese', 'milk', 'bananas', 'grapes']
print(foods)

for food in foods:
    print(food)

for food in foods:
     if food == "cheese": # Cuando encuentre "cheese" imprima "buy this"
         print("buy this")
     print(food)

for food in foods:
     if food == "cheese": # Cuando encuentre "cheese" rompa la ejecución
       break
     print(food)

for food in foods:
    if food == "cheese": # Cuando encuentre "cheese" continue, y NO muestra "cheese"
       continue
    print(food)

letters = "HELLOW"
for letter in letters:
    print(letter)

#for number in range (1, 109):# muestra los números de 1 a 108
#    print(number)

# muestra los números del 5 hasta el 10
count = 5

while count <= 10:
    print(count)
    count = count + 1 # se coloca para que no sea infinito
