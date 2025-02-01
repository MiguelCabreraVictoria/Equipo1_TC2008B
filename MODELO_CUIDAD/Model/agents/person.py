import agentpy as ap



from A_star import A_star

class Person(ap.Agent):
    def setup(self):
        self.env = self.model.environment
        self.position = None
        self.destinity = None
        self.status = ""
        self.path = []
        self.mailbox = []

    def info(self):
        """
        Muestra la informacion del individuo
        """
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print('This is a person')
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++n")
        print(f"Person {self.id} is in position {self.get_position()}")
        print(f"Person {self.id} has a status of {self.status.value}")
        print(f"Person {self.id} is going to {self.destinity.value}")
        print(f"Person {self.id} has a path of {self.path}")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    def get_position(self):
        """
        Obtiene la posicion actual del individuo
        """
        return self.env.positions[self]

    def calculate_path(self):
        """
        Calcula el camino optimo hacia el destino del individuo
        """

        start = self.get_position()
        goal = self.destinity
        goal_coordinates = [destination['coordinates'] for destination in self.env.destinities if destination['destinity'] == goal][0]
        self.path = A_star.find_path(self.model.routes_network, start, goal_coordinates, 'person')
            

    def in_destiny(self):
        """
        Verifica si el individuo ha llegado a su destino
        """

    def execute(self):
        """
        Ejecuta las acciones del individuo en cada paso de la simulacion
        """
        self.calculate_path()
        self.info()
        
      