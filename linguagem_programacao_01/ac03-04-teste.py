y=1
x=0
for y in range(1,8):
    z=1/y
    if y%2!=0:
        z=-1/y
    x+=z
    print("%.6f"%x)

