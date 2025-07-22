from ctypes.wintypes import PLARGE_INTEGER

while True:
    print("Menu Actividad 8")
    print("1. Factorial")
    print("2. Suma de los primeros n numeros")
    print("3. Fibonacci")
    print("4. letras")
    print("5. Base Exponente")
    print("6. Salir")
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
            numero = int(input("Ingrese un numero entero positivo: "))
            print(factorial(numero))
        case 2:
            print("Ejercicio 2")
            def suma(n):
                if n==0:
                    return 0
                else:
                    print(n)
                    return n+suma(n-1)
            numero=int(input("Ingrese hasta que numero queiere que se sumen los numeros: "))
            print(suma(numero))
        case 3:
            print("Ejercicio 3")
            def fibonacci(n):
                if n<=1 :
                    return n
                else:
                    print(n)
                    return fibonacci(n-1)+fibonacci(n-2)
            numero=int(input("Ingrese hasta que n numero quiere la secuencia de fibonacci"))
            print(fibonacci(numero))
        case 4:
            print("Ejercicio 4")
            def letras(palabra):
                if palabra=="":
                    return 1+letras(palabra)
                else:
                    return letras(palabra)
            frase=input("Ingrese la frase o palabra.").lower()
            cletra=input("Ingrese la letra que quiere contar").lower()
            total=letras(frase)
            print(f"La cantidad de letras es {total}")

        case 5:
            print("Ejercicio 5")
            def potencia(base, exponente):
                if exponente == 0:
                    return 1
                else:
                    return base * potencia(base, exponente - 1)
            b = int(input("Ingrese la base"))
            e = int(input("Ingrese el exponente"))
            print(potencia(b, e))
        case 6:
            print("Saliendo")
            break
        case _:
            print("Opcion Invalida")