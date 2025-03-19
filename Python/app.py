def ingresar_datos():
    personas = []

    # Solicitar el número de personas a registrar
    cantidad_personas = int(input("¿Cuántas personas deseas registrar? "))

    for i in range(cantidad_personas):
        # Solicitar nombre y edad
        nombre = input(f"Ingresa el nombre de la persona {i + 1}: ")
        edad = input(f"Ingresa la edad de {nombre}: ")

        # Validar y pedir la nota hasta que sea un número válido
        while True:
            try:
                nota = float(input(f"Ingresa la nota de {nombre}: "))
                break  # Si la conversión es exitosa, salir del ciclo
            except ValueError:
                print("Por favor ingresa una nota válida (un número).")
        
        # Almacenar los datos en una lista
        personas.append([nombre, edad, nota])

    # Mostrar los datos tal como fueron ingresados
    print("\nListado de personas ingresadas:")
    for persona in personas:
        print(f"Nombre: {persona[0]}, Edad: {persona[1]}, Nota: {persona[2]}")

    # Ordenar la lista por nota, de mayor a menor
    personas.sort(key=lambda x: x[2], reverse=True)

    # Mostrar la lista ordenada por nota
    print("\nListado de personas ordenado por nota (de mayor a menor):")
    for persona in personas:
        print(f"Nombre: {persona[0]}, Edad: {persona[1]}, Nota: {persona[2]}")

# Llamar a la función para ejecutar el programa
ingresar_datos()
