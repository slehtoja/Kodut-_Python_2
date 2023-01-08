class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        # print('Controller', model.pc_nr)  # Test

    def lets_play(self):
        while not self.model.game_over:
            self.view.ask()  # ask number and check
