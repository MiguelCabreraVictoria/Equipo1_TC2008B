from enum import Enum

class PersonStatus(Enum):
    
    IN_MOVEMENT = "moving"
    STOPPED = "stopped"
    WAITING = "waiting"
    IN_DESTINY = "in_destiny"
