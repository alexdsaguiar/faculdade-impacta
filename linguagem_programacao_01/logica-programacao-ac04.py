while True:
    n=int(input("Digite a quantidade de nomes: "))
    l=[]
    if 3<n<10:
        break
for x in range(1,n):
    l.append(str(input("Digite um nome: ")))
l.insert(3,"Teste")
del l[2]
if "Ana" not in l:
    print("Ana não existe na lista")
if "Ana" in l:
    print("O nome Ana apareceu "+str(l.count("Ana"))+" vez(es) na lista. Primeira ocorrência - índice "+str(l.index("Ana")))
l.sort()
print(l)
