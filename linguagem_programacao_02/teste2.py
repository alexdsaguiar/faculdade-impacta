def lista_perfeitos(n):
    lista = []
    List = []
    resultado = 0

    for numero_menor in range(1, n):
        for numero in range(1, numero_menor):
            if numero_menor % numero == 0:
                lista.append(numero)

        for divisor in lista:
            resultado += divisor

        if resultado == numero_menor:
            List.append(numero_menor)
        
        lista = []
        resultado = 0
        
    return List

print(lista_perfeitos(500))  