from model.passenger import Passenger
from repository.passenger_repository import PassengerRepository
from validators.repository.passenger_repository_validators import is_passport_number_valid, is_passenger_index_valid


class PassengerController:
    """
    Controller responsible for operations on passengers
    """

    def __init__(self, repository):
        """
        Creates a passenger controller
        :param repository: the passenger repository
        :type repository: PassengerRepository
        """
        self.__passenger_repository = repository

    def create_new_passenger(self, first_name, last_name, passport_number):
        """Adds a passenger to the repository
        :param first_name: First name of the passenger
        :type first_name: str
        :param last_name: Last name of the passenger
        :type last_name: str
        :param passport_number: Passport number of the passenger
        :type passport_number: str
        """

        if not is_passport_number_valid(self.__passenger_repository, passport_number):
            raise ValueError("Data is invalid")

        passenger = Passenger(first_name, last_name, passport_number)
        self.__passenger_repository.add_passenger(passenger)

    def get_passenger_by_index(self, index):
        """
        Returns the passenger at the given index
        :param index: the index of the passenger
        :type index: int
        :return: the passenger at the given index
        :rtype: Passenger
        """
        if not is_passenger_index_valid(self.__passenger_repository, index):
            raise IndexError("Invalid index")
        return self.__passenger_repository.find_passenger_by_index(index)

    def delete_passenger_by_index(self, index):
        """
        Deletes the passenger at the given index
        :param index: the index of the passenger
        :type index: int
        """
        if not is_passenger_index_valid(self.__passenger_repository, index):
            raise IndexError("Invalid index")
        self.__passenger_repository.delete_passenger_by_index(index)

    def update_passenger_by_index(self, index, first_name, last_name, passport_number):
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

        if not is_passenger_index_valid(self.__passenger_repository, index):
            raise IndexError("Invalid index")

        if passport_number is not None:
            if not is_passport_number_valid(self.__passenger_repository, passport_number):
                raise ValueError("Invalid data")

        self.__passenger_repository.update_passenger_by_index(index, first_name, last_name, passport_number)

    def get_all_passengers(self):
        """
        Returns all passengers in the repository
        :return: the list of passengers
        :rtype: list of Passenger
        """
        return self.__passenger_repository.passengers
