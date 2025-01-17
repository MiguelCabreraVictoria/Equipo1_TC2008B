from model_types.dtos.Destinities import Destinities


from dataclasses import dataclass, asdict
from typing import List

@dataclass(frozen=True)
class Parameter:
    """
    Value Object de los parametros para ingresar al modelo
    """
    num_cars: int
    num_persons: int
    max_speed: int
    semaphore_timelapse: int
    safe_distance: int
    destinities: List[Destinities]
    states: List[List[int]]

    def __post_init__(self) -> None:
        if self.num_cars < 0 or self.num_persons < 0: 
            raise ValueError("At least there should be one person or car")

        if len(self.destinities) == 0:
            raise ValueError("At there should be one destinity")

    def to_json(self):
        return asdict(self)



