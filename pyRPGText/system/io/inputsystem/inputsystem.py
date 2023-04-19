from pyRPGText.system.io.inputsystem.command import command


class inputSystem:
    def __init__(self):
        self.inputedCommand = None
        self.inputedArgument = None
        self.isValidCommand = False
        self.isValidArgument = False
        self.commandDict={}

    def resetAll(self):
        self.inputedCommand = None
        self.inputedArgument = None
        self.isValidCommand = False
        self.isValidArgument = False
        self.commandDict = {}
    def addCommand(self,text,function):
        inputCommand= command(text,function)
        inputCommand.argumentDict = None
        self.commandDict[inputCommand.getText()] = inputCommand

    def addArgumentToCommand(self, commandText,argumentName,argumentValue):
        if commandText in self.commandDict.keys():
            command = self.commandDict.get(commandText)
            command.addArgument(argumentName,argumentValue)
    def getInput(self):
        while True:
            userInput = input("Command-> ")
            self.inputedCommand, self.inputedArgument = self.lexUserInput(userInput)
            print(f"{self.inputedCommand}:{self.inputedArgument}")


    def lexUserInput(self, userInput):
        command = f""
        argumment = f""
        for index, char in enumerate(userInput):
            command = command+char
            if command in self.commandDict.keys():
                break
            elif command not in self.commandDict.keys() and index == len(userInput) - 1:
                command = None
                break
        if command is not None:
            argumentText = userInput.replace(command, "")
            argumentText = argumentText.strip()
            argumentTextNotBlank = bool(argumentText and not argumentText.isspace())
            commandFromDict = self.commandDict.get(command)
            if commandFromDict.getKeyListFromArgumentDict() is not None:
                if argumentTextNotBlank:
                    argumment = argumentText
                    print("You arrived at your Destination") #toDo: Adicionar Validação para o argumento nos dois pontos onde da tudo certo
                else:
                    argumment = None
                    print("Invalid Input: Command Needs an Argument")
            else:
                if argumentTextNotBlank:
                    print("Invalid Input: Extra Argument Not Needed")
                    argumment = None
                else:
                    argumment = argumentText
                    print("You arrived at your Destination")


        return (command, argumment)


