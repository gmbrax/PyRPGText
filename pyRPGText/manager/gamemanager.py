from pyRPGText.system.game.gamesystem import gameSystem


class gameManager:
    def __init__(self):
        self.gameSystem = gameSystem()

    def addStoryBlock(self,name,text,isInitial=False):
        self.gameSystem.addStoryBlock(name,text,isInitial)

    def addStoryBlockBranch(self,mainBlockName,branchBlockName):
        self.gameSystem.addStoryBlockBranch(mainBlockName,branchBlockName)

    def run(self):
        self.gameSystem.run()