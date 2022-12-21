'''
* Usuario (User)
- id (id)
- nombre (name)
- edad (age)
- movimientos (movements)
- tamaño (size)
- figura (figure)
- id_puzzle (id_puzzle)
- id_solution (id_solution)
'''

from models.node import Node

class User():

    def __init__(self, id, name, age, movements, size, figure, id_puzzle, id_solution):
        self.id = id
        self.name = name
        self.age = age
        self.movements = movements
        self.size = size
        self.figure = figure
        self.id_puzzle = id_puzzle
        self.id_solution = id_solution