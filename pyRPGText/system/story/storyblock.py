class StoryBlock:
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.story = None

    def run(self):
        print(self.text)
        if self.story.check_story_block_branch_is_none(self.name):
            self.story.set_current_story_block(None)
            return
        if self.story.check_story_block_has_multiple_branches(self.name):
            validoptions = self.story.get_graph_story_block_values(self.name)
            while True:
                print(f"Where do you want to go? {validoptions} ->", end=" ")
                user_input = input()
                if user_input in validoptions:
                    self.story.set_current_story_block(user_input)
                    break
        else:
            self.story.set_current_story_block(self.story.get_graph_story_block_values(self.name)[0])

    def get_name(self):
        return self.name
