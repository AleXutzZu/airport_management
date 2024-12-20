import unittest

from model.passenger import Passenger
from repository.passenger_repository import PassengerRepository
from service.passenger_controller import PassengerController


class PassengerControllerTest(unittest.TestCase):

    def setUp(self):
        self.controller = PassengerController(PassengerRepository())
        self.dummy_passengers = [
            Passenger("A", "B", "100"),
            Passenger("C", "D", "200"),
            Passenger("E", "F", "300"),
        ]

        for passenger in self.dummy_passengers:
            self.controller.create_new_passenger(passenger.first_name, passenger.last_name, passenger.passport_number)

    def test_reads_and_creation(self):
        self.assertEqual(3, len(self.controller.get_all_passengers()))

        self.assertEqual("200", self.controller.get_passenger_by_index(1).passport_number)

        with self.assertRaises(IndexError):
            self.controller.get_passenger_by_index(10)

        with self.assertRaises(ValueError):
            self.controller.create_new_passenger(self.dummy_passengers[0].first_name,
                                                 self.dummy_passengers[0].last_name,
                                                 self.dummy_passengers[0].passport_number)

    def test_delete(self):
        self.controller.delete_passenger_by_index(0)
        self.assertEqual(2, len(self.controller.get_all_passengers()))

        with self.assertRaises(IndexError):
            self.controller.delete_passenger_by_index(10)

        self.assertNotEqual(self.controller.get_passenger_by_index(0).passport_number,
                            self.dummy_passengers[0].passport_number)

    def test_update(self):
        self.controller.update_passenger_by_index(0, None, "X", None)

        self.assertEqual("X", self.controller.get_passenger_by_index(0).last_name)

        with self.assertRaises(IndexError):
            self.controller.update_passenger_by_index(-10, None, None, None)

        with self.assertRaises(ValueError):
            self.controller.update_passenger_by_index(0, None, None, self.dummy_passengers[0].passport_number)
