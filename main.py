'''
Angel Geovanny Ordon Colchaj
201905741
'''

# Importando librerias
import os, subprocess, sys

# Importando controladores
from controllers.filereaderController import FilereaderController
from controllers.processorController import ProcessorController
from controllers.simpleListController import SimpleListController
from controllers.grapherController import GrapherController
from controllers.reportController import ReportController

# Instancias
filereader_Controller = FilereaderController()
processor_controller = ProcessorController()
grapher_controller = GrapherController()
report_controller = ReportController()

# Instancia de arreglos
users = SimpleListController()
gifts = SimpleListController()

# ---------- Limpiador de consola ----------

def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        subprocess.call('clear', shell=True)

def open_file(filename):
    if sys.platform == 'win32':
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

# ------------------------------------------

print("Bienvenido")
print("Christmas Puzzle")
print("")

def menu():
    print("(1) Carga de configuración")
    print("(2) Carga de premios")
    print("(3) Opcion 3")
    print("(4) Salir")
    entry = str(input("Ingrese una opcion: "))
    return entry

cycle = True
while(cycle):
    entry = menu()
    if entry == "1":
        print("")
        print("Opcion 1")
        print("")

        # Codigo de lectura del archivo
        filepath = filereader_Controller.file_reader()
        
        if filepath is None:
            print("- Ningun archivo seleccionado \n")
        else:
            # print("filepath: " + filepath)
            processor_controller.data_processor(filepath, users)

        input("")
    elif entry == "2":
        print("")
        print("Opcion 2")
        print("")

        # Codigo de lectura del archivo
        filepath = filereader_Controller.file_reader()
        
        if filepath is None:
            print("- Ningun archivo seleccionado \n")
        else:
            # print("filepath: " + filepath)
            processor_controller.data_processor_2(filepath, gifts)

        input("")
    elif entry == "3":
        print("")
        print("Opcion 3")
        print("")

        print("---------- Usuarios ----------")
        users.show_list()

        print("---------- Premios ----------")
        gifts.show_gifts()

        # Grafico
        graph_gifts = grapher_controller.gifts_grapher(gifts)

        # Reporte
        path = report_controller.report_make(gifts, graph_gifts)
        os.system(path)
        
        input("")
    elif entry == "4":
        print("")
        print("Gracias por utilizar el programa")
        print("")
        print(" ░██████╗░██████╗░░█████╗░░█████╗░██╗░█████╗░░██████╗\n" +
                "██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗██╔════╝\n" +
                "██║░░██╗░██████╔╝███████║██║░░╚═╝██║███████║╚█████╗░\n" +
                "██║░░╚██╗██╔══██╗██╔══██║██║░░██╗██║██╔══██║░╚═══██╗\n" +
                "╚██████╔╝██║░░██║██║░░██║╚█████╔╝██║██║░░██║██████╔╝\n" +
                "░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝╚═╝░░╚═╝╚═════╝░")
        input("")
        cycle = False
    else:
        print("")
        print("Ingrese una opcion valida")
        input("")
    clear()