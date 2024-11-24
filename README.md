# Sistema de Gestión de Experimentos
## Descripción General
Este sistema permite gestionar experimentos científicos de diferentes tipos (Química, Biología, Física), incluyendo la capacidad de agregar, visualizar, analizar y generar informes de los experimentos realizados.

## Estructura del Código

### Clase `Experimento`
#### Descripción
Representa un experimento individual con sus propiedades básicas.

#### Atributos
- `nombre` (str): Nombre identificativo del experimento
- `fecha` (str): Fecha de realización del experimento en formato DD/MM/YYYY
- `tipo` (str): Tipo de experimento (Química, Biología o Física)
- `resultados` (list[float]): Lista de resultados numéricos del experimento

#### Métodos
```python
def __init__(self, nombre: str, fecha: str, tipo: str, resultados: list[float])
```
Constructor que inicializa un nuevo experimento. Valida que haya al menos 3 resultados.

```python
def diccionario(self)
```
Retorna una representación en diccionario del experimento.

### Clase `GestorExperimento`
#### Descripción
Administra la colección de experimentos y proporciona métodos para su gestión.

#### Atributos
- `experimentos` (list[Experimento]): Lista de experimentos almacenados
- `TiposValidos` (list[str]): Lista de tipos de experimentos válidos

#### Métodos
```python
def agregar_experimentos(self, nombre: str, fecha: str, tipo: str, resultados: list[float])
```
Agrega un nuevo experimento a la colección.
- **Validaciones**:
  - Mínimo 3 resultados
  - Formato de fecha válido (DD/MM/YYYY)
  - Tipo de experimento válido
- **Retorna**: `True` si se agregó correctamente, `False` en caso contrario

```python
def visualizar_experimentos(self)
```
Muestra por consola todos los experimentos almacenados.

```python
def analizar_experimento(self, indice: int)
```
Analiza un experimento específico.
- **Parámetros**: 
  - `indice`: Posición del experimento en la lista
- **Retorna**: Diccionario con estadísticas básicas:
  - promedio
  - máximo
  - mínimo

```python
def generar_informe(self, nombre_archivo: str)
```
Genera un informe en formato TXT con todos los experimentos y sus análisis.

### Función `main()`
#### Descripción
Punto de entrada del programa que implementa un menú interactivo con las siguientes opciones:
1. Agregar experimento
2. Ver experimentos
3. Analizar experimento
4. Generar informe
5. Salir

## Flujo de Trabajo

1. **Agregar Experimento**:
   - Solicita nombre, fecha, tipo y resultados
   - Valida los datos ingresados
   - Agrega el experimento si los datos son válidos

2. **Visualizar Experimentos**:
   - Muestra lista numerada de experimentos
   - Presenta detalles de cada experimento

3. **Analizar Experimento**:
   - Muestra lista de experimentos
   - Permite seleccionar uno por número
   - Presenta análisis estadístico básico

4. **Generar Informe**:
   - Solicita nombre del archivo
   - Crea archivo TXT con información detallada
   - Incluye análisis de cada experimento

## Validaciones y Manejo de Errores

### Validaciones Implementadas
- Mínimo 3 resultados por experimento
- Formato de fecha (DD/MM/YYYY)
- Tipo de experimento válido
- Conversión de resultados a números flotantes
- Índices válidos para análisis

### Manejo de Excepciones
- `ValueError` para errores de validación
- Manejo de errores en entrada de usuario
- Validación de formato de números

## Requisitos y Dependencias
- Python 3.x
- Módulo `datetime` de la biblioteca estándar

## Limitaciones y Consideraciones
- Los resultados deben ser valores numéricos
- La fecha debe seguir estrictamente el formato DD/MM/YYYY
- Los tipos de experimento están limitados a Química, Biología y Física
- Los informes se generan únicamente en formato TXT
- No hay persistencia de datos entre ejecuciones

## Ejemplos de Uso

```python
# Crear un nuevo gestor
gestor = GestorExperimento()

# Agregar un experimento
gestor.agregar_experimentos(
    nombre="Prueba pH",
    fecha="23/11/2024",
    tipo="Quimica",
    resultados=[7.0, 7.2, 7.1, 7.3]
)

# Analizar un experimento específico
analisis = gestor.analizar_experimento(0)

# Generar informe
gestor.generar_informe("informe_experimentos.txt")
```
