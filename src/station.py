from dataclasses import dataclass
from enum import Enum

class StationNetwork(Enum):
    FR = 'FR'
    CA = 'CA'

@dataclass
class Station:
    name: str
    client: str
    network: StationNetwork
    channel: str
    amplification: int
    text_station: str
    location: str = ''

    @classmethod
    def from_dict(cls, data: dict):
        data['network'] = StationNetwork[data['network']]
        return cls(**data)
