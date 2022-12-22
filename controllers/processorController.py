import xml.etree.ElementTree as ET

# Modelos
from models.user import User
from models.gift import Gift

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

            if (int(size.text) <= 30):
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

                # Add lista
                print("Es menor a 30")
                users.insert_last(User(position_user, name.text, age.text, movements.text, size.text, figure.text, 1, 1))
    
    @staticmethod
    def data_processor_2(filepath, gifts):
        tree = ET.parse(filepath)
        root = tree.getroot()

        position_gift = gifts.last_node()

        for r in root:

            position_gift += 1

            place = r[0]
            description = r[1]

            # print(place.text)
            # print(description.text)
            gifts.insert_last(Gift(position_gift, place.text, description.text))
