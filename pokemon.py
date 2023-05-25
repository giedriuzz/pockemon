from typing import List
from dataclasses import dataclass


@dataclass
class Statistic:
    base_stat: str
    name: str


@dataclass
class Pokemon:
    name: str
    stats: List[Statistic]

    def get_statistic_base_stat(self, stat_name: str):
        for stat in self.stats:
            if stat.name == stat_name:
                return stat.base_stat
        return 0
