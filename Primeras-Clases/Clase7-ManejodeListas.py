#Como cambiar un lenguaje por otro
lenguajes= ["php","java","phyton","javascript"]

print("Lenguaje seleccionado: " + lenguajes[2])

lenguajes[2]= "Ruby"

print("Lenguaje: " + lenguajes[2])


#Agregar un nuevo lenguaje a la lista
lenguajes.append(("Angular"))
print(lenguajes)

#Para Sacar o remover un elemento de la lista
lenguajes.remove("php")
print(lenguajes)
