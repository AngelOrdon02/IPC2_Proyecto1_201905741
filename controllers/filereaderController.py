from tkinter import filedialog, Tk
#from tkinter.filedialog import askopenfilename

class FilereaderController:

    @staticmethod
    def file_reader():
        Tk().withdraw()
        filepath = filedialog.askopenfile(
            title = "Selecciona un archivo XML",
            initialdir = "./",
            filetypes = (
                ("Archivos XML", "*.xml"),
                ("Todos los archivos", "*.*")
            )
        )

        if filepath is None:
            print("- Ningun archivo seleccionado \n")
            return None
        else:
            path = filepath.name
            print("- Lectura exitosa \n")
            return path