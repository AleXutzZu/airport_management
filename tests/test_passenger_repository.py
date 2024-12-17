import unittest

from model.passenger import Passenger
from repository.passenger_repository import PassengerRepository


class PassengerRepositoryTest(unittest.TestCase):

    def setUp(self):
        self.repository = PassengerRepository()
        self.dummy_passengers = [
            Passenger("A", "B", "100"),
            Passenger("C", "D", "200"),
            Passenger("E", "F", "300"),
        ]

        for passenger in self.dummy_passengers:
            self.repository.add_passenger(passenger.first_name, passenger.last_name, passenger.passport_number)

    def test_reads_and_creation(self):
        self.assertEqual(3, len(self.repository.passengers))

        self.assertEqual("200", self.repository.find_passenger_by_index(1).passport_number)

        with self.assertRaises(IndexError):
            self.repository.find_passenger_by_index(10)

        with self.assertRaises(ValueError):
            self.repository.add_passenger(self.dummy_passengers[0].first_name, self.dummy_passengers[1].last_name,
                                          self.dummy_passengers[2].passport_number)

    def test_delete(self):
        self.repository.delete_passenger_by_index(0)
        self.assertEqual(2, len(self.repository.passengers))

        with self.assertRaises(IndexError):
            self.repository.delete_passenger_by_index(10)

        self.assertNotEqual(self.repository.find_passenger_by_index(0).passport_number,
                            self.dummy_passengers[0].passport_number)

    def test_update(self):
        self.repository.update_passenger_by_index(0, last_name="X")

        self.assertEqual("X", self.repository.find_passenger_by_index(0).last_name)

        with self.assertRaises(IndexError):
            self.repository.update_passenger_by_index(-10)

        with self.assertRaises(ValueError):
            self.repository.update_passenger_by_index(0, None, None, self.dummy_passengers[0].passport_number)
