N, K = input().split()
n = int(N)
k = int(K)
lista = []

for quantidade in range(n):
    nome = str(input())
    lista.append(nome)

lista.sort()
print(lista[k-1])