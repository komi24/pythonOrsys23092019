# -*- coding: utf-8 -*-

class Personne:
    def __init__(self, last_name="George"):
        self.nom = last_name
        self.prenom = "Gerard"
        self.age = 42

#une_personne = Personne("Durand")
#autre_personne = Personne()
#print(une_personne.nom)
#
#une_personne.nom = "Alain"
#
#print(une_personne.nom)

import numpy as np

class Voiture:
    """
     attribut:
         - couleur = par défaut à 'rouge'
         - vitesse_max = 180
         - position 
    """
    def __init__(self, position_initiale, couleur='rouge'):
        self.position = np.array(position_initiale)
        self.couleur = couleur
        self.vitesse_max = 180
        self.direction = np.array([1,0])

    def avancer(self):
        nouvelle_position = self.position + self.direction
        if (nouvelle_position > 0).all() and (nouvelle_position < 10).all():
#        if nouvelle_position[0] < 10 and nouvelle_position[0] >= 0 \
#            and nouvelle_position[1] < 10 and nouvelle_position[1] >= 0:
            self.position = nouvelle_position
        else:
            self.tourner()
            self.avancer()
        
    def tourner(self):
        self.direction = np.array([[0,-1],[1,0]]).dot(self.direction)

def addition(a,b):
    """
        :Example:
        >>> addition(2,4)
        6
    """
    return a + b

#print(__name__)
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    ma_voiture = Voiture([2,3], 'bleue')
    print(ma_voiture.position)
    for i in range(20):
        ma_voiture.avancer()
        print(ma_voiture.position)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        