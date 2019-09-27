# -*- coding: utf-8 -*-
import numpy as np
import os
from tkinter import Tk, Canvas, PhotoImage

SIZE = 10

class Pompier:
    def __init__(self, manager):
        """
            position
            is_busy
        """
        self.position = np.random.randint(0,SIZE,2)
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
        if self.is_busy == 0:
            if self.position[0] < destination.position[0]:
                self.position[0] += 1
            elif self.position[0] > destination.position[0]:
                self.position[0] -= 1
            elif self.position[1] < destination.position[1]:
                self.position[1] += 1
            elif self.position[1] > destination.position[1]:
                self.position[1] -= 1
            else:
                self.is_busy = 5
                self.manager.eteindre(destination)
        elif self.is_busy > 0:
            self.is_busy -= 1
            print(self.is_busy)
                
    def __repr__(self):
        return str(self.position)
     
class Feu:
    """
        position
    """
    def __init__(self):
        self.position = np.random.randint(0,SIZE,2)
    def __repr__(self):
        return str(self.position)

class Manager:
    """
        liste_feux
        liste_pompiers
    """
    def __init__(self):
        self.liste_feux = [Feu() for i in range(8)] #[14,2,7]
        self.liste_pompiers = [Pompier(self) for i in range(3)] #[14,2,7]
        
        self.fen = Tk()
        self.canvas = Canvas(self.fen, width=(SIZE+1)*64, height=(SIZE+1)*64)
        self.canvas.pack()
        self.image_pompier = PhotoImage(file="pomp.png")
        self.image_feu = PhotoImage(file="feu.png")
        
    def eteindre(self, feu):
        """
            Retirer le feu de la liste des feux
        """
        self.liste_feux.remove(feu)
        
    def feu_le_plus_proche(self, pompier):
        """
            renvoie le feu le plus proche du pompier
        """
        if len(self.liste_feux) == 0:
            return Feu()
        feu_proche = self.liste_feux[0]
        distance_min = np.linalg.norm(
                    np.array(pompier.position)
                    -np.array(feu_proche.position)
                    )
        
        for feu in self.liste_feux:
            distance = np.linalg.norm(
                    np.array(pompier.position)
                    -np.array(feu.position)
                    )
            if distance < distance_min:
                distance_min = distance
                feu_proche = feu
        return feu_proche
    
    def display(self):
        os.system('cls')
        for i in range(SIZE+1):
            ligne = []
            for j in range(SIZE+1):
                if self.is_feu([i,j]):
                    ligne.append('x')
                elif self.is_pompier([i,j]):
                    ligne.append('o')
                else:
                    ligne.append(' ')
            print(''.join(ligne))

    def is_feu(self, position):
        for feu in self.liste_feux:
            if (feu.position == position).all():
                return True
        return False

    def is_pompier(self, position):
        for pompier in self.liste_pompiers:
            if (pompier.position == position).all():
                return True
        return False
    
    def displayUI(self):
        self.canvas.delete("all")
        for pompier in self.liste_pompiers:
            self.canvas.create_image(
                    pompier.position[0] * 64 + 32,
                    pompier.position[1] * 64 + 32,
                    image=self.image_pompier
                    )
        for feu in self.liste_feux:
            self.canvas.create_image(
                    feu.position[0] * 64 + 32,
                    feu.position[1] * 64 + 32,
                    image=self.image_feu
                    )
        self.canvas.after(800, self.run)
        
    def run(self):
        """
            Fait avancer les pompiers d'une case
            vers le feux le plus proche
        """
        if len(self.liste_feux):
            for pompier in self.liste_pompiers:
                pompier.avancer_vers(self.feu_le_plus_proche(pompier))
            print("pompier", self.liste_pompiers)
            print("feu", self.liste_feux)
            self.displayUI()


from time import sleep

manager = Manager()

manager.run()
manager.fen.mainloop()


#for i in range(30):
#    manager.run()
#    sleep(1)
    
    

