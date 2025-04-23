#Fija un número secreto (por ejemplo, 7). 
# Pide al usuario que lo adivine. 
# Di si su número es mayor, menor o igual al número secreto.

number = 0
while number !=7:
   number= int(input("ingresa un numero: "))

   if number < 7:
    print("tu numero es menor")
   elif number > 7:
    print("tu numero es mayor")
   else:
    print("tu numero es correcto")

