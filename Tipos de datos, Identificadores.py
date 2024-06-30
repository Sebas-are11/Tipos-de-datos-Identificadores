"""
Programa de Ejemplo: Cálculo de Áreas y Conversión de Unidades
Este programa permite calcular el área de un círculo y un rectángulo,
convertir unidades de medida (de metros a pies), y gestionar información
básica de un registro. Se utilizan diferentes tipos de datos y convenciones
de nomenclatura adecuadas.
"""

def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio"""
    PI = 3.14159
    area = PI * (radio ** 2)
    return area

def calcular_area_rectangulo(ancho, alto):
    """Calcula el área de un rectángulo dado su ancho y alto"""
    area = ancho * alto
    return area

def convertir_metros_a_pies(metros):
    """Convierte una medida en metros a pies"""
    pies_por_metro = 3.28084
    pies = metros * pies_por_metro
    return pies

def gestionar_registro(nombre, edad, altura):
    """Gestión básica de un registro con nombre, edad y altura"""
    registro = {
        'nombre': nombre,
        'edad': edad,
        'altura': altura,
        'es_mayor_de_edad': edad >= 18
    }
    return registro

# Ejecución del programa y prueba de funciones
if __name__ == "__main__":
    # Cálculo de áreas
    radio_circulo = 5.0
    ancho_rectangulo = 10.0
    alto_rectangulo = 20.0
    
    area_circulo = calcular_area_circulo(radio_circulo)
    area_rectangulo = calcular_area_rectangulo(ancho_rectangulo, alto_rectangulo)
    
    print(f"Área del círculo con radio {radio_circulo}: {area_circulo}")
    print(f"Área del rectángulo con ancho {ancho_rectangulo} y alto {alto_rectangulo}: {area_rectangulo}")
    
    # Conversión de unidades
    metros = 100.0
    pies = convertir_metros_a_pies(metros)
    
    print(f"{metros} metros equivalen a {pies} pies")
    
    # Gestión de registro
    nombre = "Juan Perez"
    edad = 25
    altura = 1.75
    
    registro = gestionar_registro(nombre, edad, altura)
    
    print(f"Registro: {registro}")
