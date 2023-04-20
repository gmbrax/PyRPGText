from ..story.storyblock import storyBlock
from ..story.storysystem import storySystem


# from ..io.iosystem import IOSystem ToDo: Integrate the IOSystem to the Game System

class Gamesystem:
    def __init__(self):
        self.storysystem = storySystem()
        # self.iosystem = IOSystem() # It needs to be integrated befored added here

    def add_story_block(self, name, text, is_initial=False):
        block = storyBlock(name, text)
        self.storysystem.addStoryBlock(block)
        if is_initial:
            self.storysystem.setInitialStoryBlock(block)

    def add_story_block_branch(self, main_block_name, branch_block_name):

        if main_block_name in self.storysystem.storyBlockDict.keys() \
                and branch_block_name in self.storysystem.storyBlockDict.keys():
            main_block = self.storysystem.storyBlockDict.get(main_block_name)
            branch_block = self.storysystem.storyBlockDict.get(branch_block_name)
        else:
            exit(2)

        self.storysystem.addStoryBlockBranch(main_block, branch_block)

    def run(self):
        self.storysystem.run()
