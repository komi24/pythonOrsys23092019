# -*- coding: utf-8 -*-

class Pompier:
    def __init__(self, position_init, manager):
        """
            position
            is_busy
        """
        self.position = position_init
        self.is_busy = 0
        self.manager = manager
        
    def avancer_vers(self, destination):
        """
            Faire le pompier avancer 
            d'une case vers la destination
            2e Etape : Quand le pompier arrive sur le feu.
            is_busy passe à 5 
            3e Etape : Si is_busy est >0 le pompier 
            n'avance pas. is_busy -= 1
            4e Etape : Quand is_busy est égale à 1
            On éteint le feu et is_busy devient nul
            appeler self.manager.eteindre(feu)
        """
        if self.position[0] < destination.position[0]:
            self.position[0] += 1
        elif self.position[0] > destination.position[0]:
            self.position[0] -= 1
        elif self.position[1] < destination.position[1]:
            self.position[1] += 1
        elif self.position[1] > destination.position[1]:
            self.position[1] -= 1
     
class Feu:
    """
        position
    """
    def __init__(self, position_init):
        self.position = position_init

class Manager:
    """
        liste_feux
        liste_pompiers
    """
    def __init__(self):
        self.liste_feux = [Feu([3,2]), Feu([6,7])] #[14,2,7]
        self.liste_pompiers = [Pompier([1,1], self)] #[14,2,7]
        
    def eteindre(self, feu):
        """
            Retirer le feu de la liste des feux
        """
        pass
    def run(self):
        """
            Fait avancer les pompiers d'une case
            vers le feux le plus proche
        """
        self.liste_pompiers[0].avancer_vers(self.liste_feux[0])
        print("pompier", self.liste_pompiers[0].position)
        print("feu", self.liste_feux[0].position)



manager = Manager()
for i in range(10):
    manager.run()


