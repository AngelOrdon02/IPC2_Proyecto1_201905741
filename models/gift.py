'''
* Regalo (Gift)
- id (id)
- lugar (place)
- descripcion (description)
'''

from models.node import Node

class Gift():

    def __init__(self, id, place, description):
        self.id = id
        self.place = place
        self.description = description