from typing import Iterator, Tuple, Union

from math import acos

class Vector2:
    """
    2D float Vector with components .x and .y
    """
    
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y
    
    # Class Variables
    __name__: str = "Vector2"
    __slots__: Tuple['str'] = ('x', 'y')
    
    @classmethod
    def initialize_directions(cls):
        cls.UP :'Vector2' = Vector2(0, -1)
        cls.DOWN :'Vector2' = Vector2(0, 1)
        cls.LEFT :'Vector2' = Vector2(1, 0)
        cls.RIGHT :'Vector2' = Vector2(-1, 0)
        cls.ZERO :'Vector2' = Vector2(0, 0)
        cls.ONE :'Vector2' = Vector2(1, 1)
    
    # Comparisions
    def __eq__(self, other: 'Vector2') -> bool:
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other: 'Vector2') -> bool:
        return self.x != other.x or self.y != other.y
    
    def __lt__(self, other: 'Vector2') -> bool:
        return self.x != other.x or self.y != other.y
    
    def __le__(self, other: 'Vector2') -> bool:
        return self.x != other.x or self.y != other.y
    
    def __gt__(self, other: 'Vector2') -> bool:
        return self.x != other.x or self.y != other.y
    
    def __ge__(self, other: 'Vector2') -> bool:
        return self.x != other.x or self.y != other.y
    
    # String representation
    def __str__(self) -> str:
        return f"{self.__name__}({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    # Define
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __bool__(self) -> bool:
        return self.x != 0 and self.y != 0
    
    # Container Methods:
    def __len__(self) -> float:
        return (self.x**2 + self.x**2) ** 0.5
    
    def __iter__(self) -> Iterator[float]:
        for axis_value in (self.x, self.x):
            yield axis_value
    
    def __contains__(self, value: float) -> bool:
        for axis_value in self:
            if axis_value == value:
                return True
        return False
    
    # Numeric Operators:
    def __add__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: float) -> 'Vector2':
        return Vector2(scalar * self.x, scalar * self.y)
    
    def __truediv__(self, scalar: float) -> 'Vector2':
        return Vector2(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar: float) -> 'Vector2i':
        return Vector2(self.x // scalar, self.y // scalar)
    
    def __mod__(self, scalar: float) -> 'Vector2':
        return Vector2(self.x % scalar, self.y % scalar)
    
    def __pow__(self, scalar: int) -> 'Vector2':
        return Vector2(self.x ** scalar, self.y ** scalar)
    
    # Unary Operators:
    def __neg__(self) -> 'Vector2':
        return Vector2(-self.x, -self.y)

    def __pos__(self) -> 'Vector2':
        return Vector2(self.x, self.y)
    
    def __abs__(self) -> 'Vector2':
        return Vector2(abs(self.x), abs(self.y))
    
    # Conversion Operators:
    def __int__(self) -> int:
        return self
    
    # Vector specific methods
    def dot(self, other: 'Vector2') -> int:
        return self.x * other.x + self.y * other.y
    
    def cross(self, other: 'Vector2') -> int:
        return self.x * other.y - self.y * other.x
    
    def angle(self, other: 'Vector2') -> float:
        return acos(self.dot(other) / (len(self) * len(other)))
    
    def magnitude(self) -> float:
        return len(self)
    
    def length(self) -> float:
        return len(self)
    
    def normalize(self) -> 'Vector2':
        return self / len(self)
    
    def distance(self, other: 'Vector2') -> float:
        return len(self - other)
    
    def is_linearly_dependent(self, other: 'Vector2') -> bool:
        return abs(self.normalize().dot(other.normalize())) == 1

Vector2.initialize_directions()

class Vector2i:
    """
    2D integer Vector with components .x and .y
    """
    
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
    
    # Class Variables
    __name__: str = "Vector2i"
    __slots__: Tuple['str'] = ('x', 'y')
    
    @classmethod
    def initialize_directions(cls):
        cls.UP :'Vector2i' = Vector2i(0, -1)
        cls.DOWN :'Vector2i' = Vector2i(0, 1)
        cls.LEFT :'Vector2i' = Vector2i(1, 0)
        cls.RIGHT :'Vector2i' = Vector2i(-1, 0)
        cls.ZERO :'Vector2i' = Vector2i(0, 0)
        cls.ONE :'Vector2i' = Vector2i(1, 1)
    
    # Comparisions
    def __eq__(self, other: 'Vector2i') -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: 'Vector2i') -> bool:
        return self.x != other.x or self.y != other.y
    
    def __lt__(self, other: 'Vector2i') -> bool:
        return self.x != other.x or self.y != other.y
    
    def __le__(self, other: 'Vector2i') -> bool:
        return self.x != other.x or self.y != other.y
    
    def __gt__(self, other: 'Vector2i') -> bool:
        return self.x != other.x or self.y != other.y
    
    def __ge__(self, other: 'Vector2i') -> bool:
        return self.x != other.x or self.y != other.y
    
    # String representation
    def __str__(self) -> str:
        return f"{self.__name__}({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    # Define
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __bool__(self) -> bool:
        return self.x != 0 and self.y != 0
    
    # Container Methods:
    def __len__(self) -> float:
        return (self.x**2 + self.x**2) ** 0.5
    
    def __iter__(self) -> Iterator[int]:
        for axis_value in (self.x, self.x):
            yield axis_value
    
    def __contains__(self, value: int) -> bool:
        for axis_value in self:
            if axis_value == value:
                return True
        return False
    
    # Numeric Operators:
    def __add__(self, other: 'Vector2i') -> 'Vector2i':
        return Vector2i(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector2i') -> 'Vector2i':
        return Vector2i(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: int | float) -> Union['Vector2i', 'Vector2']:
        if isinstance(scalar, int):
            return Vector2i(self.x * scalar, self.y * scalar)
        if isinstance(scalar, float):
            return Vector2(self.x * scalar, self.y * scalar)
        raise TypeError(f"Cannot multiply {self.__name__} with {type(scalar)}")
    
    def __truediv__(self, scalar: int) -> Vector2:
        return Vector2i(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar: int) -> 'Vector2i':
        return Vector2i(self.x // scalar, self.y // scalar)
    
    def __mod__(self, scalar: int | float) -> Union['Vector2i', 'Vector2']:
        if isinstance(scalar, int):
            return Vector2i(self.x % scalar, self.y % scalar)
        if isinstance(scalar, float):
            return Vector2(self.x % scalar, self.y % scalar)
        raise TypeError(f"Cannot calculate mod of {self.__name__} with {type(scalar)}")
    
    def __pow__(self, scalar: int | float) -> Union['Vector2i', 'Vector2']:
        if isinstance(scalar, int):
            return Vector2i(self.x ** scalar, self.y ** scalar)
        if isinstance(scalar, float):
            return Vector2(self.x ** scalar, self.y ** scalar)
        raise TypeError(f"Cannot raise {self.__name__} with {type(scalar)}")
    
    # Unary Operators:
    def __neg__(self) -> 'Vector2i':
        return Vector2i(-self.x, -self.y)

    def __pos__(self) -> 'Vector2i':
        return Vector2i(self.x, self.y)
    
    def __abs__(self) -> 'Vector2i':
        return Vector2i(abs(self.x), abs(self.y))
    
    # Conversion Operators:
    def __int__(self) -> int:
        return self
    
    # Vector specific methods
    def dot(self, other: 'Vector2i') -> int:
        return self.x * other.x + self.y * other.y
    
    def cross(self, other: 'Vector2i') -> int:
        return self.x * other.y - self.y * other.x
    
    def angle(self, other: 'Vector2i') -> float:
        return acos(self.dot(other) / (len(self) * len(other)))
    
    def magnitude(self) -> float:
        return len(self)
    
    def length(self) -> float:
        return len(self)
    
    def normalize(self) -> Vector2:
        return self / len(self)
    
    def distance(self, other: 'Vector2i') -> float:
        return len(self - other)
    
    def is_linearly_dependent(self, other: 'Vector2i') -> bool:
        return abs(self.normalize().dot(self.normalize())) == 1

Vector2i.initialize_directions()


def get_signed_value_string(value: int | float, zeroSign: str = ' '):
    return f"{get_sign_string(value, zeroSign)}{value}"

def get_sign_string(value: int | float, zeroSign: str = ' '):
    if value < 0:
        return '-'
    if value > 0:
        return '+'
    return zeroSign