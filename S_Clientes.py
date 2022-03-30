#Dict Clientes
clientes = {
    1 : ['Ian','Hernandez',27,'Contraseña1'],
    2 : ['Felipe', 'Godoy', 28,'Contraseña2'],
    3 : ['Camila','Pedraza',29,'Contraseña3'],
    4 : ['Anibal','Reinoso',30,'Contraseña4']
}
#Funciones
#Agregar clientes nuevos
def clienteNuevo():
    nClienteN=input('Ingrese su nombre: ').title()
    aClienteN=input('Ingrese su Apellido: ').title()
    eClienteN=input('Ingrese su Edad: ')
    ejecutar = True
    while ejecutar:
        inputContraseña=input('Ingrese su contraseña: ')
        cClienteN = verificarContraseña(inputContraseña)
        if cClienteN is not None:
            idAutomatico=max(list(clientes.keys()))+1
            clientes[idAutomatico] = [nClienteN,aClienteN,eClienteN,cClienteN]
            print(f'El/la cliente {nClienteN} {aClienteN} a sido registrado/a correctamente')
            ejecutar = False
        else:
            continue
#Verificar Contraseña
def verificarContraseña(contraseña):
    contraVeridic = True
    if len(contraseña) < 8: 
        print('La contraseña debe tener al menos 8 digitos') 
        contraVeridic = False
    if not any(char.isdigit() for char in contraseña): 
        print('La contraseña debe tener al menos 1 numero') 
        contraVeridic = False
    if not any(char.isupper() for char in contraseña): 
        print('La contraseña deberia tener al menos una Mayuscula') 
        contraVeridic = False
    if not any(char.islower() for char in contraseña): 
        print('La contraseña deberia tener al menos 1 minuscula') 
        contraVeridic = False
    if contraVeridic: 
        print('Contraseña Valida')
        return contraseña
#Eliminar Clientes por ID
def eliminarClientes():
    while True:
        try:
            eCliente = int(input('Ingrese ID del cliente a Eliminar: '))
            if eCliente in clientes.keys():
                del clientes[eCliente]
                break
            else:
                print('ID del Cliente no Registrado')
        except ValueError:
            print('Solo debe ingresar numeros enteros')
#Mostrar informacion por cliente
def mostrarInformacion():
    while True:
        try:
            iCliente = int(input('Ingrese ID del cliente a consultar informacion: '))
            if iCliente in clientes.keys():
                print(f'El cliente con el ID {iCliente} se llama {clientes[iCliente][0]} {clientes[iCliente][1]}, tiene {clientes[iCliente][2]} años y su contraseña es {clientes[iCliente][3]}')
                consultaOtroID = input('Si desea consultar por otro clientes ingrese si, de lo contrario presione enter').lower()
                if consultaOtroID =='si':
                    continue
                else:
                    break
            else:
                print('ID del Cliente no Registrado')
        except ValueError:
            print('Solo debe ingresar numeros enteros')
#mostrar solo nombres de los clientes registrados
def mostrarNombres():
    listaclientes = list(clientes.values())
    print('Los nombres de los Clientes registrados son:')
    for i in listaclientes:
        print(i[0])
#Comprobar Contraseña ingresada
def comprador():
    while True:
        try:
            idcomprador = int(input('Ingrese ID del cliente que compra: '))
            if idcomprador in clientes.keys():
                datosuser = clientes[idcomprador]
                cComprador = input('Ingrese contraseña del comprador: ')
                if cComprador == datosuser[3]:
                    return datosuser[0]
                else:
                    print('Contraseña Incorrecta')
                    continue
            else:
                print('ID del cliente no registrado')
        except ValueError:
            print('Ingrese solo numeros Enteros')


