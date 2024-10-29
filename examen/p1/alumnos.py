alumnos = ["Mastantuono", "Haaland", "Mbappe", "Maradona", "Pele", "Neymar", "Ronaldo", "Messi"]

notas = {
    "Mastantuono": [7, 8, 9, 10, 7, 8],
    "Haaland": [6, 7, 8, 9, 10, 7],
    "Mbappe": [8, 9, 7, 8, 10, 6],
    "Maradona": [9, 9, 10, 8, 7, 9],
    "Pele": [6, 5, 8, 7, 6, 7],
    "Neymar": [10, 9, 10, 8, 9, 10],
    "Ronaldo": [8, 8, 7, 9, 8, 8],
    "Messi": [9, 10, 8, 7, 9, 10]
}

for alumno in alumnos:
    promedio = sum(notas[alumno]) / len(notas[alumno])
    print(f"{alumno}: El promedio del alumno es= {promedio:.2f}")
