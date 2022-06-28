
def saisie():
    aux = False
    while aux== False:
        x = int(input("donner un entier: "))
        aux = x > 0
    return x

def pgcd_diff(a,b):
    aux = False
    while aux == False:
        if(a > b):
            a = a-b
        else:
            b = b-a
        aux = a == b
    return a

a = saisie()
b = saisie()
p = pgcd_diff(a,b)
print("Le PGCD de ",a," et ",b,"est ",p)
