from agents.car import Car
from agents.person import Person

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

    def add_sidewalks(self):
        """
        Agrega las banquetas en en el entorno
        """
        pass

    def add_lanes(self):
        """
        Agrega los carriles en en el entorno
        """
        pass

    def add_intersections(self):
        """
        Agrega las intersecciones en en el entorno
        """
        pass

    def add_buildings(self):
        """
        Agrega los edificios en en el entorno
        """
        pass

    def add_destinities(self):
        """
        Agrega los destinos en en el entorno
        """
        pass

    def add_semaphores(self):
        """
        Agrega los semaforos en en el entorno
        """
        pass

    def add_properties(self):
        self.add_sidewalks()
        self.add_lanes()
        self.add_intersections()
        self.add_buildings()
        self.add_destinities()
        self.add_semaphores()

class CityModel(ap.Model):

    def setup(self):
        self.environment_size = self.p.environment_size
        self.environment = City(self, self.environment_size)
        self.communication_range = self.p.communication_range
        self.num_cars = self.p.num_cars
        self.num_persons = self.p.num_persons
        self.cars = ap.AgentList(self, self.num_cars, Car)
        self.person = ap.AgentList(self, self.num_persons, Person)
        self.max_speed = self.p.max_speed
        self.safe_distance = self.p.state_distance
        self.semaphore_timelapse = self.p.semaphore_timelapse

    def update_semaphores(self):
        """
        Cambia el estado de los semaforos en funcion al tiempo
        """ 
        pass

    def step(self):
        pass

