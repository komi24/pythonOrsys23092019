# -*- coding: utf-8 -*-

def assertInt(ancienne_fonction):
    print("Application du décorateur")
    def nouvelle_fonction(*args):
        print("Intérieur de ma nouvelle fonction")
        for a in args:
            assert type(a) == int, \
                "Les arguments de la fonction doivent être des entiers"
        return ancienne_fonction(*args)
    return nouvelle_fonction

@assertInt
def addition(a, b):
    return a + b

@assertInt
def soustraction(a, b):
    return a - b

@assertInt
def multiplication(*args):
    resultat = 1
    for i in args:
        resultat *= i
    return resultat

print(addition(4,7))

print(soustraction(4,7))
print(multiplication(4,7, 2,3))
print(addition(4,7))
#try:
#    print(addition("b","a"))
#except Exception as e:
#    print('Error', e)
    
print("FIN")

