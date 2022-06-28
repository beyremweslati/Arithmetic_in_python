

def saisie():
    aux = False
    while aux == False:
        x = int(input("donner un entier: "))
        aux = x > 0
    return x

def pgcd_euclide(a,b):
    aux = False
    while aux == False:
        R = a % b 
        a = b
        b = R
        aux = b == 0
    return a

a = saisie()
b = saisie()
p = pgcd_euclide(a,b)
print("Le PGCD de ",a," et ",b,"est ",p)

