# Gestor de Experimentos
# Este programa permite gestionar experimentos científicos, incluyendo su creación,
# análisis y comparación de resultados.

from datetime import datetime
from prettytable import PrettyTable

class Experimento:
    """
    Clase que representa un experimento científico.
    
    Atributos:
        nombre (str): Nombre identificativo del experimento
        fecha (str): Fecha de realización en formato DD/MM/YYYY
        tipo (str): Tipo de experimento (Química, Biología, Física)
        resultados (list[float]): Lista de resultados numéricos del experimento
    """
    def __init__(self, nombre: str, fecha: str, tipo: str, resultados: list[float]):
        if len(resultados) < 3:
            raise ValueError("Se requieren al menos 3 resultados para crear un experimento")    
        self.nombre = nombre
        self.fecha = fecha
        self.tipo = tipo
        self.resultados = resultados

    def diccionario(self):
        """
        Convierte el experimento a un diccionario.
        
        Returns:
            dict: Diccionario con los atributos del experimento
        """
        return {
            "nombre": self.nombre, 
            "fecha": self.fecha, 
            "tipo": self.tipo,
            "resultados": self.resultados
        }

class GestorExperimento:
    """
    Clase principal para gestionar múltiples experimentos.
    
    Atributos:
        experimentos (list[Experimento]): Lista de experimentos almacenados
        TiposValidos (list[str]): Tipos de experimentos permitidos
    """
    def __init__(self):
        self.experimentos: list[Experimento] = []
        self.TiposValidos = ["Quimica", "Biologia", "Fisica"]

    def agregar_experimentos(self, nombre: str, fecha: str, tipo: str, resultados: list[float]) -> bool:
        """
        Agrega un nuevo experimento a la lista.
        
        Args:
            nombre: Nombre del experimento
            fecha: Fecha en formato DD/MM/YYYY
            tipo: Tipo de experimento
            resultados: Lista de resultados numéricos
        
        Returns:
            bool: True si se agregó correctamente, False si hubo error
        """
        try:
            if len(resultados) < 3:
                raise ValueError("Se requieren al menos 3 resultados para crear un experimento")
            
            datetime.strptime(fecha, "%d/%m/%Y")
            
            if tipo not in self.TiposValidos:
                raise ValueError("Tipo de experimento incorrecto.")
            
            nuevo_experimento = Experimento(nombre, fecha, tipo, resultados)
            self.experimentos.append(nuevo_experimento)
            return True
        
        except ValueError as e:
            print(f"Error al agregar el experimento: {str(e)}")
            return False
    
    def eliminar_experimento(self, indice: int):
        """
        Elimina un experimento según su índice.
        
        Args:
            indice: Posición del experimento a eliminar
        
        Returns:
            bool: True si se eliminó correctamente, False si hubo error
        """
        try:
            if 0 <= indice < len(self.experimentos):
                self.experimentos.pop(indice)
                return True
            raise ValueError("Índice de experimento no válido")
        except ValueError as e:
            print(f"Error al eliminar el experimento: {str(e)}")
            return False
        
    def visualizar_experimentos(self):
        """
        Muestra una tabla con todos los experimentos almacenados.
        Utiliza PrettyTable para formatear la salida.
        """
        if not self.experimentos:
            print("No hay experimentos para ver")
            return

        tabla = PrettyTable()
        tabla.field_names = ["#", "Nombre", "Fecha", "Tipo", "Resultados"]
        tabla.align = "l"
        
        for i, exp in enumerate(self.experimentos, 1):
            tabla.add_row([
                i, exp.nombre, exp.fecha, exp.tipo, ", ".join(map(str, exp.resultados))
            ])

        print("\033[95m" + str(tabla) + "\033[0m")

    def analizar_experimento(self, indice: int):
        """
        Realiza un análisis estadístico básico de un experimento.
        
        Args:
            indice: Índice del experimento a analizar
        
        Returns:
            dict: Diccionario con promedio, máximo y mínimo de los resultados
                 o diccionario vacío si hay error
        """
        if 0 <= indice < len(self.experimentos):
            exp = self.experimentos[indice]
            if len(exp.resultados) < 3:
                print("Error: Se requieren al menos 3 resultados para realizar el análisis")
                return {}
            
            return {
                "promedio": sum(exp.resultados) / len(exp.resultados),
                "maximo": max(exp.resultados),
                "minimo": min(exp.resultados)
            }
        return {}
    
    def comparar_experimentos(self, indices: list[int]):
        """
        Compara múltiples experimentos mostrando sus métricas principales.
        
        Args:
            indices: Lista de índices de los experimentos a comparar
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
            if not analisis:
                continue
                
            tabla.add_row([
                exp.nombre,
                f"{analisis['promedio']:.2f}",
                f"{analisis['maximo']}",
                f"{analisis['minimo']}"
            ])
            
            if analisis['promedio'] > mejor_promedio:
                mejor_promedio = analisis['promedio']
                mejor_exp = exp.nombre
            if analisis['promedio'] < peor_promedio:
                peor_promedio = analisis['promedio']
                peor_exp = exp.nombre
        
        print("\nComparación de experimentos:")
        print("\033[95m" + str(tabla) + "\033[0m")
        print(f"\nMejor desempeño: {mejor_exp} (promedio: {mejor_promedio:.2f})")
        print(f"Peor desempeño: {peor_exp} (promedio: {peor_promedio:.2f})")
    
    def generar_informe(self, nombre_archivo: str):
        """
        Genera un informe en formato texto con todos los experimentos y sus análisis.
        
        Args:
            nombre_archivo: Nombre del archivo donde se guardará el informe
        """
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write("INFORME DE EXPERIMENTOS\n")
            f.write("=" * 30 + "\n\n")
            
            for i, exp in enumerate(self.experimentos, 1):
                f.write(f"Experimento #{i}\n")
                f.write(f"Nombre: {exp.nombre}\n")
                f.write(f"Fecha: {exp.fecha}\n")
                f.write(f"Tipo: {exp.tipo}\n")
                f.write(f"Resultados: {exp.resultados}\n")
                
                if len(exp.resultados) >= 3:
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
    Permite al usuario interactuar con todas las funcionalidades del gestor
    de experimentos mediante un menú de opciones.
    """
    gestor = GestorExperimento()
    
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
            print("Tipos disponibles:", ", ".join(gestor.TiposValidos))
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
            
            if gestor.agregar_experimentos(nombre, fecha, tipo, resultados):
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
