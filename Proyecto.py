from datetime import datetime
from prettytable import PrettyTable

# Tipos válidos de experimentos
TIPOS_VALIDOS = ["Quimica", "Biologia", "Fisica".lower()]

def validar_experimento(nombre, fecha, tipo, resultados):
    """
    Valida los datos de un experimento antes de agregarlo.
    
    Args:
        nombre (str): Nombre del experimento
        fecha (str): Fecha del experimento
        tipo (str): Tipo de experimento
        resultados (list): Lista de resultados numéricos
    
    Returns:
        bool: True si el experimento es válido, False en caso contrario
    """
    try:
        # Validación de número de resultados
        if len(resultados) < 3:
            print("Error: Se requieren al menos 3 resultados")
            return False
        
        # Validación de formato de fecha
        datetime.strptime(fecha, "%d/%m/%Y")
        
        # Validación de tipo de experimento
        if tipo not in TIPOS_VALIDOS:
            print("Error: Tipo de experimento incorrecto")
            return False
        
        return True
    
    except ValueError as e:
        print(f"Error de validación: {str(e)}")
        return False

def crear_experimento(nombre, fecha, tipo, resultados):
    """
    Crea un diccionario que representa un experimento.
    
    Args:
        nombre (str): Nombre del experimento
        fecha (str): Fecha del experimento
        tipo (str): Tipo de experimento
        resultados (list): Lista de resultados numéricos
    
    Returns:
        dict: Diccionario con los datos del experimento
    """
    return {
        "nombre": nombre, 
        "fecha": fecha, 
        "tipo": tipo,
        "resultados": resultados
    }

def agregar_experimento(experimentos, nombre, fecha, tipo, resultados):
    """
    Agrega un nuevo experimento a la lista de experimentos.
    
    Args:
        experimentos (list): Lista de experimentos existentes
        nombre (str): Nombre del experimento
        fecha (str): Fecha del experimento
        tipo (str): Tipo de experimento
        resultados (list): Lista de resultados numéricos
    
    Returns:
        list: Lista actualizada de experimentos
    """
    if validar_experimento(nombre, fecha, tipo, resultados):
        nuevo_experimento = crear_experimento(nombre, fecha, tipo, resultados)
        experimentos.append(nuevo_experimento)
        print("Experimento agregado exitosamente")
    return experimentos

def eliminar_experimento(experimentos, indice):
    """
    Elimina un experimento de la lista según su índice.
    
    Args:
        experimentos (list): Lista de experimentos
        indice (int): Índice del experimento a eliminar
    
    Returns:
        list: Lista actualizada de experimentos
    """
    try:
        if 0 <= indice < len(experimentos):
            del experimentos[indice]
            print("Experimento eliminado exitosamente")
        else:
            print("Índice de experimento no válido")
    except Exception as e:
        print(f"Error al eliminar el experimento: {str(e)}")
    
    return experimentos

def visualizar_experimentos(experimentos):
    """
    Muestra una tabla con todos los experimentos almacenados.
    
    Args:
        experimentos (list): Lista de experimentos
    """
    if not experimentos:
        print("No hay experimentos para ver")
        return

    tabla = PrettyTable()
    tabla.field_names = ["#", "Nombre", "Fecha", "Tipo", "Resultados"]
    tabla.align = "l"
    
    for i, exp in enumerate(experimentos, 1):
        tabla.add_row([
            i, exp['nombre'], exp['fecha'], exp['tipo'], 
            ", ".join(map(str, exp['resultados']))
        ])

    print("\033[95m" + str(tabla) + "\033[0m")

def analizar_experimento(experimento):
    """
    Realiza un análisis estadístico básico de un experimento.
    
    Args:
        experimento (dict): Diccionario de un experimento
    
    Returns:
        dict: Diccionario con promedio, máximo y mínimo de los resultados
    """
    resultados = experimento['resultados']
    if len(resultados) < 3:
        print("Error: Se requieren al menos 3 resultados para realizar el análisis")
        return {}
    
    return {
        "promedio": sum(resultados) / len(resultados),
        "maximo": max(resultados),
        "minimo": min(resultados)
    }

def comparar_experimentos(experimentos, indices):
    """
    Compara múltiples experimentos mostrando sus métricas principales.
    
    Args:
        experimentos (list): Lista de experimentos
        indices (list): Lista de índices de los experimentos a comparar
    """
    if not all(0 <= i < len(experimentos) for i in indices):
        print("Error: Algunos índices de experimentos no son válidos")
        return
    
    tabla = PrettyTable()
    tabla.field_names = ["Experimento", "Promedio", "Máximo", "Mínimo"]
    tabla.align = "l"
    
    mejor_promedio = float('-inf')
    peor_promedio = float('inf')
    mejor_exp = None
    peor_exp = None
    
    for i in indices:
        exp = experimentos[i]
        analisis = analizar_experimento(exp)
        if not analisis:
            continue
            
        tabla.add_row([
            exp['nombre'],
            f"{analisis['promedio']:.2f}",
            f"{analisis['maximo']}",
            f"{analisis['minimo']}"
        ])
        
        if analisis['promedio'] > mejor_promedio:
            mejor_promedio = analisis['promedio']
            mejor_exp = exp['nombre']
        if analisis['promedio'] < peor_promedio:
            peor_promedio = analisis['promedio']
            peor_exp = exp['nombre']
    
    print("\nComparación de experimentos:")
    print("\033[95m" + str(tabla) + "\033[0m")
    
    if mejor_exp and peor_exp:
        print(f"\nMejor desempeño: {mejor_exp} (promedio: {mejor_promedio:.2f})")
        print(f"Peor desempeño: {peor_exp} (promedio: {peor_promedio:.2f})")

def generar_informe(experimentos, nombre_archivo):
    """
    Genera un informe en formato texto con todos los experimentos y sus análisis.
    
    Args:
        experimentos (list): Lista de experimentos
        nombre_archivo (str): Nombre del archivo de informe
    """
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write("INFORME DE EXPERIMENTOS\n")
        f.write("=" * 30 + "\n\n")
        
        for i, exp in enumerate(experimentos, 1):
            f.write(f"Experimento #{i}\n")
            f.write(f"Nombre: {exp['nombre']}\n")
            f.write(f"Fecha: {exp['fecha']}\n")
            f.write(f"Tipo: {exp['tipo']}\n")
            f.write(f"Resultados: {exp['resultados']}\n")
            
            if len(exp['resultados']) >= 3:
                analisis = analizar_experimento(exp)
                f.write(f"Análisis de resultados:\n")
                f.write(f"- Promedio: {analisis.get('promedio', 0):.2f}\n")
                f.write(f"- Máximo: {analisis.get('maximo', 0)}\n")
                f.write(f"- Mínimo: {analisis.get('minimo', 0)}\n")
            else:
                f.write("No hay suficientes resultados para realizar el análisis (mínimo 3)\n")
            f.write("\n")
    print(f"Informe generado en {nombre_archivo}")

def main():
    """
    Función principal que ejecuta el menú interactivo del programa.
    """
    experimentos = []
    
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar experimento")
        print("2. Ver experimentos")
        print("3. Analizar experimento")
        print("4. Comparar experimentos")
        print("5. Eliminar experimento")
        print("6. Generar informe")
        print("7. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del experimento: ")
            fecha = input("Fecha (DD/MM/YYYY): ")
            print("Tipos disponibles:", ", ".join(TIPOS_VALIDOS))
            tipo = input("Tipo de experimento: ")
            resultados = []
            print("Ingrese al menos 3 resultados:")
            while True:
                valor = input("Ingrese resultado (o 'fin' para terminar): ")
                if valor.lower() == 'fin':
                    if len(resultados) < 3:
                        print("Error: Debe ingresar al menos 3 resultados")
                        continue
                    break
                try:
                    resultados.append(float(valor))
                except ValueError:
                    print("Por favor ingrese un número válido")
            
            experimentos = agregar_experimento(experimentos, nombre, fecha, tipo, resultados)
            
        elif opcion == "2":
            visualizar_experimentos(experimentos)
            
        elif opcion == "3":
            visualizar_experimentos(experimentos)
            try:
                indice = int(input("Ingrese el número de experimento a analizar: ")) - 1
                if 0 <= indice < len(experimentos):
                    analisis = analizar_experimento(experimentos[indice])
                    if analisis:
                        tabla = PrettyTable()
                        tabla.field_names = ["Métrica", "Valor"]
                        tabla.align = "l"
                        tabla.add_row(["Promedio", f"{analisis['promedio']:.2f}"])
                        tabla.add_row(["Máximo", analisis['maximo']])
                        tabla.add_row(["Mínimo", analisis['minimo']])
                        print("\nResultados del análisis:")
                        print("\033[95m" + str(tabla) + "\033[0m")
                    else:
                        print("Experimento no encontrado o no tiene suficientes resultados")
                else:
                    print("Número de experimento inválido")
            except ValueError:
                print("Por favor ingrese un número válido")
                
        elif opcion == "4":
            visualizar_experimentos(experimentos)
            try:
                indices = input("Ingrese los números de experimentos a comparar (separados por comas): ")
                indices = [int(i.strip()) - 1 for i in indices.split(",")]
                comparar_experimentos(experimentos, indices)
            except ValueError:
                print("Por favor ingrese números válidos separados por comas")
                
        elif opcion == "5":
            visualizar_experimentos(experimentos)
            try:
                indice = int(input("Ingrese el número de experimento a eliminar: ")) - 1
                experimentos = eliminar_experimento(experimentos, indice)
            except ValueError:
                print("Por favor ingrese un número válido")
            
        elif opcion == "6":
            nombre_archivo = input("Nombre del archivo para el informe: ")
            if not nombre_archivo.endswith('.txt'):
                nombre_archivo += '.txt'
            generar_informe(experimentos, nombre_archivo)
            
        elif opcion == "7":
            print("¡Adiós!")
            break
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()