#1) Dar informacion preceisa al usuario, cambiar primer, segunto, tercer numero por "la variable cuadrática", "variable lineal", "término independiente"
a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
c = int(input("Introduce el tercer número: "))
#2) Validar que sean numeros enteros (Creo que con WHILE)


#3) Validar que lo que esta DEBAJO de la RAIZ sea mayor a "0",  (b ** 2 - 4 * (a * c))
# Caso contrario indicar al usuario que no tiene solucion en Reales (En un complejo) 
# Usar IF

#4) Validar si la RAIZ = 0 

#5) Veo 2 blqoes parecidos, para calcualr X e Y, no es claro

x = b ** 2 - 4 * (a * c)
x = x ** 0.5
x = - b + x
x = x / (2 * a)
 
y = b ** 2 - 4 * (a * c)
y = y ** 0.5
y = - b - y
y = y / (2 * a)
 
#6) Usar nombre de variables represetativas y claras
# X e Y deben ser X1 y X2

#7) Evitar acumular resultados en la misma variable

print(x)
print(y)
#8) Dar formato el resultado con al menos 2 decimales (En el caso que el resultado sea real)