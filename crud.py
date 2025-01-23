nino = {}
ninos = []
##################################
def deportess():
    print (" si o no")
    deporte = str(input("Juega algun deporte :")).lower()
    if deporte  == 'si':
        deportes = (str(input("Digite el deporte que juega el niño :")))
    elif deporte != 'si' or deporte != 'no':
        print ("escoja una opcion valida")
        deportess()


def estratos():
    print("Los tipos de estratos a escoger son: ")
    print("Alto - Medio - Bajo ")
    estrato = str(input("Digite el estrato del niño : ")).lower()
    if estrato == 'alto' or 'medio' or 'bajo':
        print(estrato)
    elif estrato != 'alto' or estrato != 'medio' or estrato != 'bajo':   
        print("Digite el estrato de manera correcta")
        estratos()


def crear():
    tarjeta_iden = int(input("Digite la tarjeta de identidad del niño "))
    nombre = str(input("Digite el nombre del niño: "))
    apellido = str(input("Digite el apellido del niño: "))
    estratos()
    deportess()
    edad = int(input("Digite la edad del niño: "))
    genero = str(input("Digite el genero del niño: "))

    nino[tarjeta_iden] = {
            'tarjeta_identidad': tarjeta_iden,
            'nombre': nombre,
            'apellido': apellido,
            'estrato': estrato,
            'deporte': deportes,
            'edad': edad,
            'genero': genero
        }

def leer():
    ninos.append({nino})
    for n in ninos:
        print(ninos.values())

#Menu#

while True:
    print ("--------------------------------------------")
    print ("Menu:")
    print ("Escoja de manera correcta")
    print ("1. Registrar Niño")
    print ("2. Listar Niños")
    print ("3. Salir")
    opcion = int(input("Escoja una opcion: "))
    if opcion == 1:
        crear()
    if opcion == 2:
        leer()
    if opcion == 3:
        break