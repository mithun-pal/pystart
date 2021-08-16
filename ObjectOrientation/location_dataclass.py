from dataclasses import dataclass
from position import Position, EarthPosition


@dataclass(eq=True, frozen=True)  # It makes the object equality comparable, immutable, hashable
#  and so usable in set, frozen set and as key in dict.
class Location:
    # In dataclass, type annotation is mandatory so that @dataclass decorator can detect the class attribute
    # it needs to process.
    # Data classes are best used to represent immutable value objects.That means
    # use immutable attribute type, so basic types like int, float and strings are fine.
    # Declare dataclass as frozen, i.e immutable in Python language
    name: str
    position: Position


oslo = Location("Oslo", EarthPosition(59.91, 10.75))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
amsterdam = Location("Amsterdam", EarthPosition(52.36, 4.90))
capetown = Location("Cape Town", EarthPosition(33.92, 18.42))
bern = Location("Bern", EarthPosition(46.94, 7.44))

# Hashability Rules:
# 1. Immutability is difficult to express in Python
# 2. Hash-based collections require immutable elements
# 3. Equality and hashing must be consistent, i.e if two objects have the same hash code, they might be equal
# but if they're equal they must have the same hash code.


@dataclass(
    init=True,
    repr=True,
    eq=True,  # This enables dataclass decorator to implement certain magic methods passed as True.
    order=False,
    unsafe_hash=False,
    frozen=False
)
class SimpleDataClass:
    height: float
    width: float
    length: float
