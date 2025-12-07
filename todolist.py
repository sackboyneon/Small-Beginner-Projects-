diccionario_tareas = {
        "Estudiar": "Python",
        "Jugar": "GT7",
        "Lavar los platos": "Me toca a mi lavarlos"
}

diccionario_autos = {
    "Ferrari": "430",
    "Porsche": "911",
    "Nissan": "Skyline"
}

print("A: Ver lista de tareas ")
print("B: Agregar una tarea ")
print("C: Eliminar una tarea ")
print("D: Cerrar programa")
opcion = input("Elija una opcion de las siguientes: ")

if opcion == "A":
    for key, value in diccionario_tareas.items():
        print(f"Tu tarea es {key} y la descripcion es {value}")
    for key, value in diccionario_autos.items():
        print(f"El auto es el {key} del modelo {value}")
elif opcion == "B":
    nombre_tarea = input("Ingrese el nombre de la tarea: ")
    nombre_descripcion = input("Ingrese descripcion: ")
    diccionario_tareas.update({nombre_tarea: nombre_descripcion})
    diccionario_autos.update({nombre_tarea: nombre_descripcion})
    print(diccionario_tareas)

elif opcion == "C":
    eliminacion_tarea = input("Que tarea quieres eliminar? ")
    if eliminacion_tarea in diccionario_tareas:
            diccionario_tareas.pop(eliminacion_tarea)
            print(f"La tarea eliminada fue {eliminacion_tarea}")
            print(diccionario_tareas)
    if eliminacion_tarea in diccionario_autos:
        diccionario_autos.pop(eliminacion_tarea)
        print(f"La tarea eliminada fue {eliminacion_tarea}")
        print(diccionario_autos)

if opcion == "D":
    print("Ese fue mi primer programa bien")
exit() 



    
      
 
