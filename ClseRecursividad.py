from ctypes.wintypes import PLARGE_INTEGER

while True:
    print("Menu Actividad 8")
    print("Opcion 1")
    print("Opcion 2")
    print("Opcion 3")
    print("Opcion 4")
    print("Opcion 5")
    print("Salir")
    try:
        opcion=int(input("Ingrese una Opcion: "))
    except ValueError:
        print("Ingrese un entero")
    match opcion:
        case 1:
            print("Ejercicio 1")
            def factorial(n):
                if n == 0:
                    return 1
                else:
                    print(n)
                    return n * factorial(n - 1)
            n = int(input("Ingrese un numero entero positivo: "))
            print(factorial(n))
        case 2:
            print("Ejercicio 2")
            def suma(n):
                if n==10:
                    return 1
                else:
                    print(n)
                    return n+suma(n+1)
            sumanumeros=int(input("Ingrese hasta que numero quiere que llegue la suma"))
            print("La suma de los primeros numeros es")
            print(suma(sumanumeros))
        case 3:
            print("Ejercicio 3")

        case 4:
            print("Ejercicio 4")
        case 5:
            print("Ejercicio 5")
            def potencia(base, exponente):
                if exponente == 0:
                    return 1
                else:
                    return base * potencia((base, exponente - 1))
            b = int(input("Ingrese la base"))
            e = int(input("Ingrese el exponente"))
            print(potencia(b, e))
        case 6:
            print("Saliendo")
            break
        case _:
            print("Opcion Invalida")








