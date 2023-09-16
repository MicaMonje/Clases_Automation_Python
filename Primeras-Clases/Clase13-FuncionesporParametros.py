#
def saludar():
    print("Hola, que tal?")

def salir():
    print("Nos vemos")

def suma(a,b):
    resultado= a+b
    print("La suma es: " + str(resultado))

saludar()
suma(5,6)
salir()

#--------------------
def datos (nom,ap,edad):
    print("Tu nombre es: {} {} {} " .format(nom,ap,edad))

datos("mica", "monje", "25")