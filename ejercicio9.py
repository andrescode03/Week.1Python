#Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).

year = int(input("ingresa un año: "))
if(year % 4 ==0 and year % 100 !=0)or(year % 400 == 0):
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")


