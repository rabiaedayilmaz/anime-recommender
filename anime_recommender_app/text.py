import pygame

class Text:
    def __init__(self, text, color, location, temp_color, fontsize, user_txt=""):
        self.user_txt = user_txt
        self.text = text
        self.color = color
        self.temp_color = temp_color
        self.location = location
        self.font = pygame.font.Font('assets/AthleticOutfit.ttf', fontsize)

    def set(self):
        # if there is user input
        if len(self.user_txt) > 0:
            self.user_txt = self.font.render(self.user_txt, True, self.color)

        # other texts
        if self.temp_color == 0:
            self.text = self.font.render(self.text, True, self.color)
        else:
            self.text = self.font.render(self.text, True, self.color, self.temp_color)

    def write(self, screen):
        #other texts
        textRect = self.text.get_rect()
        textRect.center = self.location

        screen.blit(self.text, textRect)







