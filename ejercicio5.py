#Pide al usuario el total de una cuenta. 
# Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). 
# Calcula y muestra el valor de la propina.

totalCost = int(input("ingrese el costo total de la cuenta="))
tip = int(input("ingrese el porcentaje de propina, entre 10, 15 y 20="))
tip2 = totalCost * (tip / 100)

costWithTip = totalCost + tip2
print (f"El costo total con su propina es. {costWithTip}")
