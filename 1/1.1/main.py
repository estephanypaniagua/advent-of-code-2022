archivo = open("data.txt")
lista = archivo.readlines()
suministros = [0]
indice = 0
for index, value in enumerate(lista):
    if value == "\n":
        lista[index] = ""
        suministros.append(0)
        indice = indice+1

    elif value[-1] == "\n":
        lista[index] = value[:-1]
        suministros[indice] = suministros[indice] + int(lista[index])

    else:
        suministros[indice] = suministros[indice] + int(lista[index])

print(max(suministros))
