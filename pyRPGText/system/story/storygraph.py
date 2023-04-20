class StoryGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, storyblock):
        self.graph[storyblock.get_name()] = None

    def add_edge(self, storyblock, storyblock_branch):
        if self.graph[storyblock.get_name()] is None:
            self.graph[storyblock.get_name()] = [storyblock_branch.get_name()]
        else:
            self.graph[storyblock.get_name()].append(storyblock_branch.get_name())

    def get_keys(self):
        return self.graph.keys()

    def get_value_from_key(self, key):
        return self.graph.get(key)
