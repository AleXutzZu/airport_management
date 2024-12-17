import unittest
from copy import deepcopy

from model.passenger import Passenger
from model.plane import Plane
from repository.plane_repository import PlaneRepository


class PlaneRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.repository = PlaneRepository()

        self.dummy_passengers = [
            Passenger("A", "B", "1"),
            Passenger("C", "D", "2"),
            Passenger("E", "F", "3"),
        ]

        self.dummy_planes = [
            Plane("A", 10, "d1", [self.dummy_passengers[0], self.dummy_passengers[1]], 1),
            Plane("B", 200, "d2", [self.dummy_passengers[0], self.dummy_passengers[2]], 2),
            Plane("C", 50, "d3", self.dummy_passengers, 3),
        ]

        for plane in self.dummy_planes:
            self.repository.add_plane(plane.airline, plane.seats, plane.destination, plane.passengers,
                                      plane.identification_number)

    def test_reads_and_creation(self):
        self.assertEqual(3, len(self.repository.planes))
        self.assertEqual(2, self.repository.find_plane_by_index(1).identification_number)

        with self.assertRaises(IndexError):
            self.repository.find_plane_by_index(10)

        with self.assertRaises(ValueError):
            self.repository.add_plane(self.dummy_planes[0].airline, self.dummy_planes[0].seats,
                                      self.dummy_planes[0].destination,
                                      self.dummy_planes[0].passengers, self.dummy_planes[0].identification_number)

    def test_delete(self):
        self.repository.delete_plane_by_index(0)
        self.assertEqual(2, len(self.repository.planes))

        self.assertEqual("B", self.repository.find_plane_by_index(0).airline)

        with self.assertRaises(IndexError):
            self.repository.delete_plane_by_index(3)

    def test_update(self):
        self.repository.update_plane_by_index(0, "A10", 20)

        self.assertEqual("A10", self.repository.find_plane_by_index(0).airline)
        self.assertEqual(20, self.repository.find_plane_by_index(0).seats)

        with self.assertRaises(IndexError):
            self.repository.update_plane_by_index(100, "A10", 20)

        with self.assertRaises(ValueError):
            self.repository.update_plane_by_index(1, None, None, None, None, 1)

    def test_passenger_deletion(self):
        test_passenger = self.dummy_passengers[0]
        self.repository.remove_passenger_from_planes(test_passenger)

        for plane in self.repository.planes:
            self.assertTrue(test_passenger not in plane.passengers)

    def test_passenger_update(self):
        self.dummy_passengers[0].passport_number = 100

        for plane in self.dummy_planes:
            self.assertEqual(100, plane.passengers[0].passport_number)
