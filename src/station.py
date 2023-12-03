from dataclasses import dataclass
from enum import Enum

class StationNetwork(Enum):
    FR = 'FR'
    CA = 'CA'

@dataclass
class Station:
    name: str
    network: StationNetwork
    channel: str
    amplification: int
    location: str = ''

    @classmethod
    def from_dict(cls, data: dict):
        data['network'] = StationNetwork[data['network']]
        data['amplification'] = int(data['amplification'])
        return cls(**data)
