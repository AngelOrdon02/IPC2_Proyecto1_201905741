class Node():

    def __init__(self, fact = None, next = None):
        self.fact = fact
        self.next = next

    def getFact(self):
        return self.fact