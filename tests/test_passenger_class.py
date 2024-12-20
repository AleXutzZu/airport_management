import unittest

from model.passenger import Passenger


class PassengerClassTest(unittest.TestCase):
    def test_creation(self):
        p = Passenger("A", "B", "100")

        self.assertEqual(p.passport_number, "100")
        self.assertEqual(p.first_name, "A")
        self.assertEqual(p.last_name, "B")

        p1 = Passenger("X", "Y", "10")

        self.assertEqual(p1.passport_number, "10")
        self.assertEqual(p1.first_name, "X")
        self.assertEqual(p1.last_name, "Y")

        p2 = Passenger("P", "Q", "2")

        self.assertEqual(p2.passport_number, "2")
        self.assertEqual(p2.first_name, "P")
        self.assertEqual(p2.last_name, "Q")

    def test_compare_by_last_name(self):
        p1 = Passenger("A", "B", "100")
        p2 = Passenger("X", "Y", "10")
        p3 = Passenger("A", "B", "2")

        self.assertTrue(p1.compare_by_last_name(p2))
        self.assertFalse(p1.compare_by_last_name(p1))

        self.assertFalse(p1.compare_by_last_name(p3))
        self.assertTrue(p3.compare_by_last_name(p2))

        self.assertFalse(p3.compare_by_last_name(p1))
