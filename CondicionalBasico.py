"""a = 100
b = 99.9

if b<a:
    print("b es mayor que a")

a = input("Ingrese un número: ")
b = input("Ingrese otro número: ")

if a>b:
    print(str(a) + " es mayor que "+str(b))
elif b>a:
    print(str(b) + " es mayor que "+str(a))
else:
    print("Los números son iguales")

genero = input("Ingrese su género")

if genero.lower() == 'f':
    print("Bienvenida!")
elif genero.lower() == 'm':
    print("Bienvenido!")
else:
    print("Bienvenidex!")

"""
a = 100
b = 99.9

print("b es mayor que a") if b>a else print("a es mayor que b")

a = 330
b = 330
print("b es mayor que a") if b>a else print("son iguales") if b==a else print("a es mayor a b")


a = 200
b = 33
c = 500
if a > b and c > a:
    print("Ambas condiciones son verdaderas.")

if a > b or a > c:
    print("Al menos una de las dos condiciones es verdadera")

x = 20

if x > 10:
    print("Mensaje", end=" ")
    if x > 20:
        print("y también mayor que 20!")
    else:
        print("pero no mayor que 20.")