# Elegance

Elegance es un **market de maquillaje** desarrollado en Django. Esta aplicación permite a los usuarios explorar productos de maquillaje, con una interfaz amigable y funcionalidades que mejoran la experiencia.

## Características

- **Interfaz de usuario intuitiva**: Diseñada para facilitar la navegación y la compra de productos.
- **Gestión de productos**: Agregar, editar y eliminar productos fácilmente.
- **Base de datos SQLite**: Almacenamiento de datos de manera segura y eficiente.
- **Integración de formularios**: Uso de Django Crispy Forms para un manejo óptimo de los formularios.
- **Interfaz de administración personalizada**: Utiliza `django-admin-interface` para una administración más amigable.

## Tecnologías utilizadas

- **Django**: Framework web en Python.
- **SQLite**: Base de datos por defecto para desarrollo.
- **Pillow**: Para el manejo de imágenes.
- **Django REST Framework**: Para construir APIs RESTful.
- **Django PWA**: Para funcionalidades de aplicación web progresiva.
- **Bootstrap**: Framework CSS para un diseño moderno y responsivo.

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python 3.6 o superior
- Django 3.2.1
- Otras dependencias necesarias (se especifican en `requirements.txt`)

## Crdenciales admin

user: admin
pass: admin123

## Instalación

Sigue estos pasos para correr el proyecto localmente:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/tuusuario/elegance.git
   cd elegance
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver


