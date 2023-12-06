import sqlite3

conn = sqlite3.connect('slang_panameno.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS palabras_slang (palabra TEXT PRIMARY KEY, significado TEXT)''')
conn.commit()

def agregar_palabra():
    palabra = input("Ingrese la nueva palabra: ")
    significado = input("Ingrese el significado de la palabra: ")
    c.execute("INSERT INTO palabras_slang (palabra, significado) VALUES (?, ?)", (palabra, significado))
    conn.commit()
    print("Palabra agregada correctamente.")

def editar_palabra():
    palabra = input("Ingrese la palabra que desea editar: ")
    nuevo_significado = input("Ingrese el nuevo significado de la palabra: ")
    c.execute("UPDATE palabras_slang SET significado = ? WHERE palabra = ?", (nuevo_significado, palabra))
    conn.commit()
    print("Palabra editada correctamente.")

def eliminar_palabra():
    palabra = input("Ingrese la palabra que desea eliminar: ")
    c.execute("DELETE FROM palabras_slang WHERE palabra = ?", (palabra,))
    conn.commit()
    print("Palabra eliminada correctamente.")

def ver_listado():
    c.execute("SELECT * FROM palabras_slang")
    palabras = c.fetchall()
    for palabra in palabras:
        print(f"{palabra[0]}: {palabra[1]}")

def buscar_significado():
    palabra = input("Ingrese la palabra que desea buscar: ")
    c.execute("SELECT significado FROM palabras_slang WHERE palabra = ?", (palabra,))
    resultado = c.fetchone()
    if resultado:
        print(f"Significado de '{palabra}': {resultado[0]}")
    else:
        print("Palabra no encontrada en el diccionario.")

while True:
    print("\nOpciones:")
    print("a) Agregar nueva palabra")
    print("c) Editar palabra existente")
    print("d) Eliminar palabra existente")
    print("e) Ver listado de palabras")
    print("f) Buscar significado de palabra")
    print("g) Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "a":
        agregar_palabra()
    elif opcion == "c":
        editar_palabra()
    elif opcion == "d":
        eliminar_palabra()
    elif opcion == "e":
        ver_listado()
    elif opcion == "f":
        buscar_significado()
    elif opcion == "g":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

conn.close()