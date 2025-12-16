#formula para celsuis a fahrenheit es 1.8*(grado celsius)+32
#formula para fahrenheit a celsius f-32/1.8 

usar_convertidor_cf = input("Quieres usar el convertidor de temperatura de C-F? ")
if usar_convertidor_cf == "si":
    print("Empecemos")
    pide_numero = (input("Dame un numero: "))
    while pide_numero.isdigit() is False:
         pide_numero = (input("Me has dado un valor no convertible, dame un numero porfis: "))
    numero = (int(pide_numero))
    formula = 1.8 * numero + 32
    resultado = int(formula)
    print(f"Estamos a {resultado} grados fahrenheit")
elif usar_convertidor_cf == "no":
        segunda_convertidor_fc = input("Quieres usar el convertidor de temperatura de F-C? ")
        if segunda_convertidor_fc == "si":
            print("Empecemos")
            pide_numero2 = (input("Dame un numero: "))
            while pide_numero2.isdigit() is False:
                pide_numero2 = (input("Me has dado un valor no convertible, dame un numero porfis: "))
            numero2 = (int(pide_numero2))
            formula2 = (numero2 - 32) / 1.8
            resultado2 = int(formula2)
            print(f"Estamos a {resultado2} grados celsius")
else:
    print("Ok, adios")
print("Gracisa por usar mi convertidor c:")