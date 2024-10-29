import sqlite3

conn = sqlite3.connect('EESTN5.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS alumnos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER
    )
''')
conn.commit()


cursor.execute("DELETE FROM alumnos")
conn.commit()


alumnos_data = [
    (1, 'Mastantuono', 18),
    (2, 'Haaland', 16),
    (3, 'Mbappe', 19),
    (4, 'Maradona', 20),
    (5, 'Pele', 15),
    (6, 'Neymar', 17),
    (7, 'Ronaldo', 18),
    (8, 'Messi', 22)
]

cursor.executemany("INSERT INTO alumnos (id, nombre, edad) VALUES (?, ?, ?)", alumnos_data)
conn.commit()

cursor.execute("SELECT * FROM alumnos WHERE edad > 17")
alumnos_mayores = cursor.fetchall()

for alumno in alumnos_mayores:
    print(f"ID: {alumno[0]}, Nombre: {alumno[1]}, Edad: {alumno[2]}")

conn.close()
