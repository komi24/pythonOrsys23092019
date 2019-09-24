# -*- coding: utf-8 -*-

#with open("template_mail.txt", "w") as f:
#    f.write("""
#            Bonjour {{ nom }} {{ prenom }},
#            Pour vos {{ age }} ans, nous vous souhaitons un joyeux anniversaire.
#            Cordialement,
#            
#            SFR
#            """)

with open("template_mail.txt", "r") as f:
    print(f.read())