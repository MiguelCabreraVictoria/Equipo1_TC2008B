from agents.car import Car
from agents.person import Person
from model_types.dtos.CellType import CellType
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
            env[f"{x},{y}"] = destinity['destinity'].value

    def add_semaphores(self):
        """
        Agrega los semaforos en en el entorno
        """
        pass

    def add_properties(self, env):
        self.add_sidewalks(env)
        self.add_lanes(env)
        self.add_intersections(env)
        self.add_buildings(env)
        self.add_destinities(env)
        #self.add_semaphores(env)

class CityModel(ap.Model):

    def setup(self):
        self.environment_size = self.p.environment_size
        self.environment = City(self, self.environment_size)
        self.communication_range = self.p.communication_range
        self.num_cars = self.p.num_cars
        self.num_persons = self.p.num_persons
        self.cars = ap.AgentList(self, self.num_cars,Car)
        self.person = ap.AgentList(self, self.num_persons, Person)
        self.max_speed = self.p.max_speed
        self.safe_distance = self.p.safe_distance
        self.semaphore_timelapse = self.p.semaphore_timelapse

        # Agregar propiedades al entorno
        self.environment.add_properties(self.environment)

        # Agregar agentes al entorno
        self.environment.add_agents(self.cars, random=True)
        self.environment.add_agents(self.person, random=True)

    def update_semaphores(self):
        """
        Cambia el estado de los semaforos en funcion al tiempo
        """ 
        pass

    def update(self):
        """
        Actualiza el estados antes de cada paso
        """
        pass

    def step(self):
        self.cars.execute()
        self.person.execute()


model = CityModel(param_01)
model.run(steps=1, display=False)

