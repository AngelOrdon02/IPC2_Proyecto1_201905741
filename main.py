'''
Angel Geovanny Ordon Colchaj
201905741
'''

# Importando librerias
import os, subprocess, sys

# Importando controladores
# from controllers.floorController import FloorController

# Instancias
# floors = FloorController()

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
    print("(1) Opcion 1")
    print("(2) Opcion 2")
    print("(3) Salir")
    entry = str(input("Ingrese una opcion: "))
    return entry

cycle = True
while(cycle):
    entry = menu()
    if entry == "1":
        print("")
        print("Opcion 1")
        print("")

        input("")
    elif entry == "2":
        print("")
        print("Opcion 2")
        print("")

        input("")
    elif entry == "3":
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