"""
A file for exceptions to be used within the program
"""


class HealthBarNotFound(Exception):
    """Raised when the program cannot find the health bar on screen."""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = self.__doc__

    def __str__(self):
        return self.message


class InstanceNotInitialized(Exception):
    """This instance has not been initialized."""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = self.__doc__

    def __str__(self):
        return self.message
