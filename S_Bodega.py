import random
import time
#variables random de stock
ramstock = random.randint(300,500)

#Dict de stocks
stocks = {
    'vasos':ramstock,
    'cucharas':ramstock,
    'cuchillos':ramstock,
    'tenedores': ramstock
}

#Funcion para Modificar Stock de la Bodega Virtual
def sumrest():
    while True:
        op = input("Si desea restar un producto ingrese'restar',\nSi desea sumar ingrese 'sumar': ").lower()
        if op == "restar":
            rpro = input("Cuál producto desea restar?: ").lower()
            if rpro in stocks.keys():
                rcant = int(input('Ingrese Cantidad a Restar del stock: '))
                stocks[rpro] = stocks[rpro] - rcant
                print(stocks[rpro])
                break
        elif op == 'sumar':
            spro = input("Cuál producto desea sumar?: ").lower()
            if spro in stocks.keys():
                scant = int(input('Ingrese Cantidad a Sumar al stock: '))
                stocks[spro] = stocks[spro] + scant
                print(stocks[spro])
                break
        else:
            print('Ingrese opcion valida')

#Funcion para Agregar Elemento de la Bodega Virtual
def agregarpro():
    npro = input('Ingrese nommbre del nuevo producto: ')
    stocks[npro] = ramstock
    print(stocks)

#Funcion para Quitar Elemento de la Bodega Virtual
def quitarpro():
    while True:
        qpro = input('Ingrese nombre del producto a quitar: ')
        if qpro in stocks.keys():
            del stocks[qpro]
            print(stocks)
            break
        else:
            print('Ingrese una opción valida')

#Funcion para mostrar items de dict stock
def mostrapro():
    for i in stocks.items():
        print(i)
        time.sleep(1)

#Funcion para Verificar Stock Menor a 400
def verificarstock():
    while True:
        vpro = input('Ingrese nombre del producto a veridicar su stock: ')
        if vpro in stocks.keys() and stocks[vpro] < 400:
            print(f'Hay en existencia menos de 400 unidades de {vpro}')
            break
        elif vpro in stocks.keys() and stocks[vpro] >= 400:
            print(f'Hay en existencias 400 o más unidades de {vpro}')
            break
        else:
            print('Ingrese una opcion Valida')

#Funcion para comprar
def comprar():
    while True:        
        productoComprado = input('Ingrese el nombre del producto a comprar: ').lower()
        if productoComprado in stocks.keys():
            pcompr = stocks[productoComprado]
            try:
                cantproducto = int(input('Ingreses la cantidad de productos a comprar: '))
                if cantproducto > pcompr:
                    print(f'Stock insuficiente para realizar la compra, ingrese un monto menor a {pcompr}')
                else:
                    return [productoComprado,cantproducto]
            except ValueError:
                print('Ingrese un numero entero')
        else:
            print('Producto no Registrado')

