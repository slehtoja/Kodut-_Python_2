import os.path
import random
import datetime


class Model:

    def __init__(self):
        self.minimum = 1
        self.maximum = 100
        self.pc_nr = random.randint(self.minimum, self.maximum)
        self.steps = 0
        self.game_over = False
        self.datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.filename = 'scores.txt'
        self.cheater = False

    def new_number(self):
        # PC new number
        return random.randint(self.minimum, self.maximum)

    def write_score_to_file(self, name, score, datetime):
        if not self.cheater:
            if os.path.exists(self.filename):
                """ File exists """
                with open(self.filename, 'a', encoding='utf-8') as f:
                    f.write(name + ';' + str(score) + ';' + str(self.datetime) + '\n')
            else:
                """ File does not exists """
                with open(self.filename, 'w', encoding='utf-8') as f:
                    f.write(name + ';' + str(score) + ';' + str(self.datetime) + '\n')
        else:
            print()
            print('You cheated and wont get to the scoreboard :(')
            self.cheater = False

    def read_score_file(self):
        scores = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                all_lines = f.readlines()
                for score in all_lines:
                    score = score.strip()
                    scores.append(score.split(';'))
        else:
            scores = None

        return scores
