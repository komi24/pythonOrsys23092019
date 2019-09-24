# -*- coding: utf-8 -*-

class Pompier:
    def __init__(self):
        """
            position
            etat
        """
        pass
    def avancer_vers(self, destination):
        """
            Faire le pompier avancer 
            d'une case vers la destination
        """
        pass
     
class Feu:
    """
        position
    """
    pass

class Manager:
    """
        liste_feux
        liste_pompier
    """
    def run(self):
        """
            Fait avancer les pompiers d'une case
            vers le feux le plus proche
        """
        self.liste_pompiers[0].avancer_vers(liste_feux[0])