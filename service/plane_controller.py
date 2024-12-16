from exceptions.invalid_input import InvalidInputError
from validators.input.plane_input_validators import get_validated_index, get_validated_plane_data
from repository.plane_repository import PlaneRepository
from repository.passenger_repository import PassengerRepository


def create_new_plane(plane_repository, passenger_repository):
    """
    Reads user input necessary to add a new passenger to the repository, and adds it
    :param plane_repository: the Plane repository
    :type plane_repository: PlaneRepository
    :param passenger_repository: the Passenger repository
    :type passenger_repository: PassengerRepository
    """
    airline = input("Enter the airline name: ")
    seats = input("Enter the number of seats: ")
    destination = input("Enter the destination: ")
    passengers = input("Enter the indices of the passengers: ")
    identification_number = input("Enter the identification number: ")

    airline, seats, destination, passengers, identification_number = get_validated_plane_data(airline, seats,
                                                                                              destination, passengers,
                                                                                              identification_number)
    try:
        passengers_objects = [passenger_repository.find_passenger_by_index(x) for x in passengers]
        plane_repository.add_plane(airline, seats, destination, passengers_objects, identification_number)
    except ValueError:
        raise InvalidInputError("Invalid data")


def get_plane_by_index(repository):
    """
    Reads index of the plane to print, then prints it
    :param repository: the Plane repository
    :type repository: PlaneRepository
    """
    index = input("Enter index of plane: ")
    index = get_validated_index(index)

    try:
        plane = repository.find_plane_by_index(index)
        return plane
    except IndexError:
        raise InvalidInputError("Index is out of range")


def delete_plane_by_index(repository):
    """
    Reads index of the plane to delete, then deletes it
    :param repository: the Plane repository
    :type repository: PlaneRepository
    """

    index = input("Enter index of plane: ")
    index = get_validated_index(index)

    try:
        repository.delete_plane_by_index(index)
    except IndexError:
        raise InvalidInputError("Index is out of range")


def update_plane_by_index(plane_repository, passenger_repository):
    """
    Reads index of the plane to update, then updates it with the data provided
    :param plane_repository: the Plane repository
    :type plane_repository: PlaneRepository
    :param passenger_repository: the Passenger repository
    :type passenger_repository: PassengerRepository
    """
    index = input("Enter index of plane: ")
    index = get_validated_index(index)

    airline = input("Enter the airline name, leave blank to skip: ")
    seats = input("Enter the number of seats, leave blank to skip: ")
    destination = input("Enter the destination, leave blank to skip: ")
    passengers = input("Enter the indices of the passengers, leave blank to skip, write [] to empty: ")
    identification_number = input("Enter the identification number, leave blank to skip: ")

    if len(airline) < 1:
        airline = None

    if len(seats) < 1:
        seats = None

    if len(destination) < 1:
        destination = None

    if passengers == "[]":
        passengers = ""
    elif len(passengers) < 1:
        passengers = None

    if len(identification_number) < 1:
        identification_number = None

    airline, seats, destination, passengers, identification_number = get_validated_plane_data(airline, seats,
                                                                                              destination, passengers,
                                                                                              identification_number)

    try:
        passengers_objects = None
        if passengers is not None:
            passengers_objects = [passenger_repository.find_passenger_by_index(x) for x in passengers]

        plane_repository.update_plane_by_index(index, airline, seats, destination, passengers_objects,
                                               identification_number)
    except ValueError:
        raise InvalidInputError("Invalid data")


def get_all_planes(repository):
    """
    Returns all planes in the repository
    :param repository: the Plane repository
    :type repository: PlaneRepository
    :return: the list of planes
    :rtype: list of Plane
    """
    return repository.planes
