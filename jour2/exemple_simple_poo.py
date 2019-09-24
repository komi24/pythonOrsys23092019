# -*- coding: utf-8 -*-

class Compte:
    def __init__(self, solde_initial):
        self.solde = solde_initial
        
    def retrait(self, montant):
        pass
    def depot(self, montant):
        pass

class Personne:
    def __init__(self, last_name="George"):
        # TODO rajouter un compte initialiser à 1000€
        self.nom = last_name
        self.prenom = "Gerard"
        self.age = 42
        
    def transfert(self, autre_personne, montant):
        """
        Retire un montant de mon compte et le 
        dépose sur le compte de autre personne
        """
    def dire_bonjour(self, autre_personne):
        """
            Dire :
                "bonjour {nom de l'autre personne},
                Je m'appelle {mon nom}"
        """
        print(f"Bonjour {autre_personne}")
        print(f"Je m'appelle {self.nom}")
    
    def envoyer_mail_anniversaire(self):
        """
            afficher le contenu de template_mail.txt
            en remplaçant {{ nom }} par self.nom etc...
        """
        text = "Bonjour"
        text = text.replace("on", "au")
    def __repr__(self):
        return self.nom

personne_1 = Personne("Bertrand")
personne_2 = Personne("Anais")

personne_1.dire_bonjour(personne_2)

