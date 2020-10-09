#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
from math import pi
import ch6

char = "aAgGtTcC"

# TODO: Définissez vos fonction ici
def calcule_volume(a : float , b : float , c : float , R : float) -> float :
    volume = a * b * c * 8 * pi / 3
    return (volume , R * volume)

def trier(dictionary : dict) -> tuple :
    sorted_dictionary = sorted(dictionary.items(), key=lambda k: k )
    maximum = max(sorted_dictionary , key=lambda tuple1: tuple1[1])
    return (sorted_dictionary , maximum)

def valide(ADN : str) -> bool :

    for letter in ADN :
        if (letter not in char) or (letter == " ") :
            return False
            
    return True

def saisie(ADN : str) -> str :
    if valide(ADN) :
        return ADN
    else :
        for letter in ADN :
            if (letter not in char) or (letter == " ") :
                ADN = ADN.replace(letter , '')
        return ADN

def proportion(ADN : str , sequence : str) :
    ADN , sequence = saisie(ADN) , saisie(sequence)
    count = ADN.count(sequence)
    return count * 100 / len(ADN)
          
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print("\nLe premier exo -> ")
    a , b , c , r = input("Entrez 3 valeurs, et ensuite la valeur de reau.\n").split()
    a , b , c , r = int(a) , int (b) , int(c) , int(r)
    print(f"Le volume de l'ellipsoide, suivi par son masse est {calcule_volume(a,b,c,r)}")

    print("\nDeuxieme exo ->")
    listd , maximum = trier(ch6.histogram("Hello World"))
    print(f"La list des elements ordonnees par cle est -> {listd} \net le maximum est -> {maximum}.")

    print("Troisieme exo ->")
    #y(60, 5) 

    print("Quatrieme exo -> ")
    chaine , sequence = input("Entrez la chaine ADN et la sequence -> \n").split()
    print(f"Il y a {round(proportion(chaine, sequence),2)}% de '{sequence}'.")
    
    

