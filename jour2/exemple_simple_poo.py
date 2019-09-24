# -*- coding: utf-8 -*-

class Compte:
    def __init__(self, solde_initial):
        self.solde = solde_initial
        
    def retrait(self, montant):
        self.solde = self.solde - montant

    def depot(self, montant):
        self.solde = self.solde + montant


class Personne:
    def __init__(self, last_name="George"):
        # TODO rajouter un compte initialiser à 1000€
        self.nom = last_name
        self.prenom = "Gerard"
        self.age = 42
        self.compte = Compte(1000)
        
    def transfert(self, autre_personne, montant):
        """
        Retire un montant de mon compte et le 
        dépose sur le compte de autre personne
        """
        self.compte.retrait(montant)
        autre_personne.compte.depot(montant)
        
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
        with open("template_mail.txt", "r") as f:
            text = f.read()
            text = text.replace("{{ nom }}",  self.nom)
            text = text.replace("{{ age }}",  str(self.age))
            text = text.replace("{{ prenom }}",  self.prenom)
            print(text)

    def envoyer_mail_anniversaire_a(self, destinataire):
        """
            afficher le contenu de template_mail.txt
            en remplaçant {{ nom }} par self.nom etc...
        """
        with open("template_mail.txt", "r") as f:
            text = f.read()
            text = text.replace("{{ nom }}",  destinataire.nom)
            text = text.replace("{{ age }}",  str(destinataire.age))
            text = text.replace("{{ prenom }}",  destinataire.prenom)
            print(text)


    def __repr__(self):
        return self.nom

personne_1 = Personne("Bertrand")
personne_2 = Personne("Anais")

personne_1.dire_bonjour(personne_2)
personne_1.envoyer_mail_anniversaire_a(personne_2)
