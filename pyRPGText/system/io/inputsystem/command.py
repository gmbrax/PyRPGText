from .argument import Argument


class Command:
    def __init__(self, text,function):
        self.argument_dict = {}
        self.text = text
        self.function = function

    def get_text(self):
        return self.text
    def get_key_list_from_argument_dict(self):
        if self.argument_dict is None:
            return None
        else:
            return self.argument_dict.keys()
    def add_argument(self, argumentname, argumentvalue):
        input_argument = Argument(argumentname, argumentvalue)
        if self.argument_dict is None:
            self.argument_dict = {}
        self.argument_dict[input_argument.get_name()] = input_argument