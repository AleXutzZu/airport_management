from exceptions.invalid_input import InvalidInputError
from model.passenger import Passenger
from repository.passenger_repository import PassengerRepository
from validators.input.passenger_input_validators import get_validated_passenger_data, get_validated_index
from repository.plane_repository import PlaneRepository


def create_new_passenger(repository):
    """
    Reads user input necessary to add a new passenger to the repository, and adds it
    :param repository: the Passenger repository
    :type repository: PassengerRepository
    """

    first_name = input("Enter first name of passenger: ")
    last_name = input("Enter last name of passenger: ")
    passport_number = input("Enter passport number: ")

    first_name, last_name, passport_number = get_validated_passenger_data(first_name, last_name, passport_number)

    repository.add_passenger(first_name, last_name, passport_number)


def get_passenger_by_index(repository):
    """
    Reads index of the passenger to get, then returns it
    :param repository: the Passenger repository
    :type repository: PassengerRepository
    :return: the requested passenger, if it exists
    :rtype: Passenger
    """
    index = input("Enter index of passenger: ")
    index = get_validated_index(index)

    try:
        passenger = repository.find_passenger_by_index(index)
        return passenger
    except IndexError:
        raise InvalidInputError("Index is out of range")


def delete_passenger_by_index(passenger_repository, plane_repository):
    """
    Reads index of the passenger to delete, then deletes it
    :param plane_repository: the Plane repository
    :type plane_repository: PlaneRepository
    :param passenger_repository: the Passenger repository
    :type passenger_repository: PassengerRepository
    """

    index = input("Enter index of passenger: ")
    index = get_validated_index(index)

    try:
        passenger = passenger_repository.find_passenger_by_index(index)
        plane_repository.remove_passenger_from_planes(passenger)
        passenger_repository.delete_passenger_by_index(index)
    except IndexError:
        raise InvalidInputError("Index is out of range")


def update_passenger_by_index(repository):
    """
    Reads index of the passenger to update, then updates it with the data provided
    :param repository: the Passenger repository
    :type repository: PassengerRepository
    """

    index = input("Enter index of passenger: ")
    index = get_validated_index(index)

    first_name = input("Enter first name of passenger, leave blank to skip: ")
    last_name = input("Enter last name of passenger, leave blank to skip: ")
    passport_number = input("Enter passport number, leave blank to skip: ")

    if len(first_name) < 1:
        first_name = None

    if len(last_name) < 1:
        last_name = None

    if len(passport_number) < 1:
        passport_number = None

    first_name, last_name, passport_number = get_validated_passenger_data(first_name, last_name, passport_number)
    try:
        repository.update_passenger_by_index(index, first_name, last_name, passport_number)
    except IndexError:
        raise InvalidInputError("Index is out of range")
    except ValueError:
        raise InvalidInputError("Passport is not unique")


def get_all_passengers(repository):
    """
    Returns all passengers in the repository
    :param repository: the Passenger repository
    :type repository: PassengerRepository
    :return: the list of passengers
    :rtype: list of Passenger
    """
    return repository.passengers
