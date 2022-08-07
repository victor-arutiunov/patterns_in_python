from gameplay import Gameplay


class WizardWorld:
    def __init__(self, player_name, player_class):
        self.player_name = player_name
        self.player_class = player_class

    def __str__(self):
        return "\n----------------- Wizard World -----------------\n"

    def play(self):
        Gameplay.start_gameplay_loop()
