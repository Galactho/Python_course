#! python

'''
Este modulo hará todas las operaciones necesarias para dar turnos en la farmacia
'''

def decorador(funcion):
    def wrapper(departamento):
        print('Su turno es:')
        turno = funcion(departamento)
        print(next(turno))
        print('Porfavor, espere hasta que le llamen')
    return wrapper

@decorador
def seleccionar_turno(departamento):
    '''
    Este metodo contiene los 3 metodos que generan un turno para cada departamento
    '''
            
    def turno_perfumeria():
        '''
        Este metodo dara un turno para el departamento de perfumeria
        '''
        x = 0
        while True:
            x += 1
            yield f'P - {x}'
  
    def turno_farmacia():
        '''
        Este metodo da un turno para el departamento de farmacia
        '''
        x = 0
        while True:
            x += 1
            yield f'F - {x}'
        
    def turno_cosmeticos():
        '''
        Este metodo da un turno para el departamento de cosmeticos
        '''
        x = 0
        while True:
            x += 1
            yield f'C - {x}'
    
    match departamento:
        case 'Perfumeria':
            return turno_perfumeria()
        case 'Farmacia':
            return turno_farmacia()
        case 'Cosmeticos':
            return turno_cosmeticos()


seleccionar_turno('Perfumeria')
decorador(seleccionar_turno('Perfumeria'))
