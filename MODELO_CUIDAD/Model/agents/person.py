import agentpy as ap

from Model.model_types.dtos.PersonStatus import PersonStatus
from Model.A_star import A_star

# TODO: Save the path and info about the person, to send it to the server

class Person(ap.Agent):
    def setup(self):
        self.env = self.model.environment
        self.position = None
        self.destinity = None
        self.destinity_coordinates = None
        self.status = None
        self.path = []
        self.mailbox = []
        self.info_added = False

    def info(self):
        """
        Muestra la informacion del individuo
        """
        # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print('This is a person')
        # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++n")
        # print(f"Person {self.id} is in position {self.get_position()}")
        # print(f"Person {self.id} has a status of {self.status.value}")
        # print(f"Person {self.id} is going to {self.destinity.value}")
        # print(f"Person {self.id} has a path of {self.path}")
        # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


        info = {
            'id': self.id,
            'type': 'Person',
            'position': list(self.get_position()),
            'status': self.status.value,
            'destinity': self.destinity.value
        }

        if self.status == PersonStatus.IN_DESTINY and not self.info_added:
            self.info_added = True
            #print(info)
            self.model.model_data.append(info)
        
        if self.status != PersonStatus.IN_DESTINY:
            #print(info)
            self.model.model_data.append(info)
    

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
        goal = self.destinity_coordinates
        
        self.path = A_star.find_path(self.model.routes_network, start, goal, 'person')
        # print(f"Person {self.id} has a path of {self.path}")
            

    def in_destiny(self):
        """
        Verifica si el individuo ha llegado a su destino
        """
        if self.get_position() == self.destinity_coordinates:
            self.status = PersonStatus.IN_DESTINY
            # print(f"Person {self.id} is in destiny, {self.destinity.value}")
                    
    
    def move(self):
        """
        Mueve al individuo en la direccion del camino
        """

        if self.status == PersonStatus.IN_MOVEMENT:
            if self.path:

                next_position = self.path.pop(0)
                self.env.move_to(self, next_position)
                # print(f"Person {self.id} moved to {next_position}, {self.status.value}")
        
        self.in_destiny()
    
    
    
    def check_collision(self, next_position):
        return any(agent.get_position() == next_position for agent in self.env.agents)
    
        
    def execute(self):
        """
        Ejecuta las acciones del individuo en cada paso de la simulacion
        """
        self.info()
        self.move()

        
        
      