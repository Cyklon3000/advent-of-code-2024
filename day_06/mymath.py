import math
import typing
import random
from typing import Type, Union, overload

class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    @overload
    def __add__(self, other: 'Vector2D') -> 'Vector2D': ...
    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    @overload
    def __sub__(self, other: 'Vector2D') -> 'Vector2D': ...
    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)

    @overload
    def __mul__(self, other: Union[int, float]) -> 'Vector2D': ...
    @overload
    def __mul__(self, other: 'Vector2D') -> 'Vector2D': ...
    def __mul__(self, other: Union[int, float, 'Vector2D']) -> 'Vector2D':
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        return Vector2D(self.x * other.x, self.y * other.y)

    @overload
    def __truediv__(self, other: Union[int, float]) -> 'Vector2D': ...
    @overload
    def __truediv__(self, other: 'Vector2D') -> 'Vector2D': ...
    def __truediv__(self, other: Union[int, float, 'Vector2D']) -> 'Vector2D':
        if isinstance(other, (int, float)):
            return Vector2D(self.x / other, self.y / other)
        return Vector2D(self.x / other.x, self.y / other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __abs__(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def __len__(self) -> int:
        return 2

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def copy(self) -> 'Vector2D':
        return Vector2D(self.x, self.y)

    def clone(self) -> 'Vector2D':
        return self.copy()

    def magnitude(self) -> float:
        return abs(self)

    def normalize(self) -> 'Vector2D':
        return self / abs(self)

    def dot(self, other: 'Vector2D') -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other: 'Vector2D') -> float:
        return self.x * other.y - self.y * other.x

    def angle(self, other: 'Vector2D') -> float:
        return math.acos(self.dot(other) / (abs(self) * abs(other)))

    def rotate(self, angle: float) -> 'Vector2D':
        return Vector2D(
            self.x * math.cos(angle) - self.y * math.sin(angle),
            self.x * math.sin(angle) + self.y * math.cos(angle),
        )

    def distance(self, other: 'Vector2D') -> float:
        return abs(self - other)

    @classmethod
    def UP(cls) -> 'Vector2D':
        return cls(0, 1)

    @classmethod
    def DOWN(cls) -> 'Vector2D':
        return cls(0, -1)

    @classmethod
    def LEFT(cls) -> 'Vector2D':
        return cls(-1, 0)

    @classmethod
    def RIGHT(cls) -> 'Vector2D':
        return cls(1, 0)

    @classmethod
    def ZERO(cls) -> 'Vector2D':
        return cls(0, 0)

    @classmethod
    def random(cls, xMin: float = 0, yMin: float = 0, xMax: float = 1, yMax: float = 1) -> 'Vector2D':
        return cls(random.uniform(xMin, xMax), random.uniform(yMin, yMax))
    
    @classmethod
    def randomInt(cls, xMin: int, yMin: int, xMax: int, yMax: int) -> 'Vector2D':
        return cls(random.randint(xMin, xMax), random.randint(yMin, yMax))