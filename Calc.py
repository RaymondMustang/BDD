print("Ingrese los datos siguentes")
num1=int(input("Ingrese el valor 1: "))
num2=int(input("Ingrese el valor 2: "))

while True:
    print("--Menu--")
    print("1. Sumar")
    print("2.")
    print("3.")
    print("4. Multiplicar")
    print("5.")
    print("6.")
    print("7. Salir")

    opcion=int(input("Seleccion una opcion: "))

    
    
    if opcion==1:
        print("Suma")
        
        res=num1+num2
        print("el resultado de la suma entre",num1," + ",num2," fue: ",res)

    elif opcion==2:
        print("Opcion 2")
        #Codigo aqui

    elif opcion==3:
        print("Opcion 3")
        #Codigo aqui

    elif opcion==4:
        print("Multiplicacion")     
        res=num1*num2
        print("el resultado de la multiplicacion entre",num1," + ",num2," fue: ",res)

    elif opcion==5:
        print("Opcion 5")
        #Codigo aqui

    elif opcion==6:
        print("Opcion 6")
        #Codigo aqui

    elif opcion==7:
        print("Gracias por su visita")
        break

    else:
        print("Por favor seleccione una opcion valida")  