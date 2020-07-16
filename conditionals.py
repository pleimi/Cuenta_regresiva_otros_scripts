
# programa 1
x = 7
print(x)# retorna 7 
if x > 16:
    print ("x is less than 5")
else:
    print ("x is greater than 15")

# programa 2

color = "blue"
if color == "red":
    print("the color is red")
elif color == "blue":
    print("the color is blue")
else:
    print("the color is other")

# programa 3

name = "juanita"
last_name = "Durán"
age = 7
if name == "juanita" and last_name == "Durán" and age == 7:# and, or y not son operadores lógicos
    print(f"your name is juanita Durán y your age is:", age, "years old") 
else:
    print("your name and age is other")

# programa 4

x = 10
y = 2
print(x + y)
if x < 10:
    if (not(x == y)):
        print("x no is equal to y")
    print("x is greater than y")
else:
    print("x es less than y")

# operadores lógicos

if x > 2 and x <= 10:
    print("x is between 2 and 10")
if x < 5 or x >= 10:
    print("x is less to 5 or greater to 10")  
if (not(x == y)):
    print("x is not equal to y") 









