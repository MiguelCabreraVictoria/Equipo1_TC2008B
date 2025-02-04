from agents.car import Car
from agents.person import Person
from model_types.dtos.CellType import CellType
from model_types.dtos.SemaphoreLight import SemaphoreLight
from model_types.dtos.CarStatus import CarStatus
from model_types.dtos.PersonStatus import PersonStatus
from parameters.param_01 import param_01

import agentpy as ap
import numpy as np
import random 

class City(ap.Grid):
    def setup(self):

        
        self.sidewalks = self.p.sidewalks
        self.lanes = self.p.lanes
        self.intersections = self.p.intersections
        self.buildings = self.p.buildings
        self.destinities = self.p.destinities
        self.semaphores = self.p.semaphores

        
    def add_sidewalks(self, env):
        """
        Agrega las banquetas en en el entorno
        """
        for x, y in self.sidewalks:
            env[f"{x},{y}"] = CellType.SIDEWALK.value

    def add_lanes(self, env):
        """
        Agrega los carriles en en el entorno
        """
        for x, y in self.lanes:
            env[f"{x},{y}"] = CellType.LANE.value

    def add_intersections(self, env):
        """
        Agrega las intersecciones en en el entorno
        """
        for x, y in self.intersections:
            env[f"{x},{y}"] = CellType.INTERSECTION.value

    def add_buildings(self, env):
        """
        Agrega los edificios en en el entorno
        """
        for x, y in self.buildings:
            env[f"{x},{y}"] = CellType.BUILDING.value

    def add_destinities(self,env):
        """
        Agrega los destinos en en el entorno
        """
        for destinity in self.destinities:
            x, y = destinity['coordinates']
            env[f"{x},{y}"] = CellType.DESTINITY.value

    def add_semaphores(self, env):
        """
        Agrega los semaforos en en el entorno
        """
        for semaphore in self.semaphores:
            x, y = semaphore['position']
            env[f"{x},{y}"] = semaphore['state'].value

    def add_properties(self, env):
        self.add_sidewalks(env)
        self.add_lanes(env)
        self.add_intersections(env)
        self.add_buildings(env)
        self.add_destinities(env)
        self.add_semaphores(env)

class CityModel(ap.Model):

    def setup(self):
        self.environment_size = self.p.environment_size
        self.environment = City(self, self.environment_size)
        self.communication_range = self.p.communication_range
        self.num_cars = self.p.num_cars
        self.num_persons = self.p.num_persons
        self.cars = ap.AgentList(self, self.num_cars,Car)
        self.persons = ap.AgentList(self, self.num_persons, Person)
        self.max_speed = self.p.max_speed
        self.safe_distance = self.p.safe_distance
        self.semaphore_timelapse = self.p.semaphore_timelapse

        # Agregar propiedades al entorno
        self.environment.add_properties(self.environment)

        # Agregar agentes al entorno
        self.environment.add_agents(self.cars, random=True)
        self.environment.add_agents(self.persons, random=True)

        # Asignar destinos a los agentes
        self.agents_destination()

        # Asignar estado inicial a los agentes
        self.agent_status()

        # Generar la red de rutas, para el calculo de caminos
        self.routes_network = self.generate_routes_network()

        self.generate_paths()

        self.agents_not_in_buildings()

    def agents_destination(self):
        """
        Asigna los destinos a los agentes
        """

        for idx, car in enumerate(self.cars):
            car.destinity = self.p.cars_destinities[idx]

        for idx, person in enumerate(self.persons):
            person.destinity = self.p.persons_destinities[idx]

    def generate_routes_network(self):
        
        route_network = []
        m, n = self.environment.shape

        for x in range(m):
            idx_row = []
            for y in range(n):
                # print(self.environment[f'{x},{y}'])
                idx_row.append(self.environment[f'{x},{y}'])
            # print(idx_row)
            route_network.append(idx_row)
        
        route_network = np.array(route_network)
        # print(road_network)
        # print(road_network.shape)
        return route_network   

    def generate_paths(self):
        """
        Genera los caminos optimos para los agentes
        """
        for car in self.cars:
            car.calculate_path()

        for person in self.persons:
            person.calculate_path()    
    
    def agent_status(self):
        """
        Asigna el estado inicial a los agentes
        """
        
        for idx, car in enumerate(self.cars):
            car.status = CarStatus.IN_MOVEMENT

        for person in self.persons:
            person.status = PersonStatus.IN_MOVEMENT

    def update_semaphores(self):
        """
        Cambia el estado de los semaforos en funcion al tiempo
        """ 
        # print("Updating semaphores")
        for semaphore in self.environment.semaphores:
            x, y = semaphore['position']
            if semaphore['state'] == SemaphoreLight.GREEN:
                # print(f'Changing semaphore {x},{y} to YELLOW')
                semaphore['state'] = SemaphoreLight.YELLOW
            elif semaphore['state'] == SemaphoreLight.RED:
                # print(f'Changing semaphore {x},{y} to GREEN')
                semaphore['state'] = SemaphoreLight.GREEN
            elif semaphore['state'] == SemaphoreLight.YELLOW:
                # print(f'Changing semaphore {x},{y} to RED')
                semaphore['state'] = SemaphoreLight.RED

    def agents_not_in_buildings(self):
        actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        new_x, new_y = random.choice(actions)
        
        for person in self.persons:
            if person.get_position() in self.p.buildings:
                # print(f"Person {person.id} is in a building at {person.get_position()}")
                x, y = person.get_position()
                pos_x, pos_y = x + new_x, y + new_y
                self.environment.move_to(person, (pos_x, pos_y))
                # print(f"Person {person.id} is moving to {(pos_x, pos_y)}")
                person.calculate_path()

        for car in self.cars:
            if car.get_position() in self.p.buildings:
                # print(f"Car {car.id} is in a building at {car.get_position()}")
                x, y = car.get_position()
                pos_x, pos_y = x + new_x, y + new_y
                self.environment.move_to(car, (pos_x, pos_y))
                # print(f"Car {car.id} is moving to {(pos_x, pos_y)}")
                car.calculate_path()


    def update(self):
        """
        Actualiza el estados antes de cada paso
        """

        if self.t % self.semaphore_timelapse == 0:
            self.update_semaphores()

    def step(self):
        
      


        self.agents_not_in_buildings()
        # self.cars.execute()
        self.persons.execute()

        


    def end(self):
        print('Simulation has ended')
        


model = CityModel(param_01)
model.run(steps=100, display=False)





