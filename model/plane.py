from model.passenger import Passenger


class Plane:
    """Class representing a plane for an airline with a set destination, total seats, passengers, airline company
    and identification number
    """

    def __init__(self, airline, seats, destination, passengers, identification_number):
        """Constructor for the Plane class
        :param airline: the airline company owning the plane
        :type airline: str
        :param seats: the number of seats available in the plane
        :type seats: int
        :param destination: the destination of the plane
        :type destination: str
        :param passengers: the passengers of the plane
        :type passengers: list of Passenger
        :param identification_number: the identification number of the plane
        :type identification_number: int
        """
        self.__airline = airline
        self.__seats = seats
        self.__destination = destination
        self.__passengers = passengers
        self.__identification_number = identification_number

        if seats < len(passengers):
            raise ValueError('Seats cannot be less than the number of passengers')

    def __repr__(self):
        return f"Plane(owned by {self.__airline}, id: {self.__identification_number}) - {self.__seats} seats, destination: {self.__destination}\n Passengers: {self.__passengers}"

    @property
    def airline(self):
        """
        Returns the airline company owning the plane
        :return: the airline company
        :rtype: str
        """
        return self.__airline

    @airline.setter
    def airline(self, value):
        """
        Updates the airline company that owns this plane
        :param value: the new airline company
        :type value: str
        """
        self.__airline = value

    @property
    def seats(self):
        """
        Returns the number of seats available in the plane
        :return: the seat number
        :rtype: int
        """
        return self.__seats

    @seats.setter
    def seats(self, value):
        """
        Updates the number of seats
        :param value: the new number of seats
        :type value: int
        """
        if value < len(self.__passengers):
            raise ValueError("Cannot have less seats than passengers")

        self.__seats = value

    @property
    def destination(self):
        """
        Returns the destination of the plane
        :return: the destination of the plane
        :rtype: str
        """
        return self.__destination

    @destination.setter
    def destination(self, value):
        """
        Updates the destination of the plane
        :param value: the new destination of the plane
        :type value: str
        """
        self.__destination = value

    @property
    def passengers(self):
        """
        Returns the passengers of the plane
        :return: the passengers of the plane
        :rtype: list of Passenger
        """
        return self.__passengers

    @passengers.setter
    def passengers(self, value):
        """
        Updates the passengers of the plane
        :param value: the new passengers of the plane
        :type value: list of Passenger
        """
        if len(value) > self.__seats:
            raise ValueError("Passengers cannot be greater than seats")
        self.__passengers = value

    @property
    def identification_number(self):
        """
        Returns the identification number of the plane
        :return: the identification number of the plane
        :rtype: int
        """
        return self.__identification_number

    @identification_number.setter
    def identification_number(self, value):
        """
        Updates the identification number of the plane
        :param value: the new identification number of the plane
        :type value: int
        """
        self.__identification_number = value
