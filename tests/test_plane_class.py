import unittest

from model.passenger import Passenger
from model.plane import Plane


class PlaneClassTest(unittest.TestCase):

    def setUp(self):
        self.dummy_passengers = [
            Passenger("A", "B", 100),
            Passenger("C", "D", 200),
            Passenger("E", "F", 300),
        ]

    def test_creation(self):
        p = Plane("A", 100, "B", [], 100)

        self.assertEqual("A", p.airline)
        self.assertEqual(100, p.seats)
        self.assertEqual("B", p.destination)
        self.assertEqual(100, p.identification_number)

        p1 = Plane("B", 20, "C", [], 10)

        self.assertEqual("B", p1.airline)
        self.assertEqual(20, p1.seats)
        self.assertEqual("C", p1.destination)
        self.assertEqual(10, p1.identification_number)

        p2 = Plane("B", 125, "D", [], 20)

        self.assertEqual("B", p2.airline)
        self.assertEqual(125, p2.seats)
        self.assertEqual("D", p2.destination)
        self.assertEqual(20, p2.identification_number)

        with self.assertRaises(ValueError):
            _p3 = Plane("A", 0, "B", self.dummy_passengers, 20)

    def test_updates(self):
        p = Plane("A", 4, "B", self.dummy_passengers, 100)

        with self.assertRaises(ValueError):
            p.seats = 1

        with self.assertRaises(ValueError):
            p.passengers = self.dummy_passengers + self.dummy_passengers
