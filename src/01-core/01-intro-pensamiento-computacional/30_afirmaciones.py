def primera_letra(lista_palabras):
    # Se define un arreglo donde se guardará el valor de la primera letra de las palabras s
    primeras_letras = []

    for palabra in lista_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se admiten str vacíos'

        primeras_letras.append(palabra[0])

    return primeras_letras

if __name__ == "__main__":
    lista_palabras = [0,'laborando','trabajando','soñando']
    print(primera_letra(lista_palabras))