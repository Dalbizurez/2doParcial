try:
    n1 = int(input("Ingrese el numero a evaluar: "))
except:
    print("Por favor ingrese un numero entero")
else:
    if n1%2 == 0:
        print(f"{n1} es par")
    else:
        print(f"{n1} es impar")