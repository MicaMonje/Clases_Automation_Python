#Ciclo sin array. "in"--> recorre dentro de..//
# for x in range(11):
#     print("tonta" + str(x))
#
#
# #Ciclo con array
# nombre =["pepe", "manuel", "anto", "pato", "emi"]
# for name in nombre:
#     print(name)
#
# #Ciclo con cadena de texto
#
# nom = "gatito gordo de peluche"
# for nr in nom:
#     print(nr)
# #---------------------------------------
# #Indicamos desde que posicion(10) hasta que posicion(20) se debe ejecutar
# for x in range(10,20):
#     print(x)
#
# #Indicamos desde que posicion(10) hasta que posicion(20) se debe ejecutar con incremento(de 5 en 5)
# for num in range(10,200,5):
#     print(num)
#
# #Utilizamos un if y un "break"--> este se usa para parar o romper un proceso con condiciones especificadas en el if
# for nu in range(0,100,7):
#     if (nu >= 75):
#         break
#     print(nu)

#"Continue" --> Utilizado para explcuir la condicion del if y continuar el ciclo sin cortarlo
for numers in range(1,11):
    if (numers==3 or numers==5 or numers==7):
        continue
    print(numers)
