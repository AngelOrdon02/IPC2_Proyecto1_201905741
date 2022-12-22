from models.node import Node

class SimpleListController():

    def __init__(self):
        self.head = None
        self.end = None
        self.size = 0

    # Método para agregar elementos al final de la linked list
    def insert_last(self, fact):
        new = Node(fact = fact)
        self.size += 1
        if self.head is None:
            self.head = new
            self.end = new
        else:
            tmp = self.head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = new
            self.end = new
    
    # Método para imprimir la lista de nodos
    def show_list(self):
        node = self.head
        while node != None:
            #print( getattr(node.fact, key)  ," => ")
            print( "id: " + str(getattr(node.fact, 'id')))
            print( "name: " + str(getattr(node.fact, 'name')))
            print( "age: " + str(getattr(node.fact, 'age')))
            node = node.next

    # Retorna el id del ultimo nodo
    def last_node(self):
        tmp = self.end
        id = 0
        if tmp is None:
            pass
        else:
            id = getattr(tmp.fact, 'id')
        return id
        #return getattr(temp.fact, 'id')

    # Tamaño del nodo
    def cont_node(self):
        return self.size

    # Método para borrar lista
    def wipe(self):
        tmp = self.head

        if (tmp is None):
            print("- Esta vacia")
        while tmp:
            self.head = tmp.next
            tmp = None
            tmp = self.head
    
    # ====================== Premio (Gift) ==============================
    # Método para buscar empresa y retornar id
    # def get_id_business(self, code_business):
    #     tmp = self.head

    #     for i in range(self.size):
    #         if ((getattr(tmp.fact, 'code')) == str(code_business)):
    #             id_business = getattr(tmp.fact, 'id')
    #             return id_business
    #         else:
    #             tmp = tmp.next

    # Método para imprimir la lista de nodos
    def show_gifts(self):
        node = self.head
        while node != None:
            #print( getattr(node.fact, key)  ," => ")
            print( "id: " + str(getattr(node.fact, 'id')))
            print( "Lugar: " + str(getattr(node.fact, 'place')))
            print( "Descripción: " + str(getattr(node.fact, 'description')))
            node = node.next

    # ============================ FIN =======================================
