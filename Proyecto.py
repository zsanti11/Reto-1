from datetime import datetime
from prettytable import PrettyTable

class Experimento:
    def crear_experimento(nombre, fecha, tipo, resultados):
        """
        Crea un experimento como un diccionario.
        """
        if len(resultados) < 3:
            raise ValueError("Se requieren al menos 3 resultados para crear un experimento")
        
        return {
            "nombre": nombre, 
            "fecha": fecha, 
            "tipo": tipo,
            "resultados": resultados
        }

class GestorExperimentos:
    def __init__(self):
        """
        Inicializa el gestor con una lista de experimentos y tipos válidos.
        """
        self.experimentos = []
        self.tipos_validos = ["Quimica", "Biologia", "Fisica"]

    def validar_datos(self, nombre, fecha, tipo, resultados):
        """
        Valida los datos de un experimento antes de agregarlo.
        """
        if len(resultados) < 3:
            print("Error: Se requieren al menos 3 resultados")
            return False

        try:
            datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            print("Error: Formato de fecha incorrecto")
            return False

        if tipo not in self.tipos_validos:
            print("Error: Tipo de experimento incorrecto")
            return False

        return True

    def agregar_experimento(self, nombre, fecha, tipo, resultados):
        """
        Agrega un nuevo experimento a la lista.
        """
        if not self.validar_datos(nombre, fecha, tipo, resultados):
            return False
        
        experimento = Experimento.crear_experimento(nombre, fecha, tipo, resultados)
        self.experimentos.append(experimento)
        return True

    def eliminar_experimento(self, indice):
        """
        Elimina un experimento de la lista por su índice.
        """
        try:
            if 0 <= indice < len(self.experimentos):
                del self.experimentos[indice]
                return True
            print("Error: Índice de experimento no válido")
            return False
        except Exception as e:
            print(f"Error al eliminar el experimento: {str(e)}")
            return False

    def visualizar_experimentos(self):
        """
        Muestra una tabla con todos los experimentos almacenados.
        """
        if not self.experimentos:
            print("No hay experimentos para ver")
            return

        tabla = PrettyTable()
        tabla.field_names = ["#", "Nombre", "Fecha", "Tipo", "Resultados"]
        tabla.align = "l"
        
        for i, exp in enumerate(self.experimentos, 1):
            tabla.add_row([
                i, 
                exp["nombre"], 
                exp["fecha"], 
                exp["tipo"], 
                ", ".join(map(str, exp["resultados"]))
            ])

        print("\033[95m" + str(tabla) + "\033[0m")

    def analizar_experimento(self, indice):
        """
        Realiza un análisis estadístico básico con los datos de promedio, valor maximo y valor minimo de un experimento.
        """
        if 0 <= indice < len(self.experimentos):
            exp = self.experimentos[indice]
            resultados = exp["resultados"]
            
            if len(resultados) < 3:
                print("Error: Se requieren al menos 3 resultados para realizar el análisis")
                return {}
            
            return {
                "promedio": sum(resultados) / len(resultados),
                "maximo": max(resultados),
                "minimo": min(resultados)
            }
        return {}

    def comparar_experimentos(self, indices):
        """
        Compara múltiples experimentos mostrando sus valores principales.
        """
        if not all(0 <= i < len(self.experimentos) for i in indices):
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
            exp = self.experimentos[i]
            analisis = self.analizar_experimento(i)
            
            tabla.add_row([
                exp["nombre"],
                f"{analisis['promedio']:.2f}",
                f"{analisis['maximo']}",
                f"{analisis['minimo']}"
            ])
            
            if analisis['promedio'] > mejor_promedio:
                mejor_promedio = analisis['promedio']
                mejor_exp = exp["nombre"]
            if analisis['promedio'] < peor_promedio:
                peor_promedio = analisis['promedio']
                peor_exp = exp["nombre"]
        
        print("\nComparación de experimentos:")
        print("\033[95m" + str(tabla) + "\033[0m")
        print(f"\nMejor desempeño: {mejor_exp} (promedio: {mejor_promedio:.2f})")
        print(f"Peor desempeño: {peor_exp} (promedio: {peor_promedio:.2f})")

    def generar_informe(self, nombre_archivo):
        """
        Genera un informe en formato texto con todos los experimentos y sus análisis.
        """
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write("INFORME DE EXPERIMENTOS\n")
            f.write("=" * 30 + "\n\n")
            
            for i, exp in enumerate(self.experimentos, 1):
                f.write(f"Experimento #{i}\n")
                f.write(f"Nombre: {exp['nombre']}\n")
                f.write(f"Fecha: {exp['fecha']}\n")
                f.write(f"Tipo: {exp['tipo']}\n")
                f.write(f"Resultados: {exp['resultados']}\n")
                
                if len(exp['resultados']) >= 3:
                    analisis = self.analizar_experimento(i-1)
                    f.write(f"Análisis de resultados:\n")
                    f.write(f"- Promedio: {analisis.get('promedio', 0):.2f}\n")
                    f.write(f"- Máximo: {analisis.get('maximo', 0)}\n")
                    f.write(f"- Mínimo: {analisis.get('minimo', 0)}\n")
                else:
                    f.write("No hay suficientes resultados para realizar el análisis (mínimo 3)\n")
                f.write("\n")

def main():
    """
    Función principal que ejecuta el menú interactivo del programa.
    """
    gestor = GestorExperimentos()
    
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
            print("Tipos disponibles:", ", ".join(gestor.tipos_validos))
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
            
            if gestor.agregar_experimento(nombre, fecha, tipo, resultados):
                print("Experimento agregado exitosamente")
            
        elif opcion == "2":
            gestor.visualizar_experimentos()
            
        elif opcion == "3":
            gestor.visualizar_experimentos()
            try:
                indice = int(input("Ingrese el número de experimento a analizar: ")) - 1
                analisis = gestor.analizar_experimento(indice)
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
            except ValueError:
                print("Por favor ingrese un número válido")
                
        elif opcion == "4":
            gestor.visualizar_experimentos()
            try:
                indices = input("Ingrese los números de experimentos a comparar (separados por comas): ")
                indices = [int(i.strip()) - 1 for i in indices.split(",")]
                gestor.comparar_experimentos(indices)
            except ValueError:
                print("Por favor ingrese números válidos separados por comas")
                
        elif opcion == "5":
            gestor.visualizar_experimentos()
            try:
                indice = int(input("Ingrese el número de experimento a eliminar: ")) - 1
                if gestor.eliminar_experimento(indice):
                    print("Experimento eliminado exitosamente")
            except ValueError:
                print("Por favor ingrese un número válido")
            
        elif opcion == "6":
            nombre_archivo = input("Nombre del archivo para el informe: ")
            if not nombre_archivo.endswith('.txt'):
                nombre_archivo += '.txt'
            gestor.generar_informe(nombre_archivo)
            print(f"Informe generado exitosamente en {nombre_archivo}")
            
        elif opcion == "7":
            print("¡Adiós!")
            break
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()