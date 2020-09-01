lista = []

while True:
    pedido = input().split()
    if pedido[0] in "a":
        lista.append(pedido[1])
    elif pedido[0] in "r" and pedido[1] not in lista:
        print("falha")
    elif pedido[0] in "r":
        del lista[-1]
        print("removido")
    elif pedido[0] in "p":
            print(" ".join(lista))
    if pedido[0] in "s":
        break