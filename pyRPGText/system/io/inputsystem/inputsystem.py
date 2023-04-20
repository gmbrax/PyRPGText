from pyRPGText.system.io.inputsystem.command import Command


class InputSystem:
    def __init__(self):
        self.inputed_command = None
        self.inputed_argument = None
        self.is_valid_command = False
        self.is_valid_argument = False
        self.command_dict={}

    def reset_all(self):
        self.inputed_command = None
        self.inputed_argument = None
        self.is_valid_command = False
        self.is_valid_argument = False
    def add_command(self, text, function):
        input_command= Command(text, function)
        input_command.argument_dict = None
        self.command_dict[input_command.get_text()] = input_command

    def add_argument_to_command(self, commandtext, argumentname, argumentvalue):
        if commandtext in self.command_dict.keys():
            command = self.command_dict.get(commandtext)
            command.add_argument(argumentname, argumentvalue)
    def get_input(self):
        while True:
            user_input = input("Command-> ")
            self.process_input(user_input)
            if self.is_valid_command and self.is_valid_argument :
                break
            else:
                self.reset_all()
    def process_input(self,userinput):
        temp_command, temp_argument = self.process_and_validate_command(userinput)
        if self.is_valid_command:
            temp_argument = self.process_argument(temp_command, temp_argument)
            self.validate_argument(temp_argument)
    def process_and_validate_command(self, userinput):
        temp_command = f""
        for index, char in enumerate(userinput):
            temp_command = temp_command + char
            if temp_command in self.command_dict.keys():
                self.is_valid_command = True
                self.inputed_command = temp_command
                break
            elif temp_command not in self.command_dict.keys() and index == len(userinput)-1:
                self.inputed_command = None
                temp_command=None
                break

        if self.is_valid_command:
            temp_argument_text = userinput.replace(temp_command, "")
            temp_argument_text = temp_argument_text.strip()
            return (temp_command,temp_argument_text)
        else:
            print("Invalid Input: Not A valid Command")
            return (None,None)

    def process_argument(self, command, argumenttext):
        def check_if_argument_is_not_blank(argumenttext):
            return bool(argumenttext and not argumenttext.isspace())
        if Command is not None:
            temp_command = self.command_dict.get(command)
        else:
            return

        if temp_command.get_key_list_from_argument_dict() is not None:
            if check_if_argument_is_not_blank(argumenttext):
                return argumenttext
            else:
                print("Invalid Input: Command Needs an Argument")

        else:
            if check_if_argument_is_not_blank(argumenttext):
                print("Invalid Input: Extra Argument Not Needed")
            else:
                return None

    def validate_argument(self,processedargument):
        temp_command = self.command_dict.get(self.inputed_command)
        argumentlist = temp_command.get_key_list_from_argument_dict()
        if argumentlist is None:
            if processedargument is None:
                self.is_valid_argument = True
            else:
                print("Invalid Input: Invalid Argument Value")
        else:
            if processedargument in argumentlist:
                self.is_valid_argument = True
            else:
                print("Invalid Input: Invalid Argument Value")
