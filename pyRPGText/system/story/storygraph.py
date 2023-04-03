class storyGraph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, storyBlock):
        self.graph[storyBlock.getName()] = None

    def addEdge(self, storyBlock, storyBlockBranch):
        if self.graph[storyBlock.getName()] is None:
            self.graph[storyBlock.getName()] = [storyBlockBranch.getName()]
        else:
            self.graph[storyBlock.getName()].append(storyBlockBranch.getName())

    def getKeys(self):
        return self.graph.keys()

    def getValueFromKey(self, key):
        return self.graph.get(key)