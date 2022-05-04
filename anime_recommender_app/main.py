import sys
import pygame

from anime_recommender import AnimeRecommender
from screens import menuScreen, choiceScreen, resultScreen

# constants
WIDTH, HEIGHT, FPS = 1050, 600, 60
x, y = 30, 200
dt = 0

# button/box paths
start_btn = "assets/startbutton.png"
start_btn_clicked = "assets/startbutton_clicked.png"
input_box = "assets/input_box.jpg"
res_box = "assets/resultbox.png"
back_btn = "assets/backbutton.png"
back_btn_clicked = "assets/backbutton_clicked.png"

# background paths
menu_bg = "assets/menuu.png"
choice_bg = "assets/secim.jpg"
res_bg = "assets/results_bg.jpg"

# texts
menu_txt = "Anime Recommender"
choice_txt = "Enter an anime you like"

# data path
data_path = "app_data/last_app_data.csv"

class App:
    def __init__(self):
        pygame.init()

        self.user_text = ""
        self.search_anime = ""
        self.recommendation = ""
        self.on_scene = 0
        self.recommend = False
        self.in_db = True

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            pygame.display.set_caption('Anime Recommender')

            if self.on_scene == 0:
                menu = menuScreen(menu_bg, start_btn, start_btn_clicked, self.screen)
                menu.draw_update()
                menu.write(menu_txt)
            elif self.on_scene == 1:
                menu2 = choiceScreen(choice_bg, input_box, self.screen, self.user_text)
                menu2.draw_update(self.screen)
                menu2.write(choice_txt)

            else:
                menu3 = resultScreen(res_bg, res_box, back_btn, back_btn_clicked, self.screen)
                menu3.draw_update()
                menu3.write(self.recommendation)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP and (80 < mouse_x < 80+260 and 290 < mouse_y < 290+100):
                    self.on_scene = 1

                # check if keyboard pressed and on the choice screen
                elif event.type == pygame.KEYDOWN and self.on_scene == 1:
                    # to delete
                    if event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    # to get input
                    elif event.key == pygame.K_RETURN:
                        # print(self.user_text)
                        # anime to search in dataset
                        self.search_anime = self.user_text

                        # time to recommend
                        self.recommend = True

                        # clears input data
                        self.user_text = ""

                        # show results to user
                        self.on_scene = 2

                    # to write
                    else:
                        self.user_text += event.unicode
            if self.recommend:
                # anime recommender part
                recommender = AnimeRecommender(data_path, self.search_anime)
                animelist = recommender.search_cluster()
                self.recommendation, self.in_db = recommender.recommend(animelist)
                # print(self.recommendation)
                # if not false, it loops
                self.recommend = False

            self.clock.tick(FPS)

if __name__ == '__main__':
    app = App()
    app.run()