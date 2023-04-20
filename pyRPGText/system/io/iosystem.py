from .inputsystem.inputsystem import InputSystem

class IOSystem:
    def __init__(self):
        self.inputsystem = InputSystem()

    def add_command(self,text, function):
        self.inputsystem.add_command(text,function)
    def add_argument_to_command(self,commandText, argumentname, argumentvalue):
        self.inputsystem.add_argument_to_command(commandText,argumentname,argumentvalue)

    def get_input(self):
        self.inputsystem.get_input()