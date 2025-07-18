# Dashboard Librer\u00eda

Este proyecto es un panel de control b\u00e1sico desarrollado con **Django** para administrar libros, autores, categor\u00edas, stock y ventas de una librer\u00eda. Incluye una peque\u00f1a API para consultar algunos datos en formato JSON.

## Instalaci\u00f3n r\u00e1pida

1. Clona el repositorio y entra en la carpeta del proyecto:

   ```bash
   git clone <repo-url>
   cd dashboard-libreria
   ```
2. Crea un entorno virtual de Python y activa el entorno:

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa: env\Scripts\activate
   ```
3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Configuraci\u00f3n de variables de entorno

El archivo `dashboard/settings.py` define la conexi\u00f3n a la base de datos PostgreSQL y la `SECRET_KEY`. Puedes exportar variables de entorno antes de ejecutar el proyecto o modificar dicho archivo para que lea los valores que necesites.

Variables utilizadas:

- `SECRET_KEY` – clave secreta de Django.
- `DB_NAME` – nombre de la base de datos.
- `DB_USER` – usuario de la base de datos.
- `DB_PASSWORD` – contrase\u00f1a del usuario.
- `DB_HOST` – host de PostgreSQL (por defecto `localhost`).
- `DB_PORT` – puerto de PostgreSQL (por defecto `5432`).

Ejemplo en Linux/macOS:

```bash
export SECRET_KEY='cambia_esta_clave'
export DB_NAME='aca3_visualizacion'
export DB_USER='postgres'
export DB_PASSWORD='tu_clave'
export DB_HOST='localhost'
export DB_PORT='5432'
```

## Migraciones

Ejecuta las migraciones de Django para crear las tablas necesarias:

```bash
python manage.py migrate
```

## Carga del backup SQL

El repositorio incluye el archivo `backup_aca3_visualizacion.sql` con datos de ejemplo. Para restaurarlo en la base de datos (debe existir previamente), ejecuta:

```bash
psql -U $DB_USER -d $DB_NAME -f backup_aca3_visualizacion.sql
```

Aseg\u00farate de que el usuario y la base de datos coinciden con los valores de configuraci\u00f3n.

## Uso de la aplicaci\u00f3n

Inicia el servidor de desarrollo con:

```bash
python manage.py runserver
```

La interfaz web estar\u00e1 disponible en `http://127.0.0.1:8000/`.

### Endpoints de la API

- **`GET /api/libro_data/`** – Devuelve el listado de libros y el stock total por libro.
- **`GET /api/ventas_data/`** – Devuelve las ventas agregadas por fecha.

Ejemplo con `curl`:

```bash
curl http://127.0.0.1:8000/api/libro_data/
```

Ambos endpoints responden en JSON y se utilizan dentro del dashboard para actualizar tablas y gr\u00e1ficos de forma din\u00e1mica.

---

Con esto tendr\u00e1s el proyecto en funcionamiento junto con su base de datos de ejemplo y podr\u00e1s consumir la API interna que ofrece.
