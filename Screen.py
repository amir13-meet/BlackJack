import pygame
import Functions
import Classes

#-------------------------------------------------------------

if __name__ == "__main__":
	pygame.init()
	Screen = pygame.display.set_mode((600,600))
	Screen.fill((0,0,0))
	add = Functions.Draw_Start_Cards(Screen) #return the sum of the first two cards' values
	Hit_Button = Functions.Draw_Hit_Button(Screen) #returns the Hit button to click on
	Drawn = 2 #cards drawn already
	while True:
		ev = pygame.event.poll()
		Functions.Draw_Score(Screen,add) #draws the current score (keeps track)
                if ev.type == pygame.MOUSEBUTTONDOWN:
                        x, y = ev.pos
                        if Hit_Button.Rectangle.collidepoint(x,y) and add <= 20:
                        	Arr = Functions.Draw_Next_Card(Screen, Drawn) #draws an additional card
                        	Drawn = Arr[0] #adds 1 to the drawn cards
                        	add += Arr[1] #adds the new card's value to the others'
		pygame.display.flip()
