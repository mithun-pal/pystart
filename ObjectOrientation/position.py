class Position:

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError(f"Latitude {latitude} out of range")
        if not (-180 <= longitude <= +180):
            raise ValueError(f"Longitude {longitude} out of range")

        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude >= 0 else "S"

    @property
    def longitude_hemisphere(self):
        return "E" if self.longitude >= 0 else "W"

    # This magic method is intended for developers
    def __repr__(self):
        return f"{typename(self)}(latitude={self.latitude}, longitude={self.longitude})"

    # This magic method is intended for external consumers
    def __str__(self):
        return format(self)

    # This magic method is needed to represent the object in f string or format method
    # everest = EarthPosition(27.9881, 86.9253)
    # f"The position of Mount Everest on Earth is {everest:.2}" -- format specifier as 2 decimal place
    # f"The position of Mount Everest on Earth is {everest!r}" -- This enforces to use the repr implementation
    # f{everest=} -- Display variable name and its repr value in an f string placeholder
    def __format__(self, format_spec):
        format_spec_comp = ".2f"
        prefix, dot, suffix = format_spec.partition(".")
        if dot:
            format_spec_comp = f".{int(suffix)}f"
        latitude = format(abs(self.latitude), format_spec_comp)
        longitude = format(abs(self.longitude), format_spec_comp)
        return (f"{latitude}° {self.latitude_hemisphere}, "
                f"{longitude}° {self.longitude_hemisphere}"
                )


def typename(obj):
    return type(obj).__name__


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass

