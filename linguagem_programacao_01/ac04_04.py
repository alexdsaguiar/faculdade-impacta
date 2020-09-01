while True:
    n1=int(input())
    if n1<1 or n1>9:
        print("Insira um número inicial entre 1 e 9")
    else:
        break
while True:
    n2=int(input())
    if n2<1 or n2>9:
        print("Insira um número final entre 1 e 9")
    else:
        break
if n1>n2:
    print("Nenhuma tabuada nesse intervalo")
else:
    for x in range(n1,n2+1):
        for y in range(1,10):
            print(x,"x",y,"=",x*y)
        print("")
