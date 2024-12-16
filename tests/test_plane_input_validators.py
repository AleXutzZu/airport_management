import unittest

from exceptions.invalid_input import InvalidInputError
from validators.input.plane_input_validators import get_validated_index, get_validated_plane_data


class PlaneInputValidatorsTest(unittest.TestCase):
    def test_index_validator(self):
        self.assertEqual(5, get_validated_index("5"))
        self.assertEqual(10, get_validated_index("10"))
        with self.assertRaises(InvalidInputError):
            get_validated_index("abc")

    def test_plane_data_validator(self):
        with self.assertRaises(InvalidInputError):
            get_validated_plane_data(None, "abc", None, None, None)

        with self.assertRaises(InvalidInputError):
            get_validated_plane_data(None, "100", None, "a b c", None)

        with self.assertRaises(InvalidInputError):
            get_validated_plane_data(None, "100", None, "1 2 3", "abc")

        self.assertIsNotNone(get_validated_plane_data("a", "100", "b", "1", "20"))
