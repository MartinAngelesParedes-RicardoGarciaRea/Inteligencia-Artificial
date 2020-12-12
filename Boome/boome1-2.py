import random
tablero1 = [
    [3,3,3,3,3,3,3,3],
    [3,0,0,0,0,0,0,3],
    [3,0,0,2,0,0,0,3],
    [3,2,0,0,0,0,0,3],
    [3,0,0,0,2,0,2,3],
    [3,0,0,3,3,0,0,3],
    [3,0,0,3,3,0,0,3],
    [3,2,0,2,0,0,2,3],
    [3,0,0,0,0,0,0,3],
    [3,0,0,0,2,0,0,3],
    [3,0,0,0,0,0,1,3],
    [3,3,3,3,3,3,3,3]
    ]
def countBoombs(lista):
    count = 0
    for x in lista:
        for y in x:
            if y == 2:
                count += 1
    return count
bombas = countBoombs(tablero1)
print("Existen: ",bombas,"Bombas")
boome = [10,6]

def SIzq(f,c):
    p = tablero1[f][c]
    if ((p == 2) or (p == 3)):
        return 1
    return 0
def SDer(f,c):
    p = tablero1[f][c]
    if ((p == 2) or (p == 3)):
        return 1
    return 0

def SArb(f,c):
    p = tablero1[f][c]
    if ((p == 2) or (p == 3)):
        return 1
    return 0
def SAbj(f,c):
    p = tablero1[f][c]
    if ((p == 2) or (p == 3)):
        return 1
    return 0

def Sboom(f,c):
    p = tablero1[f][c]
    if ((p == 2)):
        return 1
    return 0

#  R3 DER   R0 IZQ    #
R0 = 0
R3 = 0

# R4 ABAJO  #
R4 = 0

#Sb bomba#
def inicio(cb,f,c,RINT0,RINT3,RINT4):
    print("(",f,",",c,")")
    if cb > 0:
        if RINT3 == 0:
            RINT0 = SIzq(f,c - 1)
            if RINT0 == 0:
                c -= 1
            else:
                sb = Sboom(f,c - 1)
                if sb == 1:
                    c -= 1
                    tablero1[f][c] = 0
                    cb -= 1
                else:
                    RINT4 = SArb(f - 1,c)
                    if RINT4 == 0:
                        f -= 1
                        RINT3 = 1
                    else:
                        sb = Sboom(f - 1,c)
                        if sb == 1:
                            f -= 1
                            tablero1[f][c] = 0
                            cb -= 1
                            RINT3 = 1
        else:
            RINT0 = SIzq(f,c + 1)
            if RINT0 == 0:
                c = c + 1
            else:
                sb = Sboom(f,c + 1)
                if sb == 1:
                    c += 1
                    tablero1[f][c] = 0
                    cb -= 1
                else:
                    sb = Sboom(f - 1,c)
                    if sb == 1:
                        f -= 1
                        tablero1[f][c] = 0
                        cb -= 1
                    else:
                        f -= 1
                    RINT3 = 0
        print("Bombas ",cb)
        inicio(cb,f,c,RINT0,RINT3,RINT4)

inicio(bombas,boome[0],boome[1],R0,R3,R4)
print("Bomba")
for x in tablero1:
    print(x)