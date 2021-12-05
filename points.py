import math
from typing import Tuple

class Point3D:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    @property
    def coords(self) -> Tuple[float, float, float]:
        """Returns the point's coordinates as a tuple in the form (x, y, z)."""
        return (self.x, self.y, self.z)


def get_dist_between_points(p1: 'Point3D', p2: 'Point3D') -> float:
    """Returns the distance between the two points as a float."""
    return math.sqrt((abs(p2.x - p1.x)**2) + (abs(p2.y - p1.y)**2) + (abs(p2.z - p1.z)**2))