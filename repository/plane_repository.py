from model.plane import Plane
from validators.repository.plane_repository_validators import is_identification_number_valid, is_plane_index_valid


class PlaneRepository:
    """
    Manages all the planes of the application
    """

    def __init__(self):
        self.__planes = []

    @property
    def planes(self):
        """
        Returns all planes
        :return: the planes in the repository
        :rtype: list of Plane
        """
        return self.__planes

    def add_plane(self, airline, seats, destination, passengers, identification_number):
        """
        Adds a plane to the repository
        :param airline: the airline
        :type airline: str
        :param seats: the seats
        :type seats: int
        :param destination: the destination
        :type destination: str
        :param passengers: the passengers
        :type passengers: list of Passenger
        :param identification_number: the identification number
        :type identification_number: int
        """
        if not is_identification_number_valid(self, identification_number):
            raise ValueError("Data is invalid")

        plane = Plane(airline, seats, destination, passengers, identification_number)

        self.__planes.append(plane)

    def find_plane_by_index(self, index):
        """
        Returns the plane at the given index
        :param index: the index of the plane
        :type index: int
        :return: the plane at the given index
        :rtype: Plane
        """
        if not is_plane_index_valid(self, index):
            raise IndexError("Plane index is invalid")

        return self.__planes[index]

    def delete_plane_by_index(self, index):
        """
        Deletes the plane at the given index
        :param index: the index of the plane
        :type index: int
        """
        if not is_plane_index_valid(self, index):
            raise IndexError("Plane index is invalid")

        del self.__planes[index]

    def update_plane_by_index(self, index, airline=None, seats=None, destination=None, passengers=None,
                              identification_number=None):
        """
        Updates the plane at the given index
        :param index: the index of the plane
        :type index: int
        :param airline: the new airline company owning the plane, can be None to leave unchanged
        :type airline: str or None
        :param seats: the new number of seats
        :type seats: int or None
        :param destination: the new destination, can be None to leave unchanged
        :type destination: str or None
        :param passengers: the new passengers, can be None to leave unchanged
        :type passengers: list of Passenger or None
        :param identification_number: the new identification number, can be None to leave unchanged
        :type identification_number: int or None
        """
        if not is_plane_index_valid(self, index):
            raise IndexError("Plane index is invalid")

        if identification_number is not None:
            if not is_identification_number_valid(self, identification_number):
                raise ValueError("Invalid data")
            self.__planes[index].identification_number = identification_number

        if airline is not None:
            self.__planes[index].airline = airline

        if seats is not None:
            self.__planes[index].seats = seats

        if destination is not None:
            self.__planes[index].destination = destination

        if passengers is not None:
            self.__planes[index].passengers = passengers

    def remove_passenger_from_planes(self, passenger):
        """
        Removes the passenger from all planes which contain them
        :param passenger: the passenger to remove
        :type passenger: Passenger
        """

        for plane in self.__planes:
            if passenger in plane.passengers:
                plane.passengers.remove(passenger)
