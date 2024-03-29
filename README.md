# **Proyecto Final - Coderhouse**
## Alumno: Franco Cazal

## Título del Proyecto: Blog Gastronómico

- Usuario Administrador (superuser): admin

- Contraseña: 1234

# Tecnología Utilizada

## FrontEnd
- HTML 5
- CSS 3
- Javascript
- Bootstrap

## BackEnd
- Python 3.11.4
- Django 5.0.2

### Obs: es necesario instalar Pillow (python -m pip install Pillow)

## Pruebas Realizadas

- La información pertinente a las pruebas se encuentra en el archivo "Casos de Prueba - Proyecto de Python CoderHouse.xlsx" el cual se encuentra en el presente repositorio.

## Video Demostración: https://drive.google.com/file/d/1QrOlxnozQpyRllP8gddqLGEiwCSKqS93/view?usp=sharing

## Diseño de la Página

Templates utilizados:

- Restoran de HTMLCodex: https://htmlcodex.com/bootstrap-restaurant-template/

- Symp de FreeCSS: https://www.free-css.com/free-css-templates/page235/symp

## Contenido de objetos de la aplicación

- Extraido del blog: https://micorazondearroz.com/

# Objetivo

- Simular una página web con estructura de blog en la cual se comparten recetas de comida y artículos gastronómicos.

# Modelos Usados (atributos): 
- Salada: usuario, título, tipo, ocasion, ingredientes, preparacion, fechaPublicacion, imagenRecetaSalada
- Dulce: usuario, título, tipo, ocasion, ingredientes, preparacion, fechaPublicacion, imagenRecetaDulce
- Bebida: usuario, título, tipo, ocasion, ingredientes, preparacion, fechaPublicacion, imagenRecetaBebida
- Articulo: usuario, título, subtitulo, contenido, fechaPublicacion, imagen

# **Indicaciones Generales:**

## **Nombre del proyecto:** 'proyecto'

## **Nombre de la aplicación:** 'aplicacion'

## **Tema de la aplicación:** Blog de Recetas de Comida y Artículos Gastronómicos

# **Funcionamiento de la aplicación: Nav-Bar**

### Al levantar el alojamiento de la página, la principal es 'home' (url vacío), la cual ofrece una visualización general de información sobre la misma.

### La página cuenta con una barra de navegación mediante la cual, si el usuario está autenticado, por medio de botones ubicados en la zona superior derecha de la misma, se puede acceder a las distintas funcionalidades que ofrece la aplicación.

### Cada botón da acceso a la visualización de una página, la primera sección 'Acerca del Sitio' redirige a una página en la cual se puede leer infromación acerca del blog, seguidamente con 'Recetas' se tienen los demás botones en fromato 'dropdown' que redirigen a páginas que contienen una lista de datos según los modelos establecidos pertinentes al tema escogido, los cuales son: Salada, Dulce y Bebida, a continuación se tiene el apartado 'Posts' en el cual se puede ver una lista de artículos publicados por los usuarios. Las páginas correspondientes a cada uno son accesibles por medio de la barra de navegación, en el orden descrito.

## - Login, Logout y Registro

### Contiguas a las secciones de las listas de objetos mencionados previamente, se encuentra la imagen de perfil (avatar) del usuario, tal que, clickeandola le redirige a un formulario mediante el cual puede cambiar su avatar, luego se tienen los botones 'Perfil' con el que se accede l perfil y la edición del mismo y 'Logout' con el que el usuario cierra sesión.

### Obs: si el usuario no está autenticado, entonces solo podrá ver los botones 'Login' para iniciar sesión y 'Registrarse' para crear un usuario, y no podrá acceder a ninguna página del sitio hasta que inicie sesión.

# **Funcionamiento de la aplicación: Cuerpo**

## - Función de Búsqueda:

### Bajando en la página se halla el botón de 'Explorar Recetas', donde al apretar el botón de la lupa se redirige a una página que realiza la función; se pide ingresar una cadena al usuario, luego de realizar la petición se redirige a otra página en la que se devuelven en forma de lista todos los objetos de todas las clases que contengan en el atributo 'titulo' una coincidencia con dicha cadena indiferentemente de su posición en la misma.

### El proceso es análogo para realizar una búsqueda de artículos, el cual se realiza desde el apartado 'Blog'.

## - Función de visualización de datos:

### Cada página que contiene la lista de objetos pertenecientes a sus respectivas clases es accesible por medio de su botón correspondiente en la barra de navegación de la página. Dentro de cada página se pueden visualizar los objetos almacenados en la base de datos conjuntamente con sus atributos.

## - Función de insertar datos:

### Dentro de cada página en la cual son visualizables los datos de cada clase, al hacer click en la imagen de uno se accede a una página donde se ven los detalles que componen al objeto, donde si el usuario creó ese objeto existe la opción 'añadir *objeto*' por medio de un botón con forma de cruz o 'más' que al presionarlo, redirige a un formulario por medio del cual es posible insertar datos en la base de datos de la aplicación. Luego de insertar un dato se redirige a la página correspondiente a la clase del dato insertado, donde se verifica que la lista fue actualizada.

## - Función de eliminar datos:

### Dentro de cada página en la cual son visualizables los datos de cada clase, al hacer click en la imagen de uno se accede a una página donde se ven los detalles que componen al objeto, donde si el usuario creó ese objeto existe la opción 'eliminar *objeto*' por medio de un ícono de un basurero que al presionarlo redirige a un formulario de confirmación de eliminación por medio del cual es posible eliminar el objeto en la base de datos de la aplicación. Luego de eliminar el objeto se redirige a la página correspondiente a la clase del dato eliminado, donde se verifica que la lista fue actualizada.

## - Volver al inicio

### Para volver al inicio de la aplicación simplemente hay que apretar en el título de la barra de navegación 8Blog Gastronómico', que se encuentra en la zona izquierda de la misma.

#### Si por alguna razón se desea acceder a la lista de objetos por medio de los urls en vez de los botones, se pueden consultar los mismos en el archivo de 'urls' en el código del proyecto.

# **Código de la aplicación**

## - views

### Cada función encargada de resolver las peticiones realizadas está clasificada por comentarios correspondientes a cada clase y ordenados en el siguiente orden: List - Create - Detail - Update - Delete. El método utilizado para la confección de las funciones del código es el de CBV o Class-Based Views, a excepción de las correspondientes a 'Create'.

## - urls

### Clasificados y ordenados de la misma forma que las funciones en views, con la misma excepción.

## - templates

### Cada función posee un template correspondiente y se encuentran nombrados según su función, empezando siempre por la función y seguida de la clase o acción; Ejemplo: listaSaladas o deleteBebida. El template 'pagina.html' se utiliza para ser base de herencia en los distintos apartados de la aplicación.
