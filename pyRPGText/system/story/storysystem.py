from pyRPGText.system.story.storygraph import StoryGraph


class StorySystem:
    def __init__(self):
        self.current_storyblock = None
        self.storyblock_graph = StoryGraph()
        self.storyblock_dict = {}

    def add_story_block(self, storyblock):
        self.storyblock_graph.add_vertex(storyblock)
        self.storyblock_dict[storyblock.get_name()] = storyblock

    def add_story_block_branch(self, main_storyblock, branch_storyblock):
        self.storyblock_graph.add_edge(main_storyblock, branch_storyblock)

    def set_initial_story_block(self, storyblock):
        self.current_storyblock = storyblock
        self.current_storyblock.story = self

    def set_current_story_block(self, storyblock_name):
        if storyblock_name is None:
            self.current_storyblock = None
        else:
            self.current_storyblock = self.storyblock_dict.get(storyblock_name)
            self.current_storyblock.story = self

    def get_graph_keys(self):
        return self.storyblock_graph.get_keys()

    def get_graph_story_block_values(self, storyblock_name):
        return self.storyblock_graph.get_value_from_key(storyblock_name)

    def run(self):
        while self.current_storyblock is not None:
            self.current_storyblock.run()

    def check_story_block_branch_is_none(self, storyblockname):
        if self.get_graph_story_block_values(storyblockname) is None:
            return True
        else:
            return False

    def check_story_block_has_multiple_branches(self, storyblockname):
        if self.get_graph_story_block_values(storyblockname) is not None and len(
                self.get_graph_story_block_values(storyblockname)) > 1:
            if isinstance(
                    self.get_graph_story_block_values(storyblockname), list):
                return True
            else:
                return False
        else:
            return False
