import pygame
from button import Button
from text import Text

WIDTH, HEIGHT = 1050, 600


class menuScreen:
    def __init__(self, bg_img, start_btn, start_btn_clicked, screen):
        self.screen = screen

        # load background image
        self.bg_img = pygame.image.load(bg_img).convert_alpha()
        self.background_img = pygame.transform.scale(self.bg_img, (WIDTH, HEIGHT))

        # load start button
        self.start_btn = pygame.image.load(start_btn).convert_alpha()
        self.start_btn = pygame.transform.scale(self.start_btn, (260, 100))

        # load clicked start button
        self.start_btn_clicked = pygame.image.load(start_btn_clicked).convert_alpha()
        self.start_btn_clicked = pygame.transform.scale(self.start_btn_clicked, (260, 100))

        # create start button
        self.is_clicked = Button(90, 280, self.start_btn, 1).click(screen)

    def draw_update(self):
        self.screen.blit(self.background_img, (0, 0))
        self.screen.blit(self.start_btn, (80, 290))
        if self.is_clicked:
            self.screen.blit(self.start_btn_clicked, (80, 290))
            #Button(90, 280, self.start_btn_clicked, 1, self.screen).click()

    def write(self, text):
        menu_text = Text(str(text), (255, 255, 255), (500, 200), 0, 60)
        menu_text.set()
        menu_text.write(self.screen)

        pygame.display.update()

class choiceScreen:
    def __init__(self, bgc_img, input_box, screen, user_text=""):
        self.screen = screen
        self.user_txt = user_text

        # load background image
        self.bgc_img = pygame.image.load(bgc_img).convert_alpha()
        self.bgc_img = pygame.transform.scale(self.bgc_img, (WIDTH, HEIGHT))

        # load input box
        self.input_box = pygame.image.load(input_box).convert_alpha()
        self.input_box = pygame.transform.scale(self.input_box, (500, 100))

    def draw_update(self, screen):
        screen.blit(self.bgc_img, (0, 0))
        screen.blit(self.input_box, (250, 250))

    def write(self, text):
        choice_text = Text(str(text), (255, 255, 255), (500, 200), 0, 60)
        choice_text.set()
        choice_text.write(self.screen)

        # if there is user input
        if self.user_txt != "":
            self.user_txt = Text(self.user_txt, (175, 143, 233), (500, 300), 0, 60)
            self.user_txt.set()
            self.user_txt.write(self.screen)

        pygame.display.update()


class resultScreen:
    def __init__(self, bgn_img, resbox, backbtn, back_btn_clicked, screen, result=""):
        self.screen = screen
        self.result = result

        # load background image
        self.bgn_img = pygame.image.load(bgn_img).convert_alpha()
        self.bgn_img = pygame.transform.scale(self.bgn_img, (WIDTH, HEIGHT))

        # load result box
        self.resbox = pygame.image.load(resbox).convert_alpha()
        self.resbox = pygame.transform.scale(self.resbox, (800, 200))

        # load back button
        self.backbtn = pygame.image.load(backbtn).convert_alpha()
        self.backbtn = pygame.transform.scale(self.backbtn, (260, 100))

        # load back button clicked
        self.back_btn_clicked = pygame.image.load(back_btn_clicked).convert_alpha()
        self.back_btn_clicked = pygame.transform.scale(self.back_btn_clicked, (260, 100))

        self.is_clicked = Button(90, 280, self.backbtn, 1).click(screen)

    def draw_update(self):
        self.screen.blit(self.bgn_img, (0, 0))
        self.screen.blit(self.resbox, (130, 70))
        self.screen.blit(self.backbtn, (70, 290))
        if self.is_clicked:
            self.screen.blit(self.back_btn_clicked, (70, 290))


    def write(self, result):
        if type(result) != str:
            res = Text(result[0], (0, 0, 0), (500, 200), 0, 40)
            res.set()
            res.write(self.screen)
        elif result == "This anime is not in database :(":
            res = Text("This anime is not in database :(", (0, 0, 0), (500, 170), 0, 50)
            res.set()
            res.write(self.screen)
        pygame.display.update()