# Linguagem de Programação II
# AC01 ADS-EaD - Números Especiais
#
# Email Impacta: alexandre.aguiar@aluno.faculdadeimpacta.com.br

def eh_primo(n):
    if n < 2:
        return False
    else:
        for div in range(2, n):
            if n % div == 0:
                return False
        return True

def lista_primos(n):
    List = []
    for num in range(2, n):
        List.append(num)
        if num < 2:
            List.remove(num)
        else:
            for div in range(2, num):
                if num % div == 0:
                    List.remove(num)
                    break          
    return List

def eh_armstrong(n):
    if n == 0:
        return False

    lenght = int(len(str(n)))
    lista_1 = list(str(n))
    lista_2 = []
    soma = 0

    for digitos in lista_1:
        resultado_1 = int(digitos) ** lenght
        lista_2.append(resultado_1)

    for resultados in lista_2:
        soma += resultados

    return soma == n

def lista_armstrong(n):
    List = []
    
    for numero in range(1, n):
        lenght = int(len(str(numero)))
        lista_1 = list(str(numero))
        lista_2 = []
        soma = 0

        for digitos in lista_1:
            resultado_1 = int(digitos) ** lenght
            lista_2.append(resultado_1)

        for resultados in lista_2:
            soma += resultados

        if soma == numero:
            List.append(numero)

    return List

def eh_perfeito(n):
    if n == 0:
        return False

    lista = []
    resultado = 0

    for numero in range(1, n):
        if n % numero == 0:
            lista.append(numero)

    for divisor in lista:
        resultado += divisor

    return resultado == n

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