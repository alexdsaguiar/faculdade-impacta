def eh_primo(n):
    lista = []
    if n < 2:
        return False
    else:
        for div in range(2, n):
            x = n % div
            lista.append(x)
            if n % div == 0:
                return False
                
        return True

print(eh_primo(2))