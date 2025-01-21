##################################

def deportess():
    deporte = str(input("Juega algun deporte :"))
    print ("Responda si o no")
    if deporte  == 'si':
        deportes =(str(input("Digite el deporte que juega el niño :")))



def estratos():
    print("Digite el estrato de manera correcta")
    print("Los tipos de estratos a escoger son : ")
    print("Alto - Medio - Bajo")
    estrato = str(input("Digite el estrato del niño :"))



####################################

nombre = str(input("Digite el nombre del niño :"))

estrato = str(input("Digite el estrato del niño Alto - Medio - Bajo:"))


if estrato == 'Alto' or 'Medio' or 'Bajo':
    print("")
elif estrato != 'Alto' or estrato != 'Medio' or estrato != 'Bajo':   
    estratos()

print ("Responda si o no")
deporte = str(input("Juega algun deporte :"))


if deporte  == 'si':
    deportes =(str(input("Digite el deporte que juega el niño :")))
elif deporte != 'si' or deporte != 'no':
    print ("escoja una opcion valida")
    deportess()


edad = int(input("Digite la edad del niño :"))

genero = str(input("Digite el genero del niño :"))

print("----------------------------------")
print("")
print(nombre)
print(estrato)
print(deportes)
print(edad)
print(genero)
print("")
print("----------------------------------")



