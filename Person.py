# Class
class Person():
    def __init__(self, name="Person"):
        self._name = name
        self._connections = []

    def is_Jen(self):
        return self._name == "Jen"
    
    def get_possible_sets(self):
        if len(self._connections) == 0:
            return (0 if self.is_Jen() else 2)
        
        size = 1
        for person in self._connections:
            size *= person.get_possible_sets()
        return (size if self.is_Jen() else size+1)

    def add_multiple(self, num):
        for i in range(num):
            self.add_connection()
            
    def add_connection(self):
        connect_num = len(self._connections) + 1
        connect_name = f"{self._name}_{connect_num}"
        new_connect = Person(name=connect_name)
        self._connections.append(new_connect)
        return new_connect
    
    def get_tree(self):
        if len(self._connections) == 0:
            return self._name
        else:
            sub_names = [person.get_tree() for person in self._connections]
            names = [f"Head - {self._name}", sub_names]
            return f"Head - {self._name}", sub_names
            
    @property
    def connections(self):
        return self._connections

