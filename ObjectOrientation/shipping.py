import iso6346

class ShippingContainer:
    next_serial_num = 1447

    def __init__(self, owner_code, contents, **kwargs):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial_num()
            )

    @classmethod
    def _generate_serial_num(cls):
        s_num = cls.next_serial_num
        cls.next_serial_num += 1
        return s_num

    @staticmethod
    def _make_bic_code(self, owner_code, serial):
        return iso6346.create(owner_code=owner_code,
                              serial=str(serial).zfill(6))

    @classmethod
    def create_empty(cls, owner_code, **kwargs):
        return cls(owner_code, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, **kwargs):
        return cls(owner_code, contents=list(items), **kwargs)


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0

    # Making celsius as keyword only argument by putting * before it
    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        super().__init__(owner_code, contents, **kwargs)
        if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature is too hot")
        self.celsius = celsius

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, tem):
        if tem > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot")
        self._celsius=tem

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R'
        )