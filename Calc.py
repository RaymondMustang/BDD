print("Ingrese los datos siguentes")
num1=int(input("Ingrese el valor 1: "))
num2=int(input("Ingrese el valor 2: "))

while True:
    print("--Menu--")
    print("1. Sumar")
    print("2. Restar :D")
    print("3. Dividir")
    print("4. Multiplicar")
    print("5. Numero mayor menor o igual :D")
    print("6. Exponencial")
    print("7. Salir")

    opcion=int(input("Seleccion una opcion: "))

    
    
    if opcion==1:
        print("Suma")
        
        res=num1+num2
        print("el resultado de la suma entre",num1," + ",num2," fue: ",res)

    elif opcion==2:
        print("Opcion 2")
        res=num1-num2

        print("la resta de sus numeros es: ",res)

    elif opcion==3:
        if num2==0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado=num1/num2
            print("El resultado de la división es:", resultado)

    elif opcion==4:
        print("Multiplicacion")     
        res=num1*num2
        print("el resultado de la multiplicacion entre",num1," + ",num2," fue: ",res)

    elif opcion==5:
        print("Opcion 5")
        if num1>num2:
            print(num1," es el numero mayor")
            print(num2,"es el numero menor")
        if num1<num2:
            print(num2," es el numero mayor")
            print(num1,"es el numero menor")
        if num1==num2:
            print(num1,num2,"son numeros iguales")
       

    elif opcion==6:
        if num1<0 and num2!=int(num2):
            print("Error: No se puede calcular la exponenciación con un número negativo y un exponente no entero.")
        else:
            resultado=num1**num2
            print("El resultado de la exponenciación es:", resultado)

    elif opcion==7:
        print("Gracias por su visita")
        break

    else:
        print("Por favor seleccione una opcion valida")  