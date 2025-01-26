import agentpy as ap

class Person(ap.Agent):
    def setup(self):
        self.env = self.model.environment
        self.position = None
        self.destinity = None
        self.status = ""
        self.path = []
        self.mailbox = []

    def get_position(self):
        """
        Obtiene la posicion actual del individuo
        """
        return self.env.positions[self]

    def calculate_path(self):
        """
        Calcula el camino optimo hacia el destino del individuo
        """

    def in_destiny(self):
        """
        Verifica si el individuo ha llegado a su destino
        """

    def execute(self):
        """
        Ejecuta las acciones del individuo en cada paso de la simulacion
        """
        print(f"Person {self.id} is executing")
        print(f"Person {self.id} is in position {self.get_position()}")