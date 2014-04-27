from random import randint
import pygame

#--------------------------------------------------------------

class Card(object):

        def __init__(self, value = 0, suit = "None", name = ""):
            if value == 0 and suit == "None":
                self.value = randint(1,10)
                x = randint(1,4)
                if x == 1:
                    x = "of Hearts"
                elif x == 2:
                    x = "of Spades"
                elif x == 3:
                    x = "of Diamonds"
                else:
                    x = "of Clubs"
                self.suit = x
            else:
                    self.value = value
                    self.suit = suit
                    self.name = str(self.value) + self.suit

#--------------------------------------------------------------

        def Is_Ace(self):
                if self.value == 1:
                        return True
                return False

#--------------------------------------------------------------

class Button(object):
    def __init__(self, point_x, point_y, length_x, length_y, color, Main_Screen): #Color is a list of 3 indeces. [RED, GREEN, BLUE]
        self.point_x = point_x
        self.point_y = point_y
        self.length_x = length_x
        self.length_y = length_y
        self.color = color
        self.Main_Screen = Main_Screen
        self.Rectangle = pygame.Rect(self.point_x, self.point_y, self.length_x, self.length_y)
        self.Surface = pygame.Surface([self.length_x, self.length_y])
        self.Surface.fill((self.color[0], self.color[1], self.color[2]))
    def Do(self):
        self.Main_Screen.blit(self.Surface, self.Rectangle)

#--------------------------------------------------------------
