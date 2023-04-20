from ..story.storysystem import storySystem
from ..story.storyblock import storyBlock


class gameSystem:
    def __init__(self):
        self.storySystem = storySystem()
    
    def addStoryBlock(self,name,text,isInitial=False):
        block = storyBlock(name,text)
        self.storySystem.addStoryBlock(block)
        if isInitial:
            self.storySystem.setInitialStoryBlock(block)
    def addStoryBlockBranch(self,mainBlockName,branchBlockName):
        if mainBlockName in self.storySystem.storyBlockDict.keys()\
                and branchBlockName in self.storySystem.storyBlockDict.keys():
            mainBlock = self.storySystem.storyBlockDict.get(mainBlockName)
            branchBlock = self.storySystem.storyBlockDict.get(branchBlockName)
        else:
            exit(2)

        self.storySystem.addStoryBlockBranch(mainBlock,branchBlock)

    def run(self):
        self.storySystem.run()