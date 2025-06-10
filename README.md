# Laboratorio de Análisis de Datos

Este proyecto permite cargar, limpiar, analizar y guardar datasets en formato CSV o Excel en una base de datos MySQL de manera automatizada.

## Estructura del Proyecto

```
laboratorio_1
├── data/
│   └── data_saver.py         # Clase para guardar DataFrames en la base de datos
├── domain/
│   ├── dataset.py            # Clase abstracta base para datasets
│   ├── dataset_csv.py        # Implementación para archivos CSV
│   └── dataset_excel.py      # Implementación para archivos Excel
├── files/                    # Carpeta donde colocar los archivos CSV/Excel a procesar
├── main.py                   # Script principal de ejecución
├── requirements.txt          # Archivo con dependencias necesarias
└── README.md                 # Este archivo
```

## Requisitos

- Python 3.8+
- MySQL
- Paquetes Python:
  - pandas
  - sqlalchemy
  - pymysql
  - python-decouple

Instala los requisitos con:

```bash
pip install -r requirements.txt
```

## Configuración

Crea un archivo `.env` en la raíz del proyecto con los siguientes datos de conexión:

```
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_NAME=nombre_base_de_datos
DB_PORT=3306
```

## Uso

1. Coloca tus archivos `.csv` o `.xlsx` en la carpeta `files/`.
2. Ejecuta el script principal:

```bash
python main.py
```

El programa:
- Detecta automáticamente los archivos en la carpeta `files/`.
- Carga y limpia los datos (elimina duplicados, estandariza nombres de columnas, etc.).
- Muestra un reporte básico del DataFrame.
- Guarda los datos en la base de datos MySQL, creando una tabla por archivo.

## Funcionalidades principales

- **Carga automática** de archivos CSV y Excel.
- **Limpieza de datos**: elimina duplicados, estandariza nombres de columnas y valores de texto.
- **Reporte**: muestra estadísticas y datos faltantes.
- **Persistencia**: guarda los datos limpios en una base de datos MySQL.
- **Extensible**: puedes agregar nuevas fuentes de datos creando nuevas clases que hereden de `Dataset`.

## Personalización

Puedes extender la limpieza de datos o agregar nuevas funciones en `domain/dataset.py`.


---

Desarrollado para el Informatorio 2025.