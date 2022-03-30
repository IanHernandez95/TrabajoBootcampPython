from http import client
import S_Bodega as bodega
import S_Clientes as clientes
import S_Envio as envio


while True:
    print('\n----------------------------------------- \n  BIENVENIDO AL SISTEMA DE COMPRA/VENTA \n-----------------------------------------')
    print('\nPara acceder al sistema de Bodega, ingrese 1\nPara acceder al sistema de Registro de Clientes, ingrese 2\nPara acceder al sistema de Envios, ingrese 3')
    opcionmenu1 = input('Ingrese su opción: ')
    if opcionmenu1 == '1':
        print('\n-------------------------------------- \n  Usted Ingreso al sistema de bodega \n--------------------------------------')
        print('\nPara revisar el stock disponible, ingrese 1\nPara agregar productos al inventario, ingrese 2\nPara eliminar productos del invetario, ingrese 3\n'
        'Para sumar o restar stook de algun producto, ingrese 4\nPara Verificar si algun profucto tiene menos de 400 unidades en stock, ingrese 5')
        opcionmenu2 = input('Ingrese su opcion: ')
        if opcionmenu2 == '1':
            bodega.mostrapro()
            opseguir = input('Si desea hacer otra operacion ingrese si, si desea salir presione Enter: ').lower()
            if opseguir == 'si':
                continue
            else:
                print('Gracias por Operar con Nosotros')
                quit()
        elif opcionmenu2 == '2':
            bodega.agregarpro()
            opseguir = input('Si desea hacer otra operacion ingrese si, si desea salir presione Enter: ').lower()
            if opseguir == 'si':
                continue
            else:
                print('Gracias por Operar con Nosotros')
                quit()
        elif opcionmenu2 == '3':
            bodega.quitarpro()
            opseguir = input('Si desea hacer otra operacion ingrese si, si desea salir presione Enter: ').lower()
            if opseguir == 'si':
                continue
            else:
                print('Gracias por Operar con Nosotros')
                quit()
        elif opcionmenu2 == '4':
            bodega.sumrest()
            opseguir = input('Si desea hacer otra operacion ingrese si, si desea salir presione Enter: ').lower()
            if opseguir == 'si':
                continue
            else:
                print('Gracias por Operar con Nosotros')
                quit()
        elif opcionmenu2 == '5':
            bodega.verificarstock()
            opseguir = input('Si desea hacer otra operacion ingrese si, si desea salir presione Enter: ').lower()
            if opseguir == 'si':
                continue
            else:
                print('Gracias por Operar con Nosotros')
                quit()
        else:
            print('Ingrese una opcion valida')
    if opcionmenu1 == '2':
        print('\n---------------------------------------------------- \n  Usted Ingreso al sistema de Registro de clientes \n----------------------------------------------------')
        print('\nPara ver los nombres de los clientes registrados, ingrese 1\nPara agregar un cliente al registro, ingrese 2\nPara eliminar un cliente del registro, ingrese 3\n'
        'Para mostrar informacion de un cliente, ingrese 4')
        opcionmenu3 = input('Ingrese su opcion: ')
        if opcionmenu3 == '1':
            clientes.mostrarNombres()
            opseguir = input('Si desea hacer otra operacion ingrese si, si desea salir presione Enter: ').lower()
            if opseguir == 'si':
                continue
            else:
                print('Gracias por Operar con Nosotros')
                quit()
        elif opcionmenu3 == '2':
            clientes.clienteNuevo()
            opseguir = input('Si desea hacer otra operacion ingrese si, si desea salir presione Enter: ').lower()
            if opseguir == 'si':
                continue
            else:
                print('Gracias por Operar con Nosotros')
                quit()
        elif opcionmenu3 == '3':
            clientes.eliminarClientes()
            opseguir = input('Si desea hacer otra operacion ingrese si, si desea salir presione Enter: ').lower()
            if opseguir == 'si':
                continue
            else:
                print('Gracias por Operar con Nosotros')
                quit()
        elif opcionmenu3 == '4':
            clientes.mostrarInformacion()
            opseguir = input('Si desea hacer otra operacion ingrese si, si desea salir presione Enter: ').lower()
            if opseguir == 'si':
                continue
            else:
                print('Gracias por Operar con Nosotros')
                quit()
        else:
            print('Ingrese una opcion valida')
    if opcionmenu1 == '3':
        while True:
            comprador = clientes.comprador()
            pcomprado = bodega.comprar()
            tenvio = envio.envio(pcomprado[1])
            print(f'El cliente {comprador}, realizo la compra de {pcomprado[1]} unidades de {pcomprado[0]}, el tipo de envio sera {tenvio}')
            opseguir = input('Si desea hacer otra operacion ingrese si, si desea salir presione Enter: ').lower()
            if opseguir == 'si':
                break
            else:
                print('Gracias por Operar con Nosotros')
                quit()