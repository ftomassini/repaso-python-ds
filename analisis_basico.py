"""
Práctica de repaso de Python - Curso de Data Science
Repaso de variables, estructuras de control, estructuras de datos y funciones.
"""

# =====================================================================
# Tarea 1: Definición de Variables
# =====================================================================
# Cuatro variables, una por cada tipo de dato básico que pide la consigna.
nombre_producto = "Teclado mecánico"   # str  -> texto
precio_producto = 85.50                # float -> número con decimales
stock_producto = 12                    # int   -> número entero
tiene_descuento = True                 # bool  -> verdadero / falso

# f-string: la f adelante de las comillas permite meter variables entre llaves.
print(f"Producto: {nombre_producto} | Precio: ${precio_producto} | "
      f"Stock: {stock_producto} unidades | ¿Tiene descuento?: {tiene_descuento}")

print()  # línea en blanco para que la salida se lea mejor


# =====================================================================
# Tarea 2: Lógica de Negocio (Bucle + Condicional)
# =====================================================================
# Lista de precios: una lista guarda una secuencia ordenada de valores.
precios = [45.0, 120.5, 99.99, 250.0, 80.0, 100.0]

print("Clasificación de precios:")

# El for recorre la lista elemento por elemento.
# Uso 'valor' como nombre del elemento para no pisar 'precio_producto'.
for valor in precios:
    if valor > 100:
        # Entra acá solo si la condición es verdadera.
        print(f"  ${valor} -> Caro")
    else:
        # El else cubre todos los casos restantes (menor o igual a 100).
        print(f"  ${valor} -> Económico")

print()


# =====================================================================
# Tarea 3: Estructura de Datos Compleja
# =====================================================================
# Diccionario: cada producto (clave) apunta a su stock (valor).
# A diferencia de la lista, acá se accede por nombre y no por posición.
almacen = {
    "teclado": 12,
    "mouse": 30,
    "monitor": 7,
    "auriculares": 18,
}

# Agregar un producto nuevo: basta con asignar una clave que no existía.
almacen["webcam"] = 5

# Consultar el stock de un producto específico.
producto_consultado = "monitor"
print(f"Stock actual de '{producto_consultado}': {almacen[producto_consultado]} unidades")

# Variante segura: .get() devuelve un valor por defecto si la clave no existe,
# en lugar de cortar el programa con un KeyError.
print(f"Stock de 'parlantes': {almacen.get('parlantes', 0)} unidades")

print(f"Almacén completo: {almacen}")
print()


# =====================================================================
# Tarea 4: Modularización con Funciones
# =====================================================================
def resumen_estadistico(numeros):
    """
    Recibe una lista de números y devuelve un diccionario con
    la suma total, el promedio y la cantidad de elementos.
    """
    cantidad = len(numeros)                  # cuántos elementos tiene la lista
    suma_total = sum(numeros)                # suma de todos los elementos

    # Evito dividir por cero si llega una lista vacía.
    promedio = suma_total / cantidad if cantidad > 0 else 0

    # La función devuelve un diccionario, así quien la llama accede por nombre.
    return {
        "suma_total": suma_total,
        "promedio": promedio,
        "cantidad": cantidad,
    }


# Llamada con una lista de ejemplo.
resultado = resumen_estadistico([10, 20, 30])
print(f"Resumen de [10, 20, 30]: {resultado}")

# La misma función sirve para cualquier lista de números, por ejemplo 'precios'.
resumen_precios = resumen_estadistico(precios)
print(f"Resumen de la lista 'precios': {resumen_precios}")

# Como devuelve un diccionario, se puede acceder a un dato puntual.
print(f"El promedio de los precios es ${resumen_precios['promedio']:.2f}")
