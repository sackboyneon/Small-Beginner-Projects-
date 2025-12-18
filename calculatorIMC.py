#formula IMC = peso (kg) / (estatura (m))^2.
print("Bienvenido a la calculadora de IMC")
pregunta_usuario = input("Quieres usarla? ")

if pregunta_usuario == "no":
    print("Ok, hasta luego!")
    exit()

while pregunta_usuario == "si":
        try:
            peso_kg = float(input("Por favor ingresa tu peso en kilogramos: "))
            estatura_m = float(input("Por favor ingresa tu estatura en metros: "))
            resultado = peso_kg / (estatura_m ** 2)
            print(f"Tu indice de masa corporal es de {resultado:.2f}")
            if resultado < 18.5:
                print("Estas por debajo del peso normal")
            elif resultado >= 18.5 and resultado < 24.9:
                print ("Tienes un peso normal")
            elif resultado >= 25 and resultado < 29.9:
                print("Tienes sobrepeso")
            elif resultado >= 30:
                print("Tienes obesidad.")
            pregunta_usuario_otra_vez = input("Quieres calcular otra vez? ")
            if pregunta_usuario_otra_vez == "no":
                print("Gracias por usar la calculadora de IMC, hasta luego!")
                break
        except ValueError:
            print("Error: Solo se aceptan numeros. Por favor intenta de nuevo.")
        


