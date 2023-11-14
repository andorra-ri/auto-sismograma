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
    