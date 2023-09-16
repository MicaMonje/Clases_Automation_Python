#Introduccion a las variables

a: int = 100
b = 50

suma=a + b
resta=a-b

multiplicacion=a * b
division=a/b

print("la suma es: " + str(suma))
print("la resta es: " + str(resta))
print("la multiplicacion es: " + str(multiplicacion))
print("la division es: " + str(division))

Nombre="Micaela"
Ap="Monje"

print("Mi nombre es: " +Nombre + " " +Ap)
print("--------------------------------")
print("FUNCIONES EJEMPLO")

#la declaracion
def lavaplatos():
    print("Lavar los platos jefe")

#el llamado
lavaplatos()

def cuantoPlatosLava(numero:int):
    if (numero <= 10):
        print("Si puedo lavar")
    else:
        print("No puedo lavar")

cuantoPlatosLava(11)

print("--------------------------------")


def sumar(a , b):
    resultado = a + b
    return resultado


# sumar(20,20)
print("la suma es: " + str(sumar(65,10)))