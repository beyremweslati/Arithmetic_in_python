from numpy import *
def saisie():
    aux = False
    while aux == False:
        n = int(input("donner un entier: "))
        aux = n > 0
    return n
def remplir(n):
    i = 2
    x = 0
    aux = False
    while aux == False:
        if(n % i == 0):
            n = n // i
            t[x] =  i
            x = x + 1
        else:
            i = i + 1
        aux = n == 1
    return t,x
def afficher(t,x):
    for i in range(x-1):
        print(t[i],"x ", end="")
    print(t[x-1],end="")








n = saisie()
t = array([int]*50)
t,x = remplir(n)
print(n,"= ", end="")
afficher(t,x)