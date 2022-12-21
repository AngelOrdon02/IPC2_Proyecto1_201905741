import xml.etree.ElementTree as ET

# Modelos
from models.user import User

class ProcessorController:

    @staticmethod
    def data_processor(filepath, users):
        tree = ET.parse(filepath)
        root = tree.getroot()

        position_user = users.last_node()

        for r in root:

            position_user += 1

            personal_info = r.text.replace('\n', '')
            puzzle = r.text.replace('\n', '')

            # personal_info = r[0]
            name = r[0][0]
            age = r[0][1]

            movements = r[1]
            size = r[2]
            figure = r[3]
            puzzle = r[4]

            # print(movements.text)
            # print(size.text)
            # print(figure.text)

            users.insert_last(User(position_user, name.text, age.text, movements.text, size.text, figure.text, 1, 1))
            # print(puzzle.text)