from pydantic.dataclasses import dataclass

from model.country import Country


@dataclass
class Edge:
    c1:int
    c2:int
