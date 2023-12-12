from pymongo import MongoClient

# Conectarse a la base de datos MongoDB
cliente = MongoClient('localhost', 27017)
db = cliente['slang_panameno']
coleccion = db['diccionario']

# Funciones modificadas para utilizar MongoDB

def agregar_palabra():
    palabra = input("Palabra: ").lower()
    significado = input("Significado: ")

    nueva_palabra = {
        'palabra': palabra,
        'significado': significado
    }

    coleccion.insert_one(nueva_palabra)
    print("Palabra agregada correctamente.")

def editar_palabra():
    palabra = input("Palabra a editar: ").lower()
    nuevo_significado = input("Nuevo significado: ")

    palabra_existente = coleccion.find_one({'palabra': palabra})
    if palabra_existente:
        coleccion.update_one({'palabra': palabra}, {'$set': {'significado': nuevo_significado}})
        print("Palabra editada correctamente.")
    else:
        print("Palabra no encontrada en el diccionario.")

def eliminar_palabra():
    palabra = input("Palabra a eliminar: ").lower()

    resultado = coleccion.delete_one({'palabra': palabra})
    if resultado.deleted_count > 0:
        print("Palabra eliminada correctamente.")
    else:
        print("Palabra no encontrada en el diccionario.")

def ver_listado():
    palabras = coleccion.find()

    if palabras.count() == 0:
        print("El diccionario está vacío.")
    else:
        for palabra in palabras:
            print(f"{palabra['palabra']}: {palabra['significado']}")

def buscar_significado():
    palabra = input("Palabra a buscar: ").lower()

    palabra_existente = coleccion.find_one({'palabra': palabra})
    if palabra_existente:
        print(f"Significado de {palabra}: {palabra_existente['significado']}")
    else:
        print("Palabra no encontrada en el diccionario.")

def main():
    while True:
        print("\nMenú:")
        print("a) Agregar nueva palabra")
        print("c) Editar palabra existente")
        print("d) Eliminar palabra existente")
        print("e) Ver listado de palabras")
        print("f) Buscar significado de palabra")
        print("g) Salir")

        opcion = input("Selecciona una opción: ").lower()

        if opcion == 'a':
            agregar_palabra()
        elif opcion == 'c':
            editar_palabra()
        elif opcion == 'd':
            eliminar_palabra()
        elif opcion == 'e':
            ver_listado()
        elif opcion == 'f':
            buscar_significado()
        elif opcion == 'g':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
