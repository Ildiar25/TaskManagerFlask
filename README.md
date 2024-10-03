
# Gestor de Tareas

---

---

En este ejercicio guiado vamos a crear un *servidor*, desplegar en él un
**gestor de tareas** y conectarlo a una *base de datos* para almacenar, editar y
eliminar elementos mediante consultas *SQL*.

El objetivo de este ejercicio es observar la comunicación entre el *front-end* y el
*back-end* en lenguaje **Python** utilizando la librería **Flask** y **SQL Alchemy**.

Una vez desplegado el servidor en la dirección y puerto ***localhost:5000***, el usuario
deberá encontrar una *interfaz visual* que le permita realizar las siguientes acciones.

---

### ///// Contenido Obligatorio /////
- **Crear:** Añadir una nueva tarea a la base de datos
- **Marcar:** Cambiar el estado de una tarea de 'incompleta' a 'completa' y viceversa
- **Eliminar:** Quitar dicha tarea de la base de datos



### ///// Contenido Optativo /////
- **Editar:** Posibilidad de editar la tarea
- **Mejorar:** Se da la opción de poder mejorar la interfaz visual
- **Categorizar:** Se puede añadir un campo para incluir una categoría
- **Fecha límite**: Que la tarea deba estar cumplida antes de la fecha límite (7 días)

---

**NOTA:** *Todo el trabajo en código se ha realizado en inglés para poner en práctica el
desarrollo en dicho idioma.*

---

<p style="text-align:center"> * * * * * * </p>


## Estructura del proyecto
¿Qué estructura deberá tener esta aplicación?
En esta ocasión

- `database/database.db:` Almacena la base de datos donde se sincronizan las tareas.
- `static/... :` Las imágenes usadas en nuestra web.
  - `database/images/... :` Guarda todas las imágenes utilizadas en el archivo _README_.
  - `static/main.css:` Contiene los estilos propios para nuestros documentos _HTML_.
  - `static/reminder-icon.ico:` Icono de pestaña.
- `templates/... :` Almacena todas y cada una de las páginas web necesarias.
  - `templates/index.html:` Página web principal, conocida como 'home'.
  - `templates/update_task.html:` Página web que se encarga de la edición de la tarea.
- `db.py:` Creación y configuración de la base de datos. 
- `main.py:` Crea el servidor y contiene todos sus usos. También conocido como 'back-end'.
- `models.py:` Almacena las clases necesarias de dicho proyecto, en este caso la clase `Task`.
- `README.md:` Este documento.
- `requirements.txt:` Registro de versiones del stack technológico necesario para usar el programa.

---

***Estructura del directorio principal:***

![Espacio de trabajo completo](/static/images/tree-structure.png "Directorio Principal")

---

<p style="text-align:center"> * * * * * * </p>

## Principales Casos de Uso

- **Crear tarea:**

Esta característica se encargará de pedir al usuario que ingrese un **valor obligatorio**.
Cuando el usuario pulse el botón ***'guardar'***, el HTML se encargará de enviar dicha
información al ***back-end*** donde se procesará y posteriormente se almacenará en la
base de datos mediante una consulta ***SQL***.

---

***Agregar tarea 'Regar las plantas':***

![Creación de una nueva tarea 'regar las plantas'](/static/images/add-example.png "Añadir tarea")
> El usuario escribe la tarea a guardar y selecciona su categoría.

***Comprobación en Base de Datos:***

![Comprobar si 'regar las plantas' se encuentra en la base de datos](/static/images/update-example-02.png "Revisión en base de datos")
> Aparece dicha tarea en la base de datos ya almacenada.

---

- **Marcar tarea:**

Esta característica permite al usuario marcar una tarea como realizada.
Cuando el usuario pulse sobre el símbolo **check**, un 'enlace' se comunicará con el 
***back-end*** enviando como dato el id de la tarea pulsada.
Una vez en la función **'task_complete(task_id)'**, se realizará una búsqueda en la
base de datos con el ID proporcionado, se modificará el atributo _'complete'_ cambiando
su valor por el contrario (es de tipo booleano), se guaradrá dicho cambio y devolverá al
usuario a nuestra página principal.

