def turno_perfumeria():
    '''
    Este metodo dara un turno para el departamento de perfumeria
    '''
    for n in range(1,100):
        yield f'P - {n}'

def turno_farmacia():
    '''
    Este metodo dara un turno para el departamento de farmacia
    '''
    for n in range(1,100):
        yield f'F - {n}'

def turno_cosmeticos():
    '''
    Este metodo dara un turno para el departamento de cosmeticos
    '''
    for n in range(1,100):
        yield f'C - {n}'

p = turno_perfumeria()
f = turno_farmacia()
c = turno_cosmeticos()

def decorador(departamento):
    print('*' * 20)
    print('Su turno es:')
    match departamento:
        case 'P':
            print(next(p))
        case 'F':
            print(next(f))
        case 'C':
            print(next(c))
    print('Porfavor, espere hasta que le llamen')
    print('*' * 20)
