import json

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.articulos = self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def guardar_inventario(self):
        with open(self.archivo, "w") as file:
            json.dump(self.articulos, file, indent=2)

    def agregar_articulo(self, nombre, cantidad, precio):
        nuevo_articulo = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }
        self.articulos.append(nuevo_articulo)
        self.guardar_inventario()
        print(f"Artículo '{nombre}' agregado al inventario.")

    def buscar_articulo(self, nombre):
        for articulo in self.articulos:
            if articulo["nombre"] == nombre:
                return articulo
        print(f"Artículo '{nombre}' no encontrado en el inventario.")
        return None

    def editar_articulo(self, nombre, nueva_cantidad, nuevo_precio):
        articulo = self.buscar_articulo(nombre)
        if articulo:
            articulo["cantidad"] = nueva_cantidad
            articulo["precio"] = nuevo_precio
            self.guardar_inventario()
            print(f"Artículo '{nombre}' editado en el inventario.")

    def eliminar_articulo(self, nombre):
        articulo = self.buscar_articulo(nombre)
        if articulo:
            self.articulos.remove(articulo)
            self.guardar_inventario()
            print(f"Artículo '{nombre}' eliminado del inventario.")

def mostrar_menu():
    print("\n=== Menú ===")
    print("1. Agregar artículo")
    print("2. Buscar artículo")
    print("3. Editar artículo")
    print("4. Eliminar artículo")
    print("5. Mostrar inventario")
    print("0. Salir")

if __name__ == "__main__":
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del artículo: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_articulo(nombre, cantidad, precio)

        elif opcion == "2":
            nombre = input("Nombre del artículo a buscar: ")
            articulo = inventario.buscar_articulo(nombre)
            if articulo:
                print("Detalles del artículo:")
                print(json.dumps(articulo, indent=2))

        elif opcion == "3":
            nombre = input("Nombre del artículo a editar: ")
            nueva_cantidad = int(input("Nueva cantidad: "))
            nuevo_precio = float(input("Nuevo precio: "))
            inventario.editar_articulo(nombre, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Nombre del artículo a eliminar: ")
            inventario.eliminar_articulo(nombre)

        elif opcion == "5":
            print("\nInventario actual:")
            print(json.dumps(inventario.articulos, indent=2))

        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")
