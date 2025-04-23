# Descripcion general

Con el requerimiento de la inclusion de una base de datos para 
la aplicacion, se tuvo que cambiar la estructura general del proyecto
para seguir el patron MVC (Modelo-vista-controlador).

## Patron MVC

En la carpeta __src__ esta ubicado el core de la aplicacion, y este core
esta divido en tres subcarpetas:

- __model__: En esta carpeta estan ubicados todas las clases que interatuaran
con la base de datos y la representacion de las tablas.

- __view__: Aqui estara ubicado todo la logica para UI de la aplicacion de estritorio.

- __controller__: Aquie esta ubicada, la logica para mediar entre la vista y el modelo.


### Model
Esta carpeta esta subdivida en varias carpetas, que son las siguientes:

- __client__: Se encuentra todo la representacion de un cliente
- __order__: Se encuentra todo la representacion de los pedidos
- __product__: Se encuentra todo la representacion de los productos
- __production__: se encuentra toda la representacion de la producion, es decir
en esta carpeta se guarda todo la informacion relacionada con el inventario disponibles
de productos de la empresa
- __seller__: Se encuentra la representacion de un vendedor.




__Nota__:Al momento de escribir esta seccion el resto de secciones, estan sin implementar.


### View
Sin implementar por el momento

### Controller
Sin implementar por el momento

