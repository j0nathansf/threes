from os import path
import sys
sys.path.append("../")
from ui.pygetch.getch.getch import *
import platform

def get_user_move():
        """
        Fait une saisie controlée du joueur lorsqu'il est dans le jeu
        """
        print("Retour menu : M")
        print("Déplacements : ←, ↑, ↓, →")
        menu = [77, 109]
        if platform.system() == "Linux":
                fleches = {27 : {91 : {65 : 'h', 66 : 'b', 67 : 'd', 68 : 'g'}}}
                while True:
                        char = ord(getch())
                        if char in menu:
                                return 'm'
                        elif char in list(fleches):
                                char = ord(getch())
                                if char in list(fleches[27]):
                                        char = ord(getch())
                                        if char in list(fleches[27][91]):
                                                return fleches[27][91][char]
        else:
                fleches = {224 : {72 : 'h', 75 : 'g', 77 : 'd', 80 : 'b'}}
                while True:
                        char = ord(getch())
                        if char in menu:
                                return 'm'
                        elif char in list(fleches):
                                char = ord(getch())
                                if char in list(fleches[224]):
                                        return fleches[224][char]

def get_user_menu():
    """
    Fait une saisie contrôlée du joueur lorsqu'il est dans le menu
    """
    menu =  {
        'N' : ["Commencer une partie", 110, 78],
        'L' : ["Charger une partie", 76, 108],
        'S' : ["Sauvegarder une partie", 115, 83],
        'C' : ["Reprendre une partie en cours", 99, 67],
        'T' : ["Test unitaires", 116, 84],
        'Q' : ["Terminer le jeu", 113, 81]
    }
    print("MENU PRINCIPAL".center(32, "-"))
    for i in range(0, len(menu)):
        print(list(menu)[i] + ") " + list(menu.values())[i][0])
    while True:
        char = ord(getch())
        choix = char
        while True:
            if char in (27, 91) and ord(getch()) in (91, 27) or char == 0:
                ord(getch())
                break
            for i in range(0, len(menu)):
                if char in (list(menu.values())[i][1], list(menu.values())[i][2]) and char == choix:
                    return list(menu)[i]
            break
