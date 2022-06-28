
def saisie():
    aux = False
    while aux == False:
        x = int(input("donner un entier: "))
        aux = x > 0
    return x

def PPCM(a,b):
    i = 1
    x = a
    aux = False
    while aux == False:
        x = a * i
        i = i + 1
        aux = x % b == 0
    return x

a = saisie()
b = saisie()
p = PPCM(a,b)
print("Le PPCM de ",a," et ",b,"est ",p)