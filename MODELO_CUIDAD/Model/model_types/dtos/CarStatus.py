from enum import Enum


class CarStatus(Enum):
    IN_MOVEMENT = "moving"
    STOPPED = "stopped"
    PARKED = "parked"
    WAITING_FOR_PASSENGERS = "waiting"
