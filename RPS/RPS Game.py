import pygame
import random

class Button():
    def __init__(self,x,y,pos,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.pos=pos
        self.height=height

    def clicked(self,pos):
        self.pos=pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                return True
        return False
    
    class RpsGame():
        def __init__(self):
            pygame.init()

            self.screen=pygame.display.set_mode((960,640))
            pygame.display.set_caption("RPS Smasher")

            self.bg=pygame.image.load("background.jpg")
            self.r_btn()=pygame.image.load("r_button.png").convert_alpha()
            self.p_btn()=pygame.image.load("p_button.png").convert_alpha()
            self.s_btn()=pygame.image.load("s_button.png").convert_alpha()

            self.choose_rock=pygame.image.load("rock.png").convert_alpha()
            self.choose_paper=pygame.image.load("paper.png").convert_alpha()
            self.choose_scissors=pygame.image.load("scissors.png").convert_alpha()

            self.screen.blit(self.bg,(0,0))
            self.screen.blit(self.r_btn, (20,500))
            self.screen.blit(self.p_btn, (330,500))
            self.screen.blit(self.s_btn, (640,500))

            self.rock_btn=






  


 