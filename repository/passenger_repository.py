from model.passenger import Passenger


class PassengerRepository:
    """
    Manages all the passengers of the application.
    """

    def __init__(self):
        self.__passengers = []

    def add_passenger(self, passenger):
        """
        Adds a new passenger
        :param passenger: the passenger to add
        :type passenger: Passenger
        """
        self.__passengers.append(passenger)

    @property
    def passengers(self):
        """Gets all passengers in the repository
        :return: a list of all the passengers
        :rtype: list of Passenger
        """
        return self.__passengers

    def find_passenger_by_index(self, index):
        """
        Returns the passenger at the given index
        :param index: the index of the passenger
        :type index: int
        :return: the passenger at the given index
        :rtype: Passenger
        """
        return self.__passengers[index]

    def delete_passenger_by_index(self, index):
        """
        Deletes the passenger at the given index
        :param index: the index of the passenger
        :type index: int
        """
        del self.__passengers[index]

    def update_passenger_by_index(self, index, first_name=None, last_name=None, passport_number=None):
        """
        Updates the passenger at the given index
        :param index: the index of the passenger
        :type index: int
        :param last_name: the new last name, can be None to be left unchanged
        :type last_name: str or None
        :param first_name: the new first name, can be None to be left unchanged
        :type first_name: str or None
        :param passport_number: the new passport number, can be None to be left unchanged
        :type passport_number: str or None
        """

        if passport_number is not None:
            self.__passengers[index].passport_number = passport_number

        if last_name is not None:
            self.__passengers[index].last_name = last_name

        if first_name is not None:
            self.__passengers[index].first_name = first_name
