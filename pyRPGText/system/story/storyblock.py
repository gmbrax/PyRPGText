class storyBlock:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.story = None

    def run(self):
        print(self.text)
        if self.story.checkStoryBlockBranchIsNone(self.name):
            self.story.setCurrentStoryBlock(None)
            return
        if self.story.checkStoryBlockHasMultipleBranches(self.name):
            validoptions = self.story.getGraphStoryBlockValues(self.name)
            while True:
                print(f"Where do you want to go? {validoptions} ->", end=" ")
                userInput = input()
                if userInput in validoptions:
                    self.story.setCurrentStoryBlock(userInput)
                    break
        else:
            self.story.setCurrentStoryBlock(self.story.getGraphStoryBlockValues(self.name)[0])

    def getName(self):
        return self.name
