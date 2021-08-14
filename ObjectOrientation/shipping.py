class ShippingContainer:
    next_serial_num = 1447

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial_num = ShippingContainer.next_serial_num
        ShippingContainer.next_serial_num += 1