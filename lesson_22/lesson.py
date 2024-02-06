from typing import Any


class Convertor:

    def __init__(self, value: Any):
        self.value = value

    def get_unit_from_name(self):
        pass

    def get_unit_to_name(self):
        pass

    def convert(self):
        pass


class CelsiusToKelvin(Convertor):

    @classmethod
    def get_unit_from_name(cls):
        pass

    @classmethod
    def get_unit_to_name(cls):
        pass

    @classmethod
    def convert(self):
        pass
