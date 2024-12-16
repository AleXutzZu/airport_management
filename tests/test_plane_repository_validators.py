import unittest

from model.passenger import Passenger
from model.plane import Plane
from repository.plane_repository import PlaneRepository
from validators.repository.plane_repository_validators import is_plane_index_valid, is_identification_number_valid, \
    is_plane_data_valid


class PlaneRepositoryValidatorsTest(unittest.TestCase):

    def setUp(self):
        self.repository = PlaneRepository()

        self.dummy_passengers = [
            Passenger("A", "B", 100),
            Passenger("C", "D", 200),
            Passenger("E", "F", 300),
        ]

        self.dummy_planes = [
            Plane("A", 100, "d1", [self.dummy_passengers[0], self.dummy_passengers[1]], 1),
            Plane("B", 200, "d2", [self.dummy_passengers[0], self.dummy_passengers[2]], 2),
            Plane("C", 50, "d3", self.dummy_passengers, 3),
        ]

        for plane in self.dummy_planes:
            self.repository.add_plane(plane.airline, plane.seats, plane.destination, plane.passengers,
                                      plane.identification_number)

    def test_valid_index(self):
        self.assertTrue(is_plane_index_valid(self.repository, 0))
        self.assertTrue(is_plane_index_valid(self.repository, 1))
        self.assertFalse(is_plane_index_valid(self.repository, 10))

    def test_valid_identification_number(self):
        self.assertTrue(is_identification_number_valid(self.repository, 100))
        self.assertTrue(is_identification_number_valid(self.repository, 200))
        self.assertFalse(is_identification_number_valid(self.repository, 1))

    def test_valid_update_data(self):
        self.assertTrue(is_plane_data_valid(self.repository, "X", 10, None, None, 23))
        self.assertTrue(is_plane_data_valid(self.repository, "Y", 20, None, None, 12))
        self.assertFalse(is_plane_data_valid(self.repository, "X", 10, None, None, 2))
        self.assertFalse(is_plane_data_valid(self.repository, "", 10, None, None, None))
        self.assertFalse(is_plane_data_valid(self.repository, "ZYX", -23, None, None, None))
        self.assertFalse(is_plane_data_valid(self.repository, "ZYX", 14, "", None, None))
        self.assertFalse(is_plane_data_valid(self.repository, "ZYX", 14, "ABC", [], None))
