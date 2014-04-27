import pygame
import Classes

#------------------------------------------------------

def Print_At(s_x,s_y,l_x,l_y,size,text,color,Screen,bg_color=(255,255,255)):
	Rectangle=pygame.Rect(s_x,s_y,l_x,l_y)
	Surface=pygame.Surface([l_x,l_y])
	Size=pygame.font.Font(None,size)
	Prepare=Size.render(text,1,color,bg_color)
	Screen.blit(Prepare,Rectangle)

#------------------------------------------------------

def Print_On(Button,size,text,color,Screen,bg_color=(255,255,255)):
	Rectangle=pygame.Rect(Button.point_x,Button.point_y,Button.length_x,Button.length_y)
	Surface=pygame.Surface([Button.length_x,Button.length_y])
	Size=pygame.font.Font(None,size)
	Prepare=Size.render(text,1,color,bg_color)
	Screen.blit(Prepare, Rectangle)

#------------------------------------------------------

def Draw_Start_Cards(Screen):
	Card1 = Classes.Card()
	Card2 = Classes.Card()
	B_Card1 = Classes.Button(0,420,100,150,(255,255,255),Screen)
	B_Card1.Do()
	B_Card2 = Classes.Button(120,420,100,150,(255,255,255),Screen)
	B_Card2.Do()
	if Card1.value != 10:
		Print_On(B_Card1,215,str(Card1.value),(0,255,0),Screen)
	else:
		Print_At(0,460,100,200,215/2,"10",(0,255,0),Screen)
	if Card2.value != 10:		
		Print_On(B_Card2,215,str(Card2.value),(0,255,0),Screen)
	else:
		Print_At(120,460,100,200,215/2,"10",(0,255,0),Screen)
	return Card1.value + Card2.value

#------------------------------------------------------

def Draw_Hit_Button(Screen):
	Hit = Classes.Button(0,310,100,100,(0,0,255),Screen)
	Print_On(Hit,100,"Hit",(255,255,255),Screen,Hit.color)
	return Hit

#------------------------------------------------------

def Draw_Next_Card(Screen,there):
	if there <= 4:
		Card = Classes.Card()
		B_Card = Classes.Button(120*there,420,100,150,(255,255,255),Screen)
		B_Card.Do()
		if Card.value != 10:
			Print_On(B_Card,215,str(Card.value),(0,255,0),Screen)
		else:
			Print_At(120*there,460,100,200,215/2,"10",(0,255,0),Screen)
		return [there+1,Card.value]

#------------------------------------------------------

def Draw_Score(Screen, points):
	Print_At(150,310,200,100,50,"Score: "+str(points),(255,255,255),Screen,(0,0,0))

#------------------------------------------------------	







































































#------------------------------------------------------	



#------------------------------------------------------	



#------------------------------------------------------	
