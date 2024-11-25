Lado1 = int(input("Ingrese el valor del lado A: "))
Lado2 = int(input("Ingrese el valor del lado B: "))
Lado3 = int(input("Ingrese el valor del lado C: 5"))
if Lado1 + Lado2 > Lado3:
    Lado2 + Lado3 
else:
    print("Los valores ingresados no permiten formar un triangulo")
    if Lado2 + Lado3 > Lado1:
        Lado1 + Lado3 
    else:
        print("Los valores ingresados no permiten formar un triangulo")
        if Lado1 + Lado3 > Lado2:
            print("las medidas ingresadas son correctas para formar un triangulo")
        else: 
            print("Los valores ingresados no permiten formar un triangulo")
            if Lado1 == Lado2 and Lado2 == Lado3:
                print("Su triangulo es equilatero ")
            elif Lado1 != Lado2 and Lado2 != Lado3:
                print("Su triangulo es escaleno")
