n=7
x=1
count=1
soma=0
y=0

while soma<n:
    count=count+1
    soma=soma+x
    z=1/soma
    if soma%2!=0:
        z=-1/soma
    y=y+z
print("%.6f"%y)
