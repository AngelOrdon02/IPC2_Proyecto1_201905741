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

            # personal_info = r.text.replace('\n', '')
            puzzle_data = r.text.replace('\n', '')
            solution_data = r.text.replace('\n', '')

            # personal_info = r[0]
            name = r[0][0]
            age = r[0][1]

            movements = r[1]
            size = r[2]
            figure = r[3]
            puzzle_data = r[4]
            solution_data = r[5]

            # Puzzle desarrogrado
            for cell in puzzle_data:
                x = cell.get('f')
                y = cell.get('c')
                print("(" + x + ", " + y + ")")

            print()

            # Solucion del puzzle
            for cell in solution_data:
                x = cell.get('f')
                y = cell.get('c')
                print("(" + x + ", " + y + ")")

            # print(movements.text)
            # print(size.text)
            # print(figure.text)

            users.insert_last(User(position_user, name.text, age.text, movements.text, size.text, figure.text, 1, 1))
            # print(puzzle.text)