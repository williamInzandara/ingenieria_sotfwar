class determinar_numero_mayor:
    numero1 = int(input("Ingrese el primer dígito: "))
    numero2 = int(input("Ingrese el segundo dígito: "))

    # Determinar el mayor de los dos números
    if numero1 > numero2:
        print(f"El mayor es: {numero1}")
    elif numero2 > numero1:
        print(f"El mayor es: {numero2}")
    else:
        print("Ambos dígitos son iguales")