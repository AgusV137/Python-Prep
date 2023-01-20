## Flujos de Control

#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
a = 1
print("#" + str(a) )

from random import randint,uniform,random, randrange
num = randint(-2, 5)
if num < 0:
    print("El número es menor a 0")
elif num > 0:
    print("El número es mayor a 0") 
else:
    print("El numero es igual a 0") 
    
print()   
#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

print("#"+ str(a + 1) + ")")
var1 = "r#"
var2 = 3
if type(var1) == type(var2):
    print("Son el mismo tipo de dato")
else:
    print("No son el mismo tipo de dato")

print()
#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
print("#"+ str(a + 2) + ")")
num = 1
for num in range(1,21):
    if num % 2 == 0:
        print("El numero " + str(num) + " es par")
    else:
        print("El numero " + str(num) + " es impar")
print()
    
        
#4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
print("#"+ str(a + 3) + ")")

num2 = 0
for num2 in range(6):
    print(str(num2) +  " ^ 3 = " + str(num2 ** 3))

print()
#5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
print("#"+ str(a + 4) + ")")

num3 = randint(4, 8)
i = 0
for i in range(num3):
    i += 1
    print("el numero es " + str(num3) + " y el ciclo se repite por " + str(i) + " vez.") 

print()
#6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
print("#"+ str(a + 5) + ")")



print()
#7) Crear un ciclo for dentro de un ciclo while
print("#"+ str(a + 6) + ")")

print()
#8) Crear un ciclo while dentro de un ciclo for
print("#"+ str(a + 7) + ")")

print()
#9) Imprimir los números primos existentes entre 0 y 30
print("#"+ str(a + 8) + ")")

print()
#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
print("#"+ str(a + 9) + ")")

print()
#11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
print("#"+ str(a + 10) + ")")

print()
#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
print("#"+ str(a + 11) + ")")

print()
#13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
print("#"+ str(a + 12) + ")")

print()
#14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
print("#"+ str(a + 13) + ")")

print()
#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
print("#"+ str(a + 14) + ")")