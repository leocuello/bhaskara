
#Validar que sea entero
a = int(input("Introduce la variable cuadrática:\n"))
b = int(input("Introduce la variable lineal:\n"))
c = int(input("Introduce wl término independiente:\n"))


raiz = (b ** 2) - (4 * a * c)
if raiz < 0:
    print("No tiene solucion en R, es un complejo")
elif raiz == 0:
    x1 = (-b) / (2*a)
    print("X1: ", x1) 
else:
    x1 = (-b + (raiz ** 0.5)) / (2*a)
    x2 = (-b - (raiz ** 0.5)) / (2*a)

    print("X1: ", x1)
    print("X2: ", x2)