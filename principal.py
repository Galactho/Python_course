import numeros

def validacion():
    print('*' * 25)
    print('BIENVENIDO A LA FARMACIA')
    print('*' * 25)
    while True:
        print('''
        [P] - Perfumeria
        [F] - Farmacia
        [C] - Cosmeticos
        ''')
        try:
            opcion = input('¿A cuál departamento desea ingresar? ').upper()
            ['P','F','C'].index(opcion)
        except ValueError:
            print('Opción no válida, intente de nuevo')
        else:
            break
    numeros.decorador(opcion)

def inicio():
    while True:
        validacion()
        try:
            turno = input('¿Desea otro turno? [S] [N] ').upper()
            ['S','N'].index(turno)
        except ValueError:
            print('Opcion no valida, intente de nuevo')
        else:
            if turno == 'N':
                print('Gracias por su visita, vuelva pronto')
                break
inicio()