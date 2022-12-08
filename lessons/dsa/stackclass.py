class stackbase:

    def __init__(self, stackname, type):
        """ Initialise a stack """

        self._stackname = stackname
        self._type = type

    def create_stack(self):
        """ Create stack """

        self._stackname = {}

        return self._stackname

    def init_stack(self):
        """Initialise an empty stack"""

        return len(self._stackname) == 0

    def push(self, name, value):
        """ Add records to the stack """

        self._stackname[name] = value

        print("{}'s {} added.".format(name, self._type))

    def pop(self):
        if self.init_stack:
            print("Stack is empty!")

        return self._stackname.pop()