import functools

from location import *

oslo = Location("Oslo", EarthPosition(59.91, 10.75))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
amsterdam = Location("Amsterdam", EarthPosition(52.36, 4.90))
capetown = Location("Cape Town", EarthPosition(33.92, 18.42))
bern = Location("Bern", EarthPosition(46.94, 7.44))


def post_condition(predicate):
    def function_decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            if not predicate(self):
                raise RuntimeError(
                    f"Post-condition {predicate.__name__} not "
                    f"maintained for {self!r}"
                )
            return result
        return wrapper
    return function_decorator


def invariant(predicate):
    func_decorator = post_condition(predicate)

    def class_decorator(cls):
        members = list(vars(cls).items())
        for name, member in members:
            if inspect.isfunction(member):
                decorated_member = func_decorator(member)
                setattr(cls, name, decorated_member)
        return cls
    return class_decorator


def at_least_two_loc(itinerary):
    return len(itinerary._locations) >= 2


def no_duplicates(itinerary):
    already_seen = set()
    for location in itinerary._locations:
        if location in already_seen:
            return False
        already_seen.add(location)
    return True


@auto_repr
@invariant(no_duplicates)
@invariant(at_least_two_loc)
class Itinerary:

    def __init__(self, locations):
        self._locations = list(locations)

    def __str__(self):
        return "\n".join(location.name for location in self._locations)

    @classmethod
    def from_locations(cls, *locations):
        return cls(locations)

    @property
    def locations(self):
        return tuple(self._locations)

    @property
    def origin(self):
        return self._locations[0]

    @property
    def destination(self):
        return self._locations[-1]

    def add(self, location):
        self._locations.append(location)

    def remove(self, loc):
        removal_indexes = [
            index for index, location in enumerate(self._locations)
            if location.name == loc
        ]
        for index in reversed(removal_indexes):
            del self._locations[index]

    def truncate_at(self, name):
        stop = None
        for index, location in enumerate(self._locations):
            if location.name == name:
                stop = index + 1

        self._locations = self._locations[:stop]
