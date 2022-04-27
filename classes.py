from numpy import array, float64
from typing import Union


class Vector:
    def __init__(self, *args):
        if all(type(item) in [int, float, float64] for item in args):
            # items are numbers
            self.values = array(args, dtype=float)
        elif all(type(item) == tuple for item in args) and len(args) == 2:
            # item are tuples
            if len(args[0]) == len(args[1]):
                # dimensions match
                self.values = array([args[1][dimension_index] - args[0][dimension_index] for dimension_index in range(len(args[1]))], dtype=float)
            else:
                raise AttributeError("Dimensions of attributes do not match")
        else:
            raise AttributeError("Invalid attributes")

    def __repr__(self) -> str:
        return f"Vector({', '.join(str(item) for item in self.values)})"

    def __str__(self) -> str:
        return f"({', '.join(str(item) for item in self.values)})"

    def __sub__(self, other: object) -> object:
        assert type(other) == Vector
        assert other.dims == self.dims
        new_values = self.values - other.values
        return Vector(*new_values)

    def __add__(self, other: object) -> object:
        assert type(other) == Vector
        assert other.dims == self.dims
        new_values = self.values + other.values
        return Vector(*new_values)

    def __mult__(self, other: Union[int, float]) -> object:
        new_values = self.values * other
        return Vector(*new_values)

    def __truediv__(self, other: Union[int, float]) -> object:
        new_values = self.values / other
        return Vector(*new_values)

    def __eq__(self, other: object) -> bool:
        assert type(other) == Vector
        return self.x == other.x and self.y == other.y

    def __gt__(self, other: object) -> bool:
        assert type(other) == Vector
        return self.length > other.length

    def __lt__(self, other: object) -> bool:
        assert type(other) == Vector
        return self.length < other.length

    @property
    def dims(self) -> int:
        return len(self.values)

    @property
    def length(self) -> float:
        squared_values = self.values ** 2
        summed_values = squared_values.sum()
        return summed_values ** 0.5

    def normalize(self) -> object:
        return self / self.length


class Plane:
    '''
    ways to instantiate a plane:
    1.
        Plane(Vector1, Vector2, Vector3, <boundaries>)
        Where Vector1 is a point in the plane, and Vector 2 and 3 span across the plane (cant be parallel!)
        amount of vectors must be dimensionality of plane
        vectors must be same dimensionality
    2.
        Plane(Point 1-3)
        3 Points with the same dimensionality as the plane and each other
    3.
        Plane(normal, <boundaries>)
        The normal vector perpendicular to the plane

    Attributes: origin, spanning vectors, boundaries
    '''

    def __init__(self, *args, boundaries=None):
        if all(type(item) == Vector for item in args):
            if len(args) == 1:
                pass  # normal vector init
            elif len(args) >= 3:
                pass  # spanning vector init
            else:
                raise AttributeError("A plane cannot be defined by 2 vectors")
        elif all(type(item) == tuple for item in args):
            pass  # point init (maybe call spanning vector init?) (with specified boundaries)

    def _spanning_init(self, origin, spanning_vectors):  # maybe only args
        pass

    @property
    def dims(self):
        return self.origin.dims


class Line:
    pass


def intersection(a, b):
    """Calculate the intersection of lines and planes, by calling the internal functions.

    Parameters
    ----------
    a : Line or Plane
    b : Line or Plane
    """
    pass
