a= 8
b= 5
c= 10

print("Son iguales: " + str(a==b))
print("ES b menor igual a a: " + str(a<=b))
print("ES b mayor igual a a:"  + str(b<=a))
print("Es a mayor a b:"  + str(b<a))
print("Es a mayor a b:"  + str(a<b))
print("Es a diferente de b:"  + str(b!=a))


#concatenar operadores logicos (and,or)
print("Si a es menor que b y a es menor que c: " + str(a<b and a<c))

#concatenante ó o or
print("Si a es menor que b o a es menor que c: " + str(a<b or a<c))