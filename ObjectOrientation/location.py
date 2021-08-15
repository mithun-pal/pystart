import inspect
from position import *


def auto_repr(cls):
    # print(f"Decorating {cls.__name__} with auto_repr")
    members = vars(cls)
    # for name, member in members.items():
    #    print(name, member)

    if '__repr__' in members:
        raise TypeError(f"{cls.__name__} already defines __repr__")
    if '__init__' not in members:
        # Here members does not contain inherited methods
        raise TypeError(f"{cls.__name__} does not override __init__")

    sig = inspect.signature(cls.__init__)  # This returns signature object containing parameter name
    params = list(sig.parameters)[1:]  # Taking all parameters except the first one which is self
    # print("__init__ parameter names: ", params)

    if not all(
        isinstance(members.get(param, None), property)
        for param in params
    ):
        raise TypeError(
            f"Cannot apply auto_repr to {cls.__name__} because not all "
            "__init__ parameters have matching property"
        )

    def synthesized_repr(self):
        return "{typename}({args})".format(
            typename=typename(self),
            args=", ".join(
                "{name}={value!r}".format(
                    name=name,
                    value=getattr(self, name)
                ) for name in params
            )
        )
    setattr(cls, "__repr__", synthesized_repr)
    return cls

@auto_repr
class Location:

    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    #  def __repr__(self):
    #   return f"{typename(self)}(name={self.name}, position={self.position})"

    def __str__(self):
        return self.name


oslo = Location("Oslo", EarthPosition(59.91, 10.75))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
amsterdam = Location("Amsterdam", EarthPosition(52.36, 4.90))
capetown = Location("Cape Town", EarthPosition(33.92, 18.42))
bern = Location("Bern", EarthPosition(46.94, 7.44))
