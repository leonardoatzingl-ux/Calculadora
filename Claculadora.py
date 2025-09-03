#Calculadora
num1=float("Ingresar el primer numero")
Num2=float("Ingresar el segundo numero")

suma=num1+Num2
resta=num1-Num2
multiplicación=num1*Num2
división=num1/Num2


print("El resultado de la suma es: ",suma)
print("El resultado de la resta es: ",resta)
print("El resultado de la multiplicación es: ",multiplicación)
print("El resultado de la divición es: ",división)

#Mostrar menu de operaciones
print("\nElige la operación que deseas realizar:")
print("1. suma")
print("2. resta")
print("e. multiplicación")
print("4 divsión") 

opcion = input("Ingresa el numero de la opción:")

#Evaluar la opción seleccionada
if opcion == "1":
    resultado = num1 + Num2
    print("El resultado de la suma es:", resultado)
elif opcion == "2":
    resultado = num1 - Num2
    print("El resultado de la resta es:", resultado)
elif opcion == "3":
    resultado = num1 * Num2
    print("El resultado de la mutiplicaión es:", resultado)
elif opcion == "4":
    if Num2 !=0: #Evitar división entre cero
        resultado = num1 / Num2
        print("El resultado de la división es:", resultado)
    else:
        print("Error: no se puede dividir entre cero")
else:
    print("Opción no válida") 