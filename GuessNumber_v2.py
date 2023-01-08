from Controller import Controller
from Model import Model
from View import View
import datetime


class GuessNumber_v2:

    def __init__(self):
        self.model = Model()  # Loome mudeli
        self.view = View(self.model)  # Loome vaate
        self.controller = Controller(self.model, self.view)  # Loome Controlleri
        self.running = True  # while loop jaoks

    def start(self):
        while self.running:
            result = self.view.menu()  # Show game menu
            if result == 3:  # Exit
                self.running = False
            elif result == 1:  # Lets play
                self.controller.lets_play()
                if self.model.game_over:
                    name = self.view.ask_name()
                    self.model.write_score_to_file(name, self.model.steps, self.model.datetime)
                    self.model.datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    self.model.steps = 0  # Sammud nullida
                    self.model.game_over = False  # Mäng algab uuesti
                    self.model.pc_nr = self.model.new_number()  # Arvuti uus number
            elif result == 2:
                self.view.show_scoreboard()


if __name__ == '__main__':
    # GuessNumber_v2().start()  # One line
    game = GuessNumber_v2()  # Two line
    game.start()  # Two line
