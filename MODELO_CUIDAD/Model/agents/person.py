import agentpy as ap
import random

from model_types.dtos.PersonStatus import PersonStatus
from A_star import A_star

class Person(ap.Agent):
    def setup(self):
        self.env = self.model.environment
        self.position = None
        self.destinity = None
        self.status = None
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
        for destination in self.env.destinities:
            if destination['coordinates'] == self.get_position():
                self.status = PersonStatus.IN_DESTINY
                print(f"Person {self.id} is in destiny")
    
        
    def move(self):
        """
        Mueve al individuo en la direccion del camino
        """
        if self.path:

            next_position = self.path.pop(0)
            self.env.move_to(self, next_position)
            print(f"Person {self.id} moved to {next_position}, {self.status.value}")
            self.in_destiny()
    
    
    
    def check_collision(self, next_position):
        return any(agent.get_position() == next_position for agent in self.env.agents)
    
        




        
    def execute(self):
        """
        Ejecuta las acciones del individuo en cada paso de la simulacion
        """
       
        self.move()
        # self.info()
        
        
      