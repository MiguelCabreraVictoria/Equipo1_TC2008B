import agentpy as ap
import numpy as np 
import random

from model_types.dtos.CarStatus import CarStatus
from model_types.dtos.SemaphoreLight import SemaphoreLight
from A_star import A_star

class Car(ap.Agent):
    def setup(self):
        self.env = self.model.environment
        self.position = None
        self.speed = self.p.cars_initial_speed
        self.destinity = None
        self.status = None
        self.fuel = self.p.cars_initial_fuel
        self.path = []
        self.mailbox = []

    def info(self):
        """
        Muestra la informacion del coche
        """
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print('This is a car')
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"Car {self.id} is in position {self.get_position()}")
        print(f"Car {self.id} has a status of {self.status.value}")
        print(f"Car {self.id} has a speed of {self.speed}")
        print(f"Car {self.id} has a fuel of {self.fuel}")
        print(f"Car {self.id} is going to {self.destinity.value}")
        print(f"Car {self.id} has a path of {self.path}")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

    def get_position(self):
        """
        Obtiene la posicion actual del coche 
        """
        return self.env.positions[self]

    def avoid_collision(self):
        """
        Evita colisiones detectando agentes cercanos
        """

        detected_agents = self.env.neighbors(self, distance=self.p.safe_distance)
        
        # Filtrar agentes que esten en posiciones diagonales
        filtered_agents = []
        current_position = self.get_position()

        for agent in detected_agents:
            if agent != self:
                # Calcular distancia en las coodenadas x y y
                agent_position = agent.get_position()
                dx = abs(agent_position[0] - current_position[0])
                dy = abs(agent_position[1] - current_position[1])

                if dx + dy == 1:
                    filtered_agents.append(agent) 


        if len(filtered_agents) > 0:
            for agent in filtered_agents:
                agent_type = agent.__class__.__name__
                if agent_type == 'Person':
                    print(f"Car {self.id} is stopping because of a person")
                    self.status = CarStatus.STOPPED
                    self.speed = 0
                elif agent_type == 'Car':
                    if self.check_mailbox(agent.id):
                        print(f"Car {agent.id} is already stopped")
                        
                    else:
                        message = f"Car {self.id} is stopping because of a car {agent.id}"
                        print(message)
                        self.status = CarStatus.STOPPED
                        self.speed = 0
                        self.communicate('position', agent, message=message)
        
   

        if self.status == CarStatus.STOPPED and len(filtered_agents) == 0:
            self.status = CarStatus.IN_MOVEMENT
            self.speed = self.p.cars_initial_speed
            print(f"Car {self.id} started moving again")
        

                    

    def calculate_path(self):
        """
        Calcula el camino optimo hacia el destino del coche

        self.calculate_path()
        print(self.path)ementar el algoritmo A * para calcular el camino optimo
        """

        start = self.get_position()
        goal = self.destinity
        goal_coordinates = [destination['coordinates'] for destination in self.env.destinities if destination['destinity'] == goal][0]
        self.path = A_star.find_path(road_network=self.model.routes_network, start=start, goal=goal_coordinates, agent_type='car')


    def get_semphore_state(self):
        """
        Obtiene el estado del semaforo en la posicion actual
        """

        x, y = self.get_position()
        
        x_safe_distance = x + self.p.safe_distance
        y_safe_distance = y + self.p.safe_distance

        for semaphore in self.env.semaphores:
            if semaphore['position'] == (x_safe_distance, y) or semaphore['position'] == (x, y_safe_distance):
                return semaphore['state']
        
        # print(f"No semaphore found ")
        return None
    

    def wait_semaphore(self):
        """
        Espera en el semaforo si esta en rojo
        """
        state = self.get_semphore_state()
        
        if state is None:
            return
        if state == SemaphoreLight.RED:
            print(f"Car {self.id} is waiting at semaphore")
            self.status = CarStatus.WAITING
            self.speed = 0


    def search_gas_station(self):
        """
        Busca la estacion de servicio mas cercana si el combustible es bajo
        """
        pass


    def refill_fuel(self):
        """
        Recarga combustible en un estacion de servicio
        """
        self.fuel = 100


    def in_destiny(self): 
        """
        Verifica si el coche ha llegado a su destino
        """
        for destination in self.env.destinities:
            if self.destinity.value == destination['destinity']:
                if destination['coordinates'] == self.get_position():
                    self.status = CarStatus.IN_DESTINY
                    print(f"Car {self.id} is in destiny")

        

    def communicate(self,mesage_type,recipient, message):
        """
        @param recipient: Agente destinatario del mensaje
        @param message: Contenido del mensaje

        Envia un mensaje a otro agente

        """
        recipient.mailbox.append({
            'type': mesage_type,
            'sender': self.id,
            'message': message
        })
        # print(f"Car {self.id} sent a message to {recipient.__class__.__name__}: {message}")

    def check_mailbox(self, sender_id):
        """
        """

        for message in self.mailbox:
            if message['sender'] == sender_id:
                self.mailbox.clear()
                return True
            else:
                return False
            
    def move(self):
        """
        Mueve el coche en funcion de su velocidad y camino calculado
        """
        self.avoid_collision()
        self.wait_semaphore()

        if self.status == CarStatus.IN_MOVEMENT and self.fuel > 0:
            if self.path:
                next_position = self.path.pop(0)
                self.env.move_to(self, next_position)
                print(f"Car {self.id} moved to {next_position}, {self.status.value}")
            self.fuel -= 7
        
        self.in_destiny()

    def execute(self):
        """
        Ejecuta las acciones del coche en cada paso de simulacion

        """

        # self.info()
        self.move()
        
 
