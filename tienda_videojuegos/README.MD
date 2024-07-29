# Tienda de Videojuegos
Esta aplicación web, desarrollada con Django, permite gestionar venta de Accesorios, Juegos y Consolas. Implementa el patrón MVT (Model-View-Template) y está diseñada para ser un sistema básico para agregar, buscar y listar Accesorios, Juegos y Consolas con su precio y caracteristicas.
## Requisitos
- Python 3.12.4
- Django 4.2

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/genji015/pagina-juegos/tree/master/tienda_videojuegos/tienda
    cd tienda_videojuegos
    ```

2. Crea el entorno virtual e instala las dependencias:
    ```bash
    pipenv install
    pipenv shell
    ```

3. Realiza las migraciones:
    ```bash
    python manage.py migrate
    ```
### Crea un Superusuario (Opcional)
Para acceder al panel de administración de Django, crea un superusuario con el siguiente comando:
```bash
python manage.py createsuperuser
```
Sigue las instrucciones para ingresar el nombre de usuario, correo electrónico y contraseña.

4. Ejecuta el servidor:
    ```bash
    python manage.py runserver
    ```

## Funcionalidades

- **Agregar Videojuego**: `/agregar_videojuego/`: Agrega un videojuego con su nombre precio y descripcion.
- **Agregar Consola**: `/agregar_consola/`: Agrega una consola con su nombre(modelo), marca y precio.
- **Agregar Accesorio**: `/agregar_accesorio/`:Agrega un accesorio con su nombre, tipo (joystick,memorcard, auriculares etc) y su precio
- **Buscar**: Un buscador en la BD sobre productos ingresados.

## Estructura del Proyecto
- **tienda_videojuegos/**: Directorio del proyecto principal.
  - `settings.py`: Configuración del proyecto Django.
  - `urls.py`: Rutas del proyecto.
  - `wsgi.py`: Punto de entrada WSGI para servidores de aplicaciones.
- **tienda/**: Aplicación dentro del proyecto.
  - `models.py`: Definición de los modelos (Accesorios, Consolas, Juegos).
  - `views.py`: Definición de las vistas (funcionalidades).
  - `forms.py`: Formularios para la entrada de datos.
  - `templates/`: Plantillas HTML.
  - `urls.py`: Rutas específicas de la aplicación.