---

***Check a la tarea 'Reunión a las 18:00':***

![Marcando como completa la tarea 'Reunión a las 18:00'](/static/images/update-example-01.png "Completar Tarea")
> Como se puede observar, se reordenan las tareas dejando al final las tareas completadas.

***Comprobación en Base de Datos:***

![Comprobar si 'Reunión a las 18:00' se encuentra completada](/static/images/update-example-02.png "Revisión en base de datos")
> Se puede observar que el valor de dicha tarea a cambiado a '1'.

---

- **Modificar tarea:**

Para su modificación, cuando el usuario pulse sobre el lápiz azul se cargará en
pantalla otra plantilla _HTML_ llamada **'update_task.html'**.
Dicha plantilla contiene un formulario donde el usuario puede o no rellenar el
contenido y cambiar la categoría. Dicha acción actualizará la fecha de creación
de la tarea. Cabe señalar que dicho _HTML_ cargará la información de la
tarea en cuestión.
Una vez pulse el botón ***'confirmar'***, se enviarán todos los datos del formulario
al **back-end** donde la función **'updated(task_id)'** realizará las siguientes acciones:
> - Buscar en la base de datos la tarea a modificar con el ID proporcionado.
> - Proporcionar la fecha de modificación actual.
> - Realizar un control de flujo para saber si el usuario a introducido un valor en el campo 'Modificación'.
> - Actualizar los datos asociados al ID proporcionado.
> - Guardar los cambios
> - Volver a la página principal 'home'.

---

***Revisión de la tarea 'Odiar CSS':***

![Muestra la lista de tareas](/static/images/task-editor-example-01.png "Lista de tareas disponibles")
> Al lado derecho de la tarea 'Odiar CSS' pulsamos el botón azul o 'lápiz'.

***Comprobamos en la base de datos su categoría:***

![Muestra de la categoría 'Odiar CSS'](/static/images/task-editor-example-02.png "Base de datos")
> Como se puede observar, la categoría de dicha tarea es 'Hogar'. Vamos a comprobar si en
> la edición podemos ver su categoría.

***Cambiemos la categoría de la tarea 'Odiar CSS':***

![Muestra de la categoría 'Odiar CSS'](/static/images/task-editor-example-03.png "Editor de tareas")
> Como se puede observar, al editar una tarea podemos ver que su categoría es 'Hogar'.
> Le cambiamos la categoría a 'Estudios' y confirmamos.

***Comprobación en Base de Datos:***

![Comprobar que la categoría de la tarea es 'Estudios'](/static/images/task-editor-example-04.png "Revisión en base de datos")
> Se puede observar que la categoría de dicha tarea a cambiado a 'Estudios'.

---

- **Eliminar tarea:**

Para eliminar una tarea, el usuario deberá pulsar la papelera naranja a la derecha de la
tarea que desea eliminar. Dicha acción enviará a la función **'delete_task(task_id)'**
el ID de la tarea seleccionada. Esta función realizará un filtrado a la base de datos
para seleccionar dicha tarea, la eliminará y guardará los cambios. Por último,
redireccionará al usuario a la página web 'home'.

---

***Revisión la lista de las tareas:***

![Muestra la lista de tareas](/static/images/task-manager-example-01.png "Lista de tareas disponibles")
> Al lado derecho de las tareas podemos ver el icono naranja de la papelera.

***Comprobamos en la base de datos dicho listado:***

![Muestra la base de datos completa](/static/images/database-01.png "Base de datos")
> Confirmamos la cantidad total.

***Eliminemos unas cuantas tareas:***

![Eliminación de unas cuantas tareas](/static/images/delete-example-01.png "Eliminación de tareas")
> Como se puede observar, al eliminar una tarea, la web se actualiza mostrando únicamente
> las tareas restantes.

***Comprobación en Base de Datos:***

