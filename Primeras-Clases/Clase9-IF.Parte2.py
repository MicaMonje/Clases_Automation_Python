a= 40
b= 20
c= 10

#Es una manera  pero no es recomendada
#if(a>b):
#    if(a>c):
#        print("El mayor es: " + str(a))


# #Forma correcta
# if(a>b and a>c):
#     print("El mayor es: " + str(a))
# elif(b>a and b>c):
#     print("El mayor es: " + str(b))
# #Por descarte no se anoto (c>a and c>b) con el else podemos ver la unica opcion restante
# else:
#     print("El mayor es: " + str(c))

if(a<b | a>c):
    print("{} es menor que {} ó {} es mayor que {}" .format(a,b,a,c))