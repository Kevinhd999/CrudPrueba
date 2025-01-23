nino = {}
ninos = []
deportes = ""  
estrato = ""
##################################
def deportess():
    print (" Responda esta pregunta con un si o no")
    deporte = str(input("Juega algun deporte:")).lower()
    if deporte  == 'si':
        deportes = (str(input("Digite el deporte que juega el niño :")))
    elif deporte == 'no':
        deportes = ""
    elif deporte != 'si' or deporte != 'no':
        print ("escoja una opcion valida")
        deportess()
    return deportes


def estratos():
    print("Los tipos de estratos a escoger son: ")
    print("Responda la pregunta segun estas opciones")
    print("Alto - Medio - Bajo ")
    estrato = str(input("Digite el estrato del niño : ")).lower()
    if estrato == 'alto' or 'medio' or 'bajo':
        print(estrato)
    elif estrato != 'alto' or estrato != 'medio' or estrato != 'bajo':   
        print("Digite el estrato de manera correcta")
        estratos()
    return estrato


def crear():
    tarjeta_iden = int(input("Digite la tarjeta de identidad del niño "))
    nombre = str(input("Digite el nombre del niño: "))
    apellido = str(input("Digite el apellido del niño: "))
    estrato = estratos()
    deportes = deportess()
    edad = int(input("Digite la edad del niño: "))
    genero = str(input("Digite el genero del niño: "))

    ninos.append({  
            'tarjeta_identidad': tarjeta_iden,
            'nombre': nombre,
            'apellido': apellido,
            'estrato': estrato,
            'deporte': deportes,
            'edad': edad,
            'genero': genero
        })

def leer():
    if len(ninos) == 0:  
        print("No hay niños registrados.")
    else:
        for n in ninos:  
            print("\n Información del Niño ")
            print("Tarjeta de Identidad:", n['tarjeta_identidad'])
            print("Nombre:", n['nombre'])
            print("Apellido:", n['apellido'])
            print("Edad:", n['edad'])
            print("Estrato:", n['estrato'])
            print("Deporte:", n['deporte'])
            print("Genero:", n['genero'])
            print("\n")


def actualizar():
    if len(ninos) == 0:  
        print("No hay niños registrados.")
        return
    tarjeta_iden = int(input("Digite la tarjeta del niño que desea modificar "))
    for n in ninos:
        if n ['tarjeta_identidad'] == tarjeta_iden:
            print("Niño encontrado ahora modifique la informacion")
            n ["Nombre"] = str(input("Digite de nuevo el nombre: "))
            n ["Apellido"] = str(input("Digite de nuevo apellido: "))
            n ["Estrato"] = estratos()
            n ["Deporte"] = deportess()
            n ["Edad"] = int(input("Digite de nuevo la edad: "))
            n ["Genero"] = str(input("Digite de nuevo el genero: "))
            print("Niño modificado")
        else :
            print("No se encontro niño")

def eliminar():
    if len(ninos) == 0:  
        print("No se encontró a ningun niño.")
        return
    tarjeta_iden = int(input("Digite la tarjeta de identidad del niño que desea eliminar: "))
    for n in ninos:
        if n['tarjeta_identidad'] == tarjeta_iden:
            ninos.remove(n)
            print(f"Niño con tarjeta de identidad {tarjeta_iden} eliminado exitosamente.")
        else:
            print("No se encontró un niño con esa tarjeta de identidad.")

#Menu#

while True:
    print ("--------------------------------------------")
    print ("Menu:")
    print ("Escoja de manera correcta")
    print ("1. Registrar Niño")
    print ("2. Listar Niños")
    print ("3. Actualizar Niño")
    print ("4. Eliminar Niño")
    print ("5. Salir")
    opcion = int(input("Escoja una opcion: "))
    if opcion == 1:
        crear()
    elif opcion == 2:
        leer()
    elif opcion == 3:
        actualizar()
    elif opcion == 4:
        eliminar()
    elif opcion == 5:
        print("Fin del programa")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción correcta.")
