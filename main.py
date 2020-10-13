import random

num = random.randint(1,100)
print("Adivina el numero del 1 al 100 en 10 intentos")

elegido = 0
intentos = 10

while elegido != num and intentos > 0:
    elegido = int(input())
    if elegido > num:
        print("El numero es menor que {}".format(elegido))
    elif elegido < num:
        print("El numero es mayor que {}".format(elegido))

    intentos -= 1
    print("Te quedan {} intentos".format(intentos))
        

if elegido == num:
    print("Ganaste! el numero era el {}".format(num))
else:
    print("Te quedaste sin intentos! el numero era el {}".format(num))
