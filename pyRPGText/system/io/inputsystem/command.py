from pyRPGText.system.io.inputsystem.argument import argument


class command:
    def __init__(self, text,function):
        self.argumentDict= {}
        self.text = text
        self.function = function

    def getText(self):
        return self.text
    def getKeyListFromArgumentDict(self):
        return self.argumentDict.keys()
    def addArgument(self,argumentName, argumentValue):
        inputArgument = argument(argumentName,argumentValue)
        if self.argumentDict is None:
            self.argumentDict = {}
        self.argumentDict[inputArgument.getName()] = inputArgument