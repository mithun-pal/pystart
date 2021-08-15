import iso6346

class ShippingContainer:
    next_serial_num = 1447

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
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial_num()
            )

class RefrigeratedShippingContainer(ShippingContainer):

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R'
        )