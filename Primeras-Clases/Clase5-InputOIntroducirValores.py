#Introducir Input
print("Cual es tu nombre: ")
nom= input()

#print("Tu nombre es: ")

print("Cual es tu ap: ")
ap= input()

print("Cual es tu edad: ")

eddString = input()
edd = int(eddString)

print("Dame el valor de a: ")
a = input()
a = int(a)


print("Dame el valor de b: ")
b = input()
b = int(b)
suma = a + b

print("Tu nombre es: {} {} {}".format(nom,ap,edd))
print("La suma de {} + {} es: {}".format(a,b,suma))