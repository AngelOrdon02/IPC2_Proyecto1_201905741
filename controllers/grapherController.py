import os

class GrapherController:

    @staticmethod
    def gifts_grapher(gifts):
        
        # row = floors.get_floor_row(id_floor)
        # column = floors.get_floor_column(id_floor)

        # chain = patterns.get_pattern_grapher(id_pattern)

        # name = floors.get_floor_name(id_floor)
        # code = patterns.get_pattern_code(id_pattern)

        name_path = "gifts"

        cont = 0

        path = f'./resources/dot/{name_path}.dot'
        file = open(path, "w")

        # --------------- Inicio dot ---------------
        file.write("digraph G{\n")

        file.write("    subgraph cluster_1 {\n")
        file.write("        node [style=\"filled\"];\n")
        # file.write("        b0 -> b1 -> b2 -> b3;\n")
        file.write("            b0 -> b1;\n")
        file.write("            b1 -> b2;\n")
        file.write("            b2 -> b3;\n")
        file.write("        label = \"Top #10\";\n")
        file.write("        color=\"blue\"\n")
        file.write("    }\n")
        # file.write("    ")

        # file.write("graph [ dpi = 300 ];\n")
        # file.write("a0 [shape=none label=<\n")
        file.write("}")
        # --------------- Fin dot ---------------

        file.close()
        
        name_dot = f'{name_path}.dot'
        name_png = f'{name_path}.png'
        os.system(f"dot -Tpng ./resources/dot/{name_dot} -o ./resources/img/{name_png}")

        return name_path