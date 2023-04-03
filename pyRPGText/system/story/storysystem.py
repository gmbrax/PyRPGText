from pyRPGText.system.story.storygraph import storyGraph


class storySystem:
    def __init__(self):
        self.currentStoryBlock = None
        self.storyBlockGraph = storyGraph()
        self.storyBlockDict = {}
    def addStoryBlock(self, storyBlock):
        self.storyBlockGraph.addVertex(storyBlock)
        self.storyBlockDict[storyBlock.getName()] = storyBlock

    def addStoryBlockBranch(self, mainStoryBlock, branchStoryBlock):
        self.storyBlockGraph.addEdge(mainStoryBlock, branchStoryBlock)

    def setInitialStoryBlock(self, storyBlock):
        self.currentStoryBlock = storyBlock
        self.currentStoryBlock.story = self

    def setCurrentStoryBlock(self, storyBlockName):
        if storyBlockName is None:
            self.currentStoryBlock = None
        else:
            self.currentStoryBlock = self.storyBlockDict.get(storyBlockName)
            self.currentStoryBlock.story = self

    def getGraphKeys(self):
      return self.storyBlockGraph.getKeys()

    def getGraphStoryBlockValues(self, storyBlockName):
        return self.storyBlockGraph.getValueFromKey(storyBlockName)

    def run(self):
        while self.currentStoryBlock is not None:
            self.currentStoryBlock.run()
        return

    def checkStoryBlockBranchIsNone(self, storyblockname):
        if self.getGraphStoryBlockValues(storyblockname) is None:
            return True
        else:
            return False

    def checkStoryBlockHasMultipleBranches(self, storyblockname):
        if self.getGraphStoryBlockValues(storyblockname) is not None and len(
        self.getGraphStoryBlockValues(storyblockname)) > 1:
            if isinstance(
            self.getGraphStoryBlockValues(storyblockname), list):
                return True
            else:
                return False
        else:
            return False