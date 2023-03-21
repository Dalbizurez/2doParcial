try:
    n1 = int(input("Ingrese el primer valor: "))
    n2 = int(input("Ingrese el segundo valor: "))
except:
    print("Solo se aceptan numeros")
else:
    if n1>n2:
        print(f"{n1} es el mayor")
    elif n1<n2:
        print(f"{n2} es el mayor")
    else:
        print(f"{n1} y {n2} son iguales")