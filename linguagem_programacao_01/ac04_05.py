x1=input()
x2=input()
z=0
combination=str(x1)
digit=str(x2)

if digit not in combination:
    print("Caractere nao encontrado.")
else:
    x=combination.split(digit)
    for y in x:
        z+=1
    print("O caractere buscado ocorre",(z-1),"vezes na sequencia.")