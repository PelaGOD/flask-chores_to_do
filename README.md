# Flask Chores To Do

## Descripción

Este proyecto es una aplicación web creada con **Flask** para gestionar tareas pendientes (chores). Utiliza **Firestore** como base de datos para almacenar y administrar las tareas de manera eficiente. La aplicación te permite agregar, actualizar y eliminar tareas, ofreciendo una interfaz intuitiva y sencilla para organizar tus pendientes.

## Instalación

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/usuario/flask-chores-todo.git
2. Navega al directorio del proyecto:
   ```bash
   cd flask-chores-todo
3. Instala las dependencias necesarias ejecutando el siguiente comando:
   ```bash
   pip install -r requirements.txt
4. Configura las variables de entorno necesarias para Firestore en un archivo .env:
   ```bash
   FIRESTORE_PROJECT_ID=tu_proyecto_id
5. Ejecuta la aplicación localmente:
   ```bash
   flask run

## Uso
1. Accede a la aplicación desde tu navegador en http://127.0.0.1:5000.
2. Agrega nuevas tareas, actualiza el estado de las existentes o elimínalas a medida que las completes.

## Tecnologías utilizadas
* Flask: Framework web en Python.
* Firestore: Base de datos NoSQL de Google Firebase.
* Python: Lenguaje de programación.
