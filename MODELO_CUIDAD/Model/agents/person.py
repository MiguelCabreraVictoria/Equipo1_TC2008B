import agentpy as ap

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
        print(f"Person {self.id} has a status of {self.status}")
        print(f"Person {self.id} is going to {self.destinity.value}")
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

    def in_destiny(self):
        """
        Verifica si el individuo ha llegado a su destino
        """

    def execute(self):
        """
        Ejecuta las acciones del individuo en cada paso de la simulacion
        """
        self.info()