import pygame
import Functions
import Classes

#-------------------------------------------------------------

if __name__ == "__main__":
	pygame.init()
	Screen = pygame.display.set_mode((600,600))
	Screen.fill((0,0,0))
	add = Functions.Draw_Start_Cards(Screen)
	Hit_Button = Functions.Draw_Hit_Button(Screen)
	Drawn = 2
	while True:
		ev = pygame.event.poll()
		Functions.Draw_Score(Screen,add)
                if ev.type == pygame.MOUSEBUTTONDOWN:
                        x, y = ev.pos
                        if Hit_Button.Rectangle.collidepoint(x,y) and add <= 20:
                        	Arr = Functions.Draw_Next_Card(Screen, Drawn)
                        	Drawn = Arr[0]
                        	add += Arr[1]
		pygame.display.flip()