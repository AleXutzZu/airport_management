from model.plane import Plane


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

    def add_plane(self, plane):
        """
        Adds a plane to the repository
        :param plane: the plane to add
        :type plane: Plane
        """
        self.__planes.append(plane)

    def find_plane_by_index(self, index):
        """
        Returns the plane at the given index
        :param index: the index of the plane
        :type index: int
        :return: the plane at the given index
        :rtype: Plane
        """
        return self.__planes[index]

    def delete_plane_by_index(self, index):
        """
        Deletes the plane at the given index
        :param index: the index of the plane
        :type index: int
        """
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
        if identification_number is not None:
            self.__planes[index].identification_number = identification_number

        if airline is not None:
            self.__planes[index].airline = airline

        if seats is not None:
            self.__planes[index].seats = seats

        if destination is not None:
            self.__planes[index].destination = destination

        if passengers is not None:
            self.__planes[index].passengers = passengers
