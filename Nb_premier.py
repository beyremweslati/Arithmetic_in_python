

def saisie():
    x = int(input("donner un entier: "))
    return x

def nm_premier(a):
    aux = False
    i = 1
    while aux == False:
        i = i + 1
        aux = a % i == 0 or i == a // 2
    res = a % i == 0
    return res
def affichage(a,res):
    if(res):
        print(a," n'est pas un nombre premier")
    else:
        print(a," est un nombre premier")
a = saisie()
res = nm_premier(a)
affichage(a,res)