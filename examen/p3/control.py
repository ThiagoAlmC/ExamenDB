calificaciones = []

print("Ingresa las calificaciones undividualmente. Escribe 'fin' para finalizar.")

while True:
    entrada = input("Calificación: ")
    
    if entrada.lower() == 'fin':
        break

    try:
        calificacion = float(entrada)
        if 0 <= calificacion <= 10:
            calificaciones.append(calificacion)
        else:
            print("Calificación entre 0 y 10.")
    except ValueError:
        print("Error. Hacelo bien pibe, pone un número o escribi 'fin' para finalizar.")

if calificaciones:
    calificacion_max = max(calificaciones)
    calificacion_min = min(calificaciones)
    promedio = sum(calificaciones) / len(calificaciones)
    promedio_menor = promedio 

    print("\nResultados:")
    print(f"Calificación más alta: {calificacion_max}")
    print(f"Calificación más baja: {calificacion_min}")
    print(f"Promedio: {promedio:.2f}")

    estado = "Aprobado" if promedio >= 7 else "Desaprobado"
    print(f"Por el promedio esta: {estado}")

else:
    print("No hay calificaciones, jaja saludos.")

