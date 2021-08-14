class ShippingContainer:
    next_serial_num = 1447

    @staticmethod
    def _generate_serial_num():
        s_num = ShippingContainer.next_serial_num
        ShippingContainer.next_serial_num += 1
        return s_num

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial_num = ShippingContainer._generate_serial_num()
