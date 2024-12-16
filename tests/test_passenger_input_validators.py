import unittest

from exceptions.invalid_input import InvalidInputError
from validators.input.passenger_input_validators import get_validated_index, get_validated_passenger_data


class PassengerInputValidatorsTest(unittest.TestCase):
    def test_index_validator(self):
        self.assertEqual(5, get_validated_index("5"))
        self.assertEqual(10, get_validated_index("10"))
        with self.assertRaises(InvalidInputError):
            get_validated_index("abc")

    def test_passenger_data_validator(self):
        with self.assertRaises(InvalidInputError):
            get_validated_passenger_data(None, None, "abc")

        with self.assertRaises(InvalidInputError):
            get_validated_passenger_data(None, None, "12a")

        self.assertEqual(("A", "B", 10), get_validated_passenger_data("A", "B", "10"))
