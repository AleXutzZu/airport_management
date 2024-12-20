import unittest

from model.passenger import Passenger
from model.plane import Plane
from repository.plane_repository import PlaneRepository
from service.plane_controller import PlaneController


class PlaneControllerTest(unittest.TestCase):
    def setUp(self):
        self.controller = PlaneController(PlaneRepository())

        self.dummy_passengers = [
            Passenger("A", "B", "111"),
            Passenger("AC", "D", "1112"),
            Passenger("AE", "F", "3"),
        ]

        self.dummy_planes = [
            Plane("A", 10, "d1", [self.dummy_passengers[0]], 1),
            Plane("B", 200, "d2", [self.dummy_passengers[0], self.dummy_passengers[2]], 2),
            Plane("C", 50, "d3", self.dummy_passengers, 3),
        ]

        for plane in self.dummy_planes:
            self.controller.create_new_plane(plane.airline, plane.seats, plane.destination, plane.passengers,
                                             plane.identification_number)

    def test_reads_and_creation(self):
        self.assertEqual(3, len(self.controller.get_all_planes()))
        self.assertEqual(2, self.controller.get_plane_by_index(1).identification_number)

        with self.assertRaises(IndexError):
            self.controller.get_plane_by_index(10)

        with self.assertRaises(ValueError):
            self.controller.create_new_plane(self.dummy_planes[0].airline, self.dummy_planes[0].seats,
                                             self.dummy_planes[0].destination,
                                             self.dummy_planes[0].passengers,
                                             self.dummy_planes[0].identification_number)

    def test_delete(self):
        self.controller.delete_plane_by_index(0)
        self.assertEqual(2, len(self.controller.get_all_planes()))

        self.assertEqual("B", self.controller.get_plane_by_index(0).airline)

        with self.assertRaises(IndexError):
            self.controller.delete_plane_by_index(3)

    def test_update(self):
        self.controller.update_plane_by_index(0, "A10", 20, None, None, None)

        self.assertEqual("A10", self.controller.get_plane_by_index(0).airline)
        self.assertEqual(20, self.controller.get_plane_by_index(0).seats)

        with self.assertRaises(IndexError):
            self.controller.update_plane_by_index(100, "A10", 20, None, None, None)

        with self.assertRaises(ValueError):
            self.controller.update_plane_by_index(1, None, None, None, None, 1)

    def test_passenger_deletion(self):
        test_passenger = self.dummy_passengers[0]
        self.controller.remove_passenger_from_planes(test_passenger)

        for plane in self.controller.get_all_planes():
            self.assertTrue(test_passenger not in plane.passengers)

    def test_passenger_update(self):
        self.dummy_passengers[0].passport_number = 100

        for plane in self.dummy_planes:
            self.assertEqual(100, plane.passengers[0].passport_number)

    def test_sort_passengers_by_last_name(self):
        passengers = self.controller.get_sorted_passengers_on_plane_by_last_name(2)
        self.assertEqual(passengers, sorted(self.dummy_passengers, key=lambda passenger: passenger.last_name))

        passengers = self.controller.get_sorted_passengers_on_plane_by_last_name(0)
        self.assertEqual(passengers, sorted(self.controller.get_plane_by_index(0).passengers,
                                            key=lambda passenger: passenger.last_name))

        passengers = self.controller.get_sorted_passengers_on_plane_by_last_name(1)
        self.assertEqual(passengers, sorted(self.controller.get_plane_by_index(1).passengers,
                                            key=lambda passenger: passenger.last_name))

    def test_sort_planes_by_passenger_count(self):
        planes = self.controller.get_sorted_planes_by_passenger_count()

        self.assertEqual(planes, sorted(self.dummy_planes, key=lambda plane: len(plane.passengers)))

    def test_get_sorted_planes_by_count_of_passengers_matching_prefix(self):
        planes = self.controller.get_sorted_planes_by_count_of_passengers_matching_prefix("A")

        def comparator(plane):
            count = 0
            for passenger in plane.passengers:
                if len(passenger.first_name) < 1:
                    continue

                l = 1
                if passenger.first_name[:l] == "A":
                    count += 1
            return count

        self.assertEqual(planes, sorted(self.dummy_planes, key=lambda plane: comparator(plane)))

    def test_get_sorted_planes_by_concatenation(self):
        planes = self.controller.get_sorted_planes_by_concatenation()

        self.assertEqual(planes,
                         sorted(self.dummy_planes, key=lambda plane: str(len(plane.passengers)) + plane.destination))

    def test_get_planes_with_common_passport_prefixes(self):
        planes = self.controller.get_planes_with_common_passport_prefixes()

        self.assertEqual(planes, [self.dummy_planes[2]])

    def test_get_passengers_on_plane_containing_string(self):
        passengers = self.controller.get_passengers_on_plane_containing_string(1, "B")

        self.assertEqual(passengers, [self.dummy_passengers[0]])

    def test_get_all_planes_containing_passenger_with_name(self):
        planes = self.controller.get_all_planes_containing_passenger_with_name("AC")

        self.assertEqual(planes, [self.dummy_planes[2]])