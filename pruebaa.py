print("tienes 2 intentos para colocar los datos correctos")
contador = 1
while contador <= 2:
    contraseña = input("ingrese la contraseña: ")
    if contraseña == "halo tuyo":
        print("felizidades ingresaste los datos correctos")
        contador = 3
    else:
        print("la contraseña es incorrecta")
        if contador == 2:
            print("comunicate con el desarrollador has fallado los 2 intentos")
        contador = contador +1