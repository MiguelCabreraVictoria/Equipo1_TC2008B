from model_types.dtos.Destinities import Destinities
from model_types.dtos.SemaphoreLight import SemaphoreLight

from dataclasses import dataclass, asdict
from typing import List, Tuple, Dict


# TODO: # TODO add directions to lanes (N, S, E, W)
@dataclass(frozen=True)
class Parameter:
    """
    Value Object de los parametros para ingresar al modelo
    """

    # Parametros Modelo
    environment_size: Tuple[int, int]
    num_cars: int
    communication_range: int
    num_persons: int
    safe_distance: int
    max_speed: int
    semaphore_timelapse: int

    # Parametros Entorno
    sidewalks: List[Tuple[int, int]]
    lanes: List[Tuple[int, int]]
    intersections: List[Tuple[int, int]]
    buildings: List[Tuple[int, int]]
    destinities: Dict[Destinities, Tuple[int, int]]
    semaphores: Dict[Tuple[int, int], SemaphoreLight]

    # Parametros Agentes
    cars_initial_speed: int
    cars_initial_fuel : int
    cars_destinities: List[Destinities]
    persons_destinities: List[Destinities]


    def __post_init__(self) -> None:

        if self.num_cars < 1 or self.num_persons < 1: 
            raise ValueError("At least there should be one person or car")
        
        if len(self.destinities) == 0:
            raise ValueError("There should be at least one destinities.")

        if len(self.destinities) == 0:
            raise ValueError("At there should be one destinity")
        
        if len(self.cars_destinities) != self.num_cars:
            raise ValueError("The number of destinities for cars should be the same as num_cars.")
        
        if len(self.persons_destinities) != self.num_persons:
            raise ValueError("The number of destinities for persons should be the same as num_persons.")
        
    def to_json(self):
        return asdict(self)



