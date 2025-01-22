import agentpy as ap

class Person(ap.Agent):
    def setup(self):
        self.position = None
        self.destinity = None
        self.status 
        self.path = []
        self.mailbox = []

    def get_position(self):
        """
        Obtiene la posicion actual del individuo
        """
        pass

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
        pass
