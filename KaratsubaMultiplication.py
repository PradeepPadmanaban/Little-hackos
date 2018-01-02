import math

def multiply(x,y):
    sx= str(x)
    sy= str(y)
    nx= len(sx)
    ny= len(sy)
    if ny<=2 or nx<=2:
        r = int(x)*int(y)
        return r
    n = nx
    if nx>ny:
        sy = sy.rjust(nx,"0")
        n=nx
    elif ny>nx:
        sx = sx.rjust(ny,"0")
        n=ny
    m = n%2
    offset = 0
    if m != 0:
        n+=1
        offset = 1
    floor = int(math.floor(n/2)) - offset
    a = sx[0:floor]
    b = sx[floor:n]
    c = sy[0:floor]
    d = sy[floor:n]
    print(a,b,c,d)

    ac = multiply(a,c)
    bd = multiply(b,d)

    ad_bc = multiply((int(a)+int(b)),(int(c)+int(d)))-ac-bd
    r = ((10**n)*ac)+((10**(n/2))*ad_bc)+bd

    return r

print(multiply(4,5))
print(multiply(4,58779))
print(int(multiply(4872139874092183,5977098709879)))
print(int(4872139874092183*5977098709879))
print(int(multiply(4872349085723098457,597340985723098475)))
print(int(4872349085723098457*597340985723098475))
print(int(multiply(4908347590823749,97098709870985)))
print(int(4908347590823749*97098709870985))
