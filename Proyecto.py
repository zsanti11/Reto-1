from datetime import datetime
class Experimento:
    def __init__(self, nombre: str, fecha: str, tipo: str, resultados: list[float]):
        if len(resultados) < 3:
            raise ValueError("Se requieren al menos 3 resultados para crear un experimento")    
        self.nombre = nombre
        self.fecha = fecha
        self.tipo = tipo
        self.resultados = resultados

    def diccionario(self):
        return {
            "nombre": self.nombre, 
            "fecha": self.fecha, 
            "tipo": self.tipo,
            "resultados": self.resultados
        }

class GestorExperimento:
    def __init__(self):
        self.experimentos: list[Experimento] = []
        self.TiposValidos = ["Quimica", "Biologia", "Fisica"]

    def agregar_experimentos(self, nombre: str, fecha: str, tipo: str, resultados: list[float]) -> bool:
        try:
            # Validar que haya al menos 3 resultados
            if len(resultados) < 3:
                raise ValueError("Se requieren al menos 3 resultados para crear un experimento")
            
            # Validar fecha
            datetime.strptime(fecha, "%d/%m/%Y")
            
            # Validar tipo
            if tipo not in self.TiposValidos:
                raise ValueError("Tipo de experimento incorrecto.")
            
            nuevo_experimento = Experimento(nombre, fecha, tipo, resultados)
            self.experimentos.append(nuevo_experimento)
            return True
        
        except ValueError as e:
            print(f"Error al agregar el experimento: {str(e)}")
            return False
        
    def visualizar_experimentos(self):
        if not self.experimentos:
            print("No hay experimentos para ver")
            return
        
        for i, exp in enumerate(self.experimentos, 1):
            print(f"\nExperimento #{i}")
            print(f"Nombre: {exp.nombre}")
            print(f"Fecha: {exp.fecha}")
            print(f"Tipo: {exp.tipo}")
            print(f"Resultados: {exp.resultados}")

    def analizar_experimento(self, indice: int):
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
    
    def generar_informe(self, nombre_archivo: str):
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
    gestor = GestorExperimento()
    
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar experimento")
        print("2. Ver experimentos")
        print("3. Analizar experimento")
        print("4. Generar informe")
        print("5. Salir")
        
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
                    print("\nResultados del análisis:")
                    print(f"Promedio: {analisis['promedio']:.2f}")
                    print(f"Máximo: {analisis['maximo']}")
                    print(f"Mínimo: {analisis['minimo']}")
                else:
                    print("Experimento no encontrado o no tiene suficientes resultados")
            except ValueError:
                print("Por favor ingrese un número válido")
            
        elif opcion == "4":
            nombre_archivo = input("Nombre del archivo para el informe: ")
            if not nombre_archivo.endswith('.txt'):
                nombre_archivo += '.txt'
            gestor.generar_informe(nombre_archivo)
            print(f"Informe generado exitosamente en {nombre_archivo}")
            
        elif opcion == "5":
            print("¡Adiós!")
            break
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()