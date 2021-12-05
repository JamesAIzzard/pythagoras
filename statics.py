import math
from enum import Enum
from typing import List


class Axes(Enum):
    X = 1
    Y = 2
    Z = 3


class Point:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z


class Vector3D:
    def __init__(self, x: float, y: float, z: float, tail: 'Point' = None):
        if tail is None:
            self.tail = Point()
        else:
            self.tail = tail
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: 'Vector3D') -> 'Vector3D':
        head_point = Point(*self.head_coords)
        return Vector3D(
            x=head_point.x + other.x,
            y=head_point.y + other.y,
            z=head_point.z + other.z
        )

    @property
    def length(self) -> float:
        """Returns the vector length."""
        return math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

    @property
    def head_coords(self) -> List[float, float, float]:
        """Returns a list of coordinates representing the head position."""
        return [
            self.tail.x + self.x,
            self.tail.y + self.y,
            self.tail.z + self.z
        ]


def make_vector_from_angle_on_plane(
        on_plane: 'Axes',
        angle_from: 'Axes',
        angle: float,
        length: float,
        tail: 'Point' = None
) -> 'Vector3D':
    """Creates a 3D vector on a specified plane using angle from axis."""
    raise NotImplementedError


def get_planar_angle(
        vector: 'Vector3D',
        on_plane: Axes,
        angle_from: Axes
) -> float:
    """Gets the angle of the vector's projection on the specified plane
    from the specified axis."""
    raise NotImplementedError


fa_ = Vector3D(x=80, y=0, z=0)
fb_ = make_vector_from_angle_on_plane(
    on_plane=Axes.Z,
    angle_from=Axes.X,
    angle=45,
    length=160
)
r_ = fa_ + fb_

print(f"Magnitude of R: {r_.length}(N)")
print(f"Direction of R: {r_.get_planar_angle(on_plane=Axes.Z, angle_from=Axes.X)}")
