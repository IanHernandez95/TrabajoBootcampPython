
bodegaA = 0
bodegaB = 0

def envio(cantproductos):
    global bodegaA
    global bodegaB
    while True:
        try:
            tEnvio = int(input('¿Cual es la distancia del envio?: '))
            bodegaA = bodegaA + cantproductos
            bodegaB = bodegaB + cantproductos
            if tEnvio > 1000 and bodegaB < 500:
                tipodeenvio = 'Largo'
                bodegaA = bodegaA - cantproductos
                return tipodeenvio
            elif tEnvio > 1000 and bodegaB >= 500:
                print('No se puede Realizar el Envio, Bodega Llena')
                bodegaB = bodegaB - cantproductos
                bodegaA = bodegaA - cantproductos
            elif tEnvio <= 1000 and bodegaA < 500:
                tipodeenvio = 'Rapido'
                bodegaB = bodegaB - cantproductos
                return tipodeenvio
            elif tEnvio <= 1000 and bodegaA >= 500:
                print('No se puede Realizar el Envio, Bodega Llena')
                bodegaB = bodegaB - cantproductos
                bodegaA = bodegaA - cantproductos
        except:
            print('Debe ingresar un valor valido(solo numeros Enteros)')



