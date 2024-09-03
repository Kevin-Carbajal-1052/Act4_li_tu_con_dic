# Ejemplo de uso de listas
misnovias=["Galleta" , "Najera", "Tavito"]
misnumeros=[666, 77, 10]
# Mostrando mis novias
print(misnovias)
# Mostrando mis numeros
print(misnumeros)
print("--Accediendo a los elementos de la lista--")
print(misnovias[-2])
if "Ana" in misnovias:
    print("Si, Ana esta en la lista de mis novias")
else:
    print("Chale no eres mi novia")
print("Numeros de mis novias")
Nnovias=len(misnovias)
print(f"Numero de novias = {Nnovias}")
print("Ciclo for en listas")
posicion=0
for x in misnovias:
    print(posicion," ",x)
    posicion=posicion+1