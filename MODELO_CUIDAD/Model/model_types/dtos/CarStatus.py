from enum import Enum


class CarStatus(Enum):

    IN_MOVEMENT = "moving"
    STOPPED = "stopped"
    PARKED = "parked"
    WAITING = "waiting"
    IN_DESTINY = "in_destiny"
