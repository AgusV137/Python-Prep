# %%


# %% [markdown]
# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
# 

# %%
variable_1 = 3
print(variable_1)

# %% [markdown]
# 2) Imprimir el tipo de dato de la constante 8.5
# 

# %%
print(type(8.5))

# %% [markdown]
# 3) Imprimir el tipo de dato de la variable creada en el punto 1
# 

# %%
print(type(variable_1))

# %% [markdown]
# 
# 4) Crear una variable que contenga tu nombre

# %%
nombre = "Agustín"
print(nombre)

# %% [markdown]
# 5) Crear una variable que contenga un número complejo
# 

# %%
variable_2 = 2 + 1j


# %% [markdown]
# 6) Mostrar el tipo de dato de la variable crada en el punto 5
# 

# %%
type(variable_2)

# %% [markdown]
# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
# 

# %%
variable_3 = 3.1416

# %% [markdown]
# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
# 

# %%
variable_4 = "True"
variable_5 = True
variable_4 == variable_5

# %% [markdown]
# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
# 

# %%
print (type (variable_4)) 
print (type (variable_5))

# %% [markdown]
# 10) Asignar a una variable, la suma de un número entero y otro decimal
# 

# %%
variable_6 = 187 + 1.24
print (variable_6)
type(variable_6)

# %% [markdown]
# 11) Realizar una operación de suma de números complejos
# 

# %%
variable_2 + 3.14j

# %% [markdown]
# 12) Realizar una operación de suma de un número real y otro complejo
# 

# %%
variable_3 + variable_2

# %% [markdown]
# 13) Realizar una operación de multiplicación
# 

# %%
3 * 4.5
    

# %% [markdown]
# 14) Mostrar el resultado de elevar 2 a la octava potencia
# 

# %%
2 ** 8

# %% [markdown]
# 
# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
# 
# 

# %%
variable_8 = 27 / 4
print(variable_8)

# %% [markdown]
# 
# 16) De la división anterior solamente mostrar la parte entera
# 

# %%
variable_8 = 27 // 4
print(variable_8)

# %% [markdown]
# 
# 17) De la división de 27 entre 4 mostrar solamente el resto
# 

# %%
variable_9 = 27 % 4
print(variable_9)

# %% [markdown]
# 
# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
# 

# %%
(variable_8) * 4 + variable_9

# %% [markdown]
# 
# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
# 

var1 = "hola"
var2 = " wey"
var1 + var2

# %% [markdown]
# 
# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
# 
"2" == 2

# %% [markdown]
# 
# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
# 
# 
a = int("2")
b = 2

a == b

# %% [markdown]
# 
# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# 
a = float('3.8')
# %% [markdown]
# 
# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
# 
a = 3
a -= 2
print(a)

# %% [markdown]
# 
# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
# 

3 << 3

# %% [markdown]
# 
# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
b= "2" + '2'
print(b)


# %% [markdown]
# 
# 26) Realizar una operación válida entre valores de tipo entero y string

a = "hola " * 3
print(a) 