import os

class ReportController:
    
    @staticmethod
    def report_make(gifts, graph_gifts):
        my_name = 'Angel Geovanny Ordón Colchaj'
        my_code = '201905741'

        # name = floors.get_floor_name(id_floor)
        # code = patterns.get_pattern_code(id_pattern)

        name_path = "report"

        #path = './resources/reports/report1.html'
        path = f'{name_path}.html'
        f = open(path, 'w', encoding='utf-8')

        # --------------- Inicio html ---------------
        f.write("<!DOCTYPE html>\n")
        f.write("<html lang=\"en\" dir=\"ltr\">\n")
        f.write("   <head>\n")
        f.write("       <meta charset=\"utf-8\">\n")
        f.write("       <title>Reporte</title>\n")
        f.write("       \n")
        f.write("       <script src=\"https://code.jquery.com/jquery-3.1.1.min.js\" crossorigin=\"anonymous\"></script>\n")
        f.write("       <link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css\">\n")
        f.write("       <script src=\"https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.js\"></script>\n")
        f.write("       \n")
        f.write("       <link rel=\"stylesheet\" href=\"./resources/reports/css/style.css\">\n")
        f.write("       \n")
        f.write("       <link rel=\"shortcut icon\" href=\"./resources/reports/img/favicon.ico\" type=\"image/x-icon\">\n")
        f.write("       <link rel=\"icon\" href=\"./resources/reports/img/favicon.ico\" type=\"image/x-icon\">\n")
        f.write("       \n")
        f.write("       <script type=\"text/javascript\" src=\"./resources/reports/scripts/script.js\"></script>\n")
        f.write("   </head>\n")
        f.write("   <body>\n")
        f.write("       <div class=\"ui large top fixed hidden menu\">\n")
        f.write("           <div class=\"ui container\">\n")
        f.write("               <a class=\"active item\">Reporte</a>\n")
        f.write("           </div>\n")
        f.write("       </div>\n")
        f.write("   \n")
        f.write("       <!-- Page Contents -->\n")
        f.write("       <div class=\"ui inverted vertical masthead center aligned segment\" id=\"fondo_usac\">\n")
        f.write("           <div class=\"ui text container\">\n")
        f.write(f"               <h1 class=\"ui inverted header\">Chistmas Puzzle</h1>\n")
        f.write(f"               <h2>Premios</h2>\n")
        f.write("           </div>\n")
        f.write("       </div>\n")
        f.write("       <div class=\"ui vertical stripe\">\n")
        f.write("           <div class=\"ui middle aligned stackable grid container\">\n")

        f.write("               <div class=\"row\">\n")
        f.write("                   <div class=\"two wide column\"></div>\n")
        f.write("                       <div class=\"twelve wide column\">\n")
        f.write("                           <div class=\"ui segment\">\n")
        f.write("                               <h3>Premios</h3>\n")
        f.write(f"                              <img class=\"ui centered medium image\" style=\"width:200px;height:550px;\" src=\"./resources/img/{graph_gifts}.png\">\n")
        f.write("                           </div>\n")
        f.write("                       </div>\n")
        f.write("                   <div class=\"two wide column\"></div>\n")
        f.write("               </div>\n")

        f.write("           </div>\n")
        f.write("       </div>\n")
        f.write("       \n")
        f.write("       <br>\n")
        f.write("       <br>\n")
        f.write("       <br>\n")
        f.write("       <br>\n")
        f.write("       <br>\n")
        f.write("       <br>\n")
        f.write("       <br>\n")
        f.write("       <br>\n")
        f.write("       <br>\n")
        f.write("       <br>\n")
        f.write("       \n")
        f.write("       <div class=\"ui inverted vertical footer segment\">\n")
        f.write("           <div class=\"ui container\">\n")
        f.write("               <div class=\"ui stackable inverted divided equal height stackable grid\">\n")
        f.write("                   <div class=\"three wide column\">\n")
        f.write("                       <h4 class=\"ui inverted header\">USAC</h4>\n")
        f.write("                   </div>\n")
        f.write("                   <div class=\"three wide column\">\n")
        f.write("                       <h4 class=\"ui inverted header\">IPC2 N</h4>\n")
        f.write("                   </div>\n")
        f.write("                   <div class=\"seven wide column\">\n")
        f.write("                       <h4 class=\"ui inverted header\">Proyecto 1</h4>\n")
        f.write("                       <p>Angel Geovanny Ordon Colchaj - 201905741</p>\n")
        f.write("                   </div>\n")
        f.write("               </div>\n")
        f.write("           </div>\n")
        f.write("       </div>\n")
        f.write("   </body>\n")
        f.write("   \n")
        f.write("</html>\n")
        # --------------- Fin html ---------------

        f.close()
        print("--------------------")
        print("Reporte Generado Exitosamente")
        print("--------------------")
        return path