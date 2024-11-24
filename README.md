# Sistema de Gestión de Experimentos Científicos 🧪

Un sistema robusto para la gestión y análisis de experimentos de laboratorio desarrollado en Python. Esta aplicación permite a los investigadores y estudiantes registrar, analizar y documentar experimentos científicos de manera sistemática y eficiente.

## 🌟 Características Principales

- ✅ Gestión completa de experimentos (crear, ver, analizar, eliminar)
- 📊 Análisis estadístico de resultados
- 📈 Comparación entre múltiples experimentos
- 📝 Generación de informes detallados
- 🔍 Validación robusta de datos
- 🎯 Interfaz de usuario interactiva mediante menú de consola

## 🛠️ Tecnologías Utilizadas

- Python 3.x
- PrettyTable (para visualización de datos tabulares)
- Módulo datetime (para manejo y validación de fechas)

## 📋 Requisitos Previos

```bash
pip install prettytable
```

## 🚀 Instalación y Uso

1. Clona el repositorio:
```bash
git clone [https://github.com/zsanti11/Reto-1]
cd gestor-experimentos
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta el programa:
```bash
python main.py
```

## 💡 Guía de Uso

### Menú Principal
El sistema presenta las siguientes opciones:
1. Agregar experimento
2. Ver experimentos
3. Analizar experimento
4. Comparar experimentos
5. Eliminar experimento
6. Generar informe
7. Salir

### Agregar un Experimento
- Ingresa el nombre del experimento
- Proporciona la fecha (formato DD/MM/YYYY)
- Selecciona el tipo (Química, Biología, Física)
- Ingresa al menos 3 resultados numéricos

### Análisis de Resultados
El sistema calcula automáticamente:
- Promedio de resultados
- Valor máximo
- Valor mínimo

### Comparación de Experimentos
Permite comparar múltiples experimentos mostrando:
- Tabla comparativa de métricas
- Identificación del mejor y peor desempeño
- Análisis estadístico comparativo

### Generación de Informes
Crea informes detallados en formato .txt que incluyen:
- Detalles de todos los experimentos
- Análisis estadísticos
- Resumen de resultados

## 🔍 Estructura del Código

### Clases Principales

#### `Experimento`
Representa un experimento individual con sus atributos:
- `nombre`: Nombre del experimento
- `fecha`: Fecha de realización
- `tipo`: Categoría del experimento
- `resultados`: Lista de resultados numéricos

#### `GestorExperimento`
Maneja la lógica principal del sistema:
- Gestión de experimentos
- Validaciones
- Análisis de datos
- Generación de informes

## 🔐 Validaciones Implementadas

- Formato de fecha válido (DD/MM/YYYY)
- Tipos de experimento permitidos
- Mínimo de 3 resultados por experimento
- Validación de datos numéricos
- Índices válidos para operaciones

## 📊 Ejemplo de Uso

```python
# Crear un nuevo experimento
gestor = GestorExperimento()
gestor.agregar_experimentos(
    nombre="Prueba pH",
    fecha="24/11/2024",
    tipo="Quimica",
    resultados=[7.2, 7.4, 7.1, 7.3]
)

# Analizar resultados
analisis = gestor.analizar_experimento(0)
print(f"Promedio: {analisis['promedio']}")
```

## 🤝 Contribución

1. Haz un Fork del proyecto
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Notas de la Versión

### Versión 1.0.0
- Implementación inicial del sistema
- Funcionalidades básicas de gestión de experimentos
- Sistema de análisis y comparación
- Generación de informes

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles.

## 👤 Autor

[Santiago Valencia Bedoya]
- GitHub: (https://github.com/zsanti11)


## ✨ Librerias

-Librerias usadas: Datetime, Prettytable
