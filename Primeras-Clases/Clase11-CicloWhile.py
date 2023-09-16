#While --> Ciclo en el cual se puede repetir cualquier cantidad de veces hasta que se cumpla la condicion
# inicio = 1
# fin = 10
#
# while (inicio <= fin):
#     print("se repite" + str(inicio))
#     inicio=inicio + 2

#While con un if y un breack
inicio = 1
fin = 100

while (inicio <= fin):
    inicio=inicio + 1
    if(inicio==5):
        break
    print("se repite" + str(inicio))