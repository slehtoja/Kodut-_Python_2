import re
import datetime


class View:

    def __init__(self, model):
        self.model = model
        # print('View', model.pc_nr)  # Test

    def menu(self):
        print('-----------------')
        print('1. Lets Play Game')
        print('2. Show scoreboard')
        print('3. Exit')
        print('-----------------')
        return int(input('Please make a choice 1, 2 or 3: '))

    def ask(self):
        mn = str(self.model.minimum)  # Minimum
        mx = str(self.model.maximum)  # Maximum
        print()
        user_input = int(input('Enter the guessed number '+mn+' - '+mx+': '))
        self.model.steps += 1  # Steps + 1
        if user_input > self.model.pc_nr and user_input != 10000:
            print('The number is smaller!')
        elif user_input < self.model.pc_nr and user_input != 10000:
            print('The number is bigger!')
        elif user_input == self.model.pc_nr and user_input != 10000:
            print('Hurray! You guessed number in ' + str(self.model.steps) + ' steps.')
            self.model.game_over = True
        elif user_input == 10000:
            print(' You found back door. The correct number is', self.model.pc_nr)
            self.model.cheater = True

    def ask_name(self):
        print()
        return input('What is your name? ')

    def show_scoreboard(self):
        scores = self.model.read_score_file()
        print()
        print('Scoreboard:')
        if scores is not None:
            scores.sort(key=lambda s: (int(s[1]), datetime.datetime.now().strptime(s[2], "%Y-%m-%d %H:%M:%S")))
            for score in scores:
                score[0] = re.sub(r'^(.{15}).*$', '\\g<1>...', score[0])
                score[2] = datetime.datetime.now().strptime(score[2], "%Y-%m-%d %H:%M:%S").strftime("%d.%m.%Y %H:%M:%S")
                print(score[0].ljust(18, ' '), score[1].rjust(4, ' '), score[2])   # Names, steps
        else:
            print('First play game :)')
