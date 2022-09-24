print("Hola Mundo!!!")           # Imprime una cadena de caracteres (string)

frase ="Hola Mundo!!!"           # Asigno a la variable frase los caracteres Hola Mundo!!!
print(frase)                     # Imprime la variable frase

# Variables númericas

x = 5.0
y = 3

type(x)                          # Indica el tipo de variable
print("X es igual a: ", x)
print("Y es igual a: ", y)
print( x, "es una variable tipo: ", type(x))
print( y, "es una variable tipo: ", type(y))
print( frase, "es una variable tipo: ", type(frase))

numero = "355"
value = int(numero)
print( numero, "es una variable tipo: ", type(numero))
print( value, "es una variable tipo: ", type(value))

print("Suma: ", x + y)
print("Resta: ", x - y)
print("Multiplicación: ", x * y)
print("División: ", x / y)
print("Potencia: ", x ** y)
print("Modulo: ", x % y)

# Loops (iteraciones)

for num in range(10, 0, -1):          # Se mueve sobre una lista de números
    if num % 3 == 0:                  # ¿Es divisible por 3? - condicional
        print(num)
        break                         # Termina el ciclo de iteración
    else:
        print(num, "No es divisible por 3")
        continue

# Operaciones con strings

frase = "Hola Mundo"
frase2 = "Big Data"

print(frase + frase2)                 # Concatena dos variables str

n_repeticiones = 10
print(n_repeticiones*frase)