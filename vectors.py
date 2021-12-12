from typing import Optional
import math

import points
from axes import Axes


class Vector3D:
    def __init__(self, x: float, y: float, z: float, tail: Optional["points.Point3D"] = None):
        self.tail: "points.Point3D"
        self.head: "points.Point3D"
        if tail is None:
            self.tail = points.Point3D(0, 0, 0)
        else:
            self.tail = tail
        self.head = points.Point3D(
            x=self.tail.x + x, 
            y=self.tail.y + y, 
            z=self.tail.z + z
        )

    def __add__(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(
            tail = points.Point3D(*self.tail.coords),
            x=self.x + other.x,
            y=self.y + other.y,
            z=self.z + other.z
        )

    @property
    def x(self) -> float:
        """Returns the x component as a float."""
        return self.head.x - self.tail.x

    @property
    def y(self) -> float:
        """Returns the y component as a float."""
        return self.head.y - self.tail.y

    @property
    def z(self) -> float:
        """Returns the z component as a float."""
        return self.head.z - self.tail.z

    @property
    def length(self) -> float:
        """Returns the vector length."""
        return points.get_dist_between_points(self.head, self.tail)


def make_vector_from_angle_on_plane(
    on_plane: "Axes",
    angle_from: "Axes",
    angle: float,
    length: float,
    tail: Optional["points.Point3D"] = None,
) -> "Vector3D":
    """Creates a 3D vector on a specified plane using angle from axis.
    Defines angular polarity based on the right hand rule.
    """
    # Default the tail if not provided
    if tail is None:
        tail = points.Point3D(0, 0, 0)

    # Calculate the perpendicular components
    a = length * math.cos(angle)
    b = length * math.sin(angle)

    # Assign components
    if on_plane is Axes.X:
        if angle_from is Axes.Y:
            raise NotImplementedError
        else:
            raise NotImplementedError
        x, y, z = [0, a, b]
    elif on_plane is Axes.Y:
        if angle_from is Axes.X:
            raise NotImplementedError
        else:
            raise NotImplementedError
        x, y, z = [a, 0, b]
    else: # on Z plane
        if angle_from is Axes.X:
            x, y, z = [a, b, 0]
        else:
            x, y, z = [-b, a, 0]

    # Build vector
    return Vector3D(
        x=x,
        y=y,
        z=z,
        tail=tail
    )


def get_planar_angle(vector: "Vector3D", on_plane: "Axes", angle_from: "Axes") -> float:
    """Gets the angle of the vector's projection on the specified plane
    from the specified axis."""
    raise NotImplementedError
