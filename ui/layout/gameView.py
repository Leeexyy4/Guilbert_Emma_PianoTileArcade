import pygame
import random
import numpy as np
import sys

from ui.utils.note import Note

class GameView:
    def __init__(self, windowManager):
        self.__windowManager = windowManager
        self.__notes = {
            self.createNoteFromMP3(self.__windowManager.getMusicSelect())
        }
        self.__listNotes = list[Note(self)]
        
    def affichageJeu(self):
        """
            La fonction affichageJeu permet l'affichage du jeu
        """
         