
# Variables instanciadas
num1 = 1
num2 = 2
resultado = 0

# operaciones de suma, resta, multiplicacion y division
print("Inciso 2")
# Suma
resultado = num1 + num2
print(resultado)

# Resta
resultado = num1 - num2
print(resultado)

# Multiplicacion
resultado = num1*num2
print(resultado)

# Division
resultado = num1/num2
print(resultado)

# Potencia
resultado = num1 ** num2
print(resultado)

print("Inciso 3")
# Imprime en consola el string, realiza la operacion de suma entre num1 & num2 e imprime el resultado de dicha operacion
print("El resultado de la suma entre", num1, "y", num2, "es:", num1 + num2)

print("Inciso 4")
# Matriz
A = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20],
     [21, 22, 23, 24, 25]]

print("Inciso 5")
# imprime toda la matriz
print("A= "+str(A[0]))  # primera fila
print("   "+str(A[1]))  # segunda fila
print("   "+str(A[2]))  # tercera fila
print("   "+str(A[3]))  # cuarta fila
print("   "+str(A[4]))  # quinta fila

print("Inciso 6")
# Cambio de valores en la matriz
A[0][0] = 0  # primera fila primer valor
A[1][1] = 0  # segunda fila segundo valor
A[2][2] = 0  # tercera fila tercer valor
A[3][3] = 0  # cuarta fila cuarto valor
A[4][4] = 0  # quinta fila quinto valor

# imprime toda la matriz
print("A= "+str(A[0]))  # primera fila
print("   "+str(A[1]))  # segunda fila
print("   "+str(A[2]))  # tercera fila
print("   "+str(A[3]))  # cuarta fila
print("   "+str(A[4]))  # quinta fila



