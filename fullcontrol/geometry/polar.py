
from fullcontrol.geometry import Point, Vector
from math import atan2, cos, sin, tau

from pydantic import BaseModel


class PolarPoint(BaseModel):
    radius: float
    angle: float


def polar_to_point(centre: Point, radius: float, angle: float) -> Point:
    'find x y coordinates of a Point based on angle (radians), radius and centre Point. return new Point with z = centre.z'
    return Point(x=centre.x + radius*cos(angle), y=centre.y + radius*sin(angle), z=centre.z)


def point_to_polar(point: Point, centre: Point) -> PolarPoint:
    'find polar radius and angle (radians: 0 to 2pi) in XY plane of the given Point relative to the centre Point. return a PolarPoint, accessed with .radius and .angle)'
    r = ((point.x - centre.x) ** 2 + (point.y - centre.y) ** 2) ** 0.5
    angle = atan2((point.y - centre.y), (point.x - centre.x))
    return PolarPoint(radius=r, angle=angle % tau)


def polar_to_vector(length: float, angle: float) -> Vector:
    'return an xy Vector based on an angle (radians) and length defined in polar coordinates. return a Vector with xy components'
    pt = polar_to_point(Point(x=0, y=0), length, angle)
    return Vector(x=pt.x, y=pt.y)
