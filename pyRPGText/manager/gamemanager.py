from ..system.game.gamesystem import Gamesystem


class GameManager:
    def __init__(self):
        self.gamesystem = Gamesystem()

    def add_story_block(self, name, text, is_initial=False):
        self.gamesystem.add_story_block(name, text, is_initial)

    def add_story_block_branch(self, main_block_name, branch_block_name):
        self.gamesystem.add_story_block_branch(main_block_name, branch_block_name)

    def run(self):
        self.gamesystem.run()
