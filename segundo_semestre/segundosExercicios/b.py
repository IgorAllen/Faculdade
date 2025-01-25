def ordenaLista(lista):
    lista.sort() #"sort" ñ tem retorno.
    return lista

x = [3, 2, 1]

print("Lista antes do função:", x)
ordenaLista(x)
print("Lista depois do função:", x)

#Lista antes do função: [3, 2, 1].
#Lista depois do função: [1, 2, 3].