![Comprobar que las tareas se han eliminado](/static/images/database-delete-example.png "Revisión en base de datos")
> Se confirma que la cantidad de tareas totales ha disminuido.

---

- **Categorizar:**

Para categorizar una tarea, tan solo habrá que desplegar el menú en la creación 
de una tarea o simplemente dándole al botón **'modificar'**.
Dicha acción rellenará automáticamente el atributo _'category'_ de nuestra clase 
**'Task'**.

---

***Menú desplegable 'Categorías':***

![Muestra la lista de categorías](/static/images/category-example.png "Lista de categorías disponibles")
> Desplegando el menú el usuario podrá elegir a qué categoría quiere asignar la tarea.

***Ejemplo de 'Categorías' en la base de datos:***

![Muestra la lista de categorías en la base de datos](/static/images/database-01.png "Categorías almacenadas")
> Podemos ver que cada tarea tiene una categoría asignada.

---

- **Fecha límite:**

En esta aplicación la fecha límite se marcará con un icono rojo de aviso en el lado
izquierdo de la misma. Por defecto, dicho icono no aparecerá hasta pasados 7 días
desde la creación de la tarea. El único modo de eliminar dicho icono es modificando
la tarea, pues automáticamente se actualizará su fecha de creación.

---

***Comprobemos la lista de tareas:***

![Muestra la lista de tareas](/static/images/task-manager-example-01.png "Lista de tareas disponibles")
> Como podemos observar, ninguna de las tareas actuales tiene el icono de aviso.

***Comprobamos en la base de datos sus fechas:***

![Muestra la base de datos completa](/static/images/database-01.png "Base de datos")
> Cada tarea tiene asignada una fecha de creación.

***Avancemos en el tiempo:***

![Muestra la base de datos completa](/static/images/due-time-example.png "Base de datos")
> Modificando la variable **'due_time'** podemos observar como aparece el icono según
> la fecha almacenada.

---

<p style="text-align:center"> * * * * * * </p>

## Guía de Instalación

Antes de realizar el testeo de la aplicación, se deberá tener en cuenta los siguientes
requisitos. Para ello se muestran a continuación todas las librerías utilizadas
y el lenguaje principal de programación.

---

### Stack Tecnológico Principal

- **Python:** Como lenguaje de programación principal
- **Flask:** Como framework para web
- **SQLite:** Como lenguaje de la base de datos
- **Jinja:** Como motor de renderizado para web

### Stack Tecnológico Secundario

- **Pycharm:** Como IDE de programación
- **Virtualenvi**: Como entorno virtual
- **SQLAlchemy**: Módulo de _Python_ para comunicar la base de datos con la programación
- **Google Fonts**: Para el estilo web
- **UIGradients**: Para generar degradados de color en _CSS_
- **Bootstrap**: Librería de componentes gráficos y temas

### Preparación del entorno

1. Asegúrate de tener instalado ***Python*** en tu equipo. Puedes descargarlo
desde [aquí](https://www.python.org/downloads/).
2. Copia o descarga el repositorio del proyecto.
3. Ve al directorio principal del proyecto y crea un nuevo entorno virtual
con el siguiente comando: `py -m venv .venv`.
4. Actívalo usando `.venv\Scripts\activate`.
5. Ahora instala las dependencias necesarias mediante el archivo **requirements.txt**
usando el comando `pip install –r requirements.txt`.
6. Una vez finalizado todo el proceso, ya se puede iniciar el archivo `main.py`:

```bash
py main.py
```

**NOTA TÉCNICA:** *Para visualizar la aplicación, abrir el navegador y entrar a la
siguiente dirección web: **localhost:5000**. Si deseas cerrar la aplicación, deberás
de seleccionar el terminal abierto en tu IDE y pulsar **'Ctrl + C'**.*


## Créditos finales

Autor: ***Joan Pastor Vicéns***

[Mi Github](https://github.com/Ildiar25) ~~~~~
[Mi LinkedIn](https://www.linkedin.com/in/joan-pastor-vicens-aa5b4a55)
