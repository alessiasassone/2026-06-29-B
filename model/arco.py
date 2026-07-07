from dataclasses import dataclass

from model.album import Album


@dataclass
class Arco:
    n1: Album
    n2: Album