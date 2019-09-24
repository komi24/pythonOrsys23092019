# -*- coding: utf-8 -*-

def dire_bonjour_fr(nom):
    print(f'Bonjour {nom}')
def dire_bonjour_en(nom):
    print(f'Hello {nom}')
def dire_bonjour_es(nom):
    print(f'Hola {nom}')
def dire_bonjour_pt(nom):
    print(f'Oi {nom}')
def dire_bonjour_zh(nom):
    print(f'Ni hao {nom}')

langues = {
    'FR': dire_bonjour_fr,
    'EN': dire_bonjour_en,
    'ES': dire_bonjour_es,
    'PT': dire_bonjour_pt,
    'ZH': dire_bonjour_zh
}
def dire_bonjour(nom, lng="FR"):
    langues[lng](nom)
    