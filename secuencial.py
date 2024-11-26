def busquedaSecuencial(unaLista, item):
    pos = 0
    encontrado = False
    while pos < len(unaLista) and not encontrado:
        if unaLista[pos] == item:
            encontrado = True
        else:
            pos = pos+1
    return encontrado
listaPrueba = [3, 5, 7, 9, 11, 13, 15]

numero= int(input("¿Qué número quiere buscar?: "))
resultado = busquedaSecuencial(listaPrueba, numero)

if resultado:
    print(f"El número {numero} está en la lista.")
else:
    print(f"El número {numero} no está en la lista.")
