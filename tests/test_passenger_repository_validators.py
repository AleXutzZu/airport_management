import unittest

from model.passenger import Passenger
from repository.passenger_repository import PassengerRepository
from validators.repository.passenger_repository_validators import is_passenger_index_valid, is_passport_number_valid, \
    is_passenger_data_valid


class PassengerRepositoryValidatorsTest(unittest.TestCase):

    def setUp(self):
        self.repository = PassengerRepository()
        self.dummy_passengers = [
            Passenger("A", "B", "100"),
            Passenger("C", "D", "200"),
            Passenger("E", "F", "300"),
        ]

        for passenger in self.dummy_passengers:
            self.repository.add_passenger(passenger.first_name, passenger.last_name, passenger.passport_number)

    def test_valid_index(self):
        self.assertTrue(is_passenger_index_valid(self.repository, 0))
        self.assertTrue(is_passenger_index_valid(self.repository, 1))
        self.assertFalse(is_passenger_index_valid(self.repository, 10))

    def test_valid_passport_number(self):
        self.assertTrue(is_passport_number_valid(self.repository, "0"))
        self.assertTrue(is_passport_number_valid(self.repository, "20"))
        self.assertFalse(is_passport_number_valid(self.repository, "100"))

    def test_valid_update_data(self):
        self.assertTrue(is_passenger_data_valid(self.repository, None, None, "0"))
        self.assertTrue(is_passenger_data_valid(self.repository, "A", "B", "0"))
        self.assertTrue(is_passenger_data_valid(self.repository, None, None, "20"))
        self.assertFalse(is_passenger_data_valid(self.repository, None, None, "100"))
        self.assertFalse(is_passenger_data_valid(self.repository, "", None, None))
        self.assertFalse(is_passenger_data_valid(self.repository, "A", "", None))
        self.assertFalse(is_passenger_data_valid(self.repository, "A", "B", "200"))
