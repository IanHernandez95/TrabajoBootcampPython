# TrabajoBootcampPython

SPRINT DE ENTREGA:
Se solicita como entregable de este Sprint la implementación final de todos los conceptos vistos durante
el Módulo 1: Python básico. Por tanto, se debe poner foco en lo siguiente:
Comentar debidamente el código para que sea comprensible por un tercero.
El programa tiene tres partes: manejo de bodega, información clientes y sistema de envío.
Cada parte debe entregarse en un script diferente.

MANEJO DE BODEGA

● Guarde la información de los productos en una bodega virtual.

● Los productos son vasos, cucharas, cuchillos y tenedores. Cada producto debe tener un stock
aleatorio entre 300 y 500 unidades y una descripción del producto.

● Debe definir funciones que puedan:

● Sumar y disminuir el número de unidades por producto.

● Agregar nuevos productos.

● Quitar productos de la bodega virtual.

● Mostrar todos los productos disponibles y su stock. Debe tener un desfase de un segundo entre
cada producto.

● Verificar si un producto tiene menos de 400 unidades y enviar una alerta.
Información clientes

INFORMACION DE CLIENTES

● Debe crear una base de datos que tenga información de clientes: ID, nombre, apellido, edad y
contraseña. Cree 4 clientes iniciales para probar el programa.

● Diseñe tres funciones:
- la primera debe agregar nuevos clientes,
- la segunda debe eliminar clientes según ID.
- la tercera debe mostrar toda la información por cliente.


SISTEMA DE ENVIO

● El sistema de envío debe ser un programa que pregunta qué tipo de envío es necesario (Rápido
o largo)

● Si es un envío a una distancia de más de 1.000 km es considerado largo. Si es igual o menor a la
distancia de 1.000 km es considerado rápido.

● En el caso que sea un envío rápido debe enviarse a una Bodega_A, caso contrario debe ser
almacenado a una Bodega_B.

● El programa debe verificar que cada bodega no supere las 500 unidades.