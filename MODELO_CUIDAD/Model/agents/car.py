import agentpy as ap


from model_types.dtos.CarStatus import CarStatus
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
        
        if len(detected_agents) > 1:
            self.status = CarStatus.STOPPED
            self.speed = 0
            
            print(f'{len(detected_agents)} agents detected')
            for agent in detected_agents:
                if agent != self: 
                    print(f"Car {self.id} detected {agent} {agent.id} at {agent.get_position()}")
                    

    def calculate_path(self):
        """
        Calcula el camino optimo hacia el destino del coche

        Nota: Se busca impl  print("person")
        self.calculate_path()
        print(self.path)ementar el algoritmo A * para calcular el camino optimo
        """

        start = self.get_position()
        goal = self.destinity
        goal_coordinates = [destination['coordinates'] for destination in self.env.destinities if destination['destinity'] == goal][0]
        self.path = A_star.find_path(self.model.routes_network, start, goal_coordinates, 'car')
            


    def wait_semaphore(self):
        """
        Espera en el semaforo si esta en rojo
        """
        pass

    def search_gas_station(self):
        """
        Busca la estacion de servicio mas cercana si el combustible es bajo
        """
        pass

    def refill_fuel(self):
        """
        Recarga combustible en un estacion de servicio
        """
        pass

    def in_destiny(): 
        """
        Verifica si el coche ha llegado a su destino
        """
        pass 

    def move(self):
        """
        Mueve el coche en funcion de su velocidad y camino calculado
        """
        
        if len(self.path) > 0:
            print('no path')
            
        
        if len(self.path) > 0:
            next_position = self.path.pop(0)
            self.env.move_agent(self, next_position)


    def communicate(self, recipient, message):
        """
        @param recipient: Agente destinatario del mensaje
        @param message: Contenido del mensaje

        Envia un mensaje a otro agente

        """
        pass

    def execute(self):
        """
        Ejecuta las acciones del coche en cada paso de simulacion

        """
        self.calculate_path()
        self.info()
 
