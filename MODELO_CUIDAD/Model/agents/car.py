import agentpy as ap


class Car(ap.Agent):
    def setup(self):
        self.env = self.model.environment
        self.position = None
        self.speed = self.p.cars_initial_speed
        self.destinity = ""
        self.status = ""
        self.fuel = self.p.cars_initial_fuel
        self.path = []
        self.mailbox = []

    def get_position(self):
        """
        Obtiene la posicion actual del coche 
        """
        return self.env.positions[self]

    def avoid_collision(self):
        """
        Evita colisiones detectando agentes cercanos
        """
        pass

    def calculate_path(self):
        """
        Calcula el camino optimo hacia el destino del coche
        """
        pass

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
        pass

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
        print(f"Car {self.id} is executing")
        print(f"Car {self.id} is in position {self.get_position()}")
     
 
