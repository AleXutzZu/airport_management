from exceptions.invalid_input import InvalidInputError
from utils.utils import merge_sort
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


def get_sorted_passengers_on_plane_by_last_name(plane_repository):
    """
    Returns the passengers sorted by last name on a given plane
    :param plane_repository: the Plane repository
    :type plane_repository: PlaneRepository
    :return: the list of passengers
    :rtype: list of Passenger
    """
    plane = get_plane_by_index(plane_repository)

    return merge_sort(plane.passengers, lambda x, y: x.last_name < y.last_name)


def get_sorted_planes_by_passenger_count(plane_repository):
    """
    Returns the planes sorted in ascending order of the number of passengers
    :param plane_repository: the Plane repository
    :type plane_repository: PlaneRepository
    :return: the list of planes
    :rtype: list of Plane
    """
    return merge_sort(plane_repository.planes, lambda x, y: len(x.passengers) < len(y.passengers))


def get_sorted_planes_by_count_of_passengers_matching_prefix(plane_repository):
    prefix = input("Enter the prefix to search for in passenger first names: ")

    def comparator(plane_lhs, plane_rhs):
        count_lhs, count_rhs = 0, 0

        for passenger in plane_lhs.passengers:
            if len(passenger.first_name) < len(prefix):
                continue

            l = len(prefix)
            if passenger.first_name[:l] == prefix:
                count_lhs += 1

        for passenger in plane_rhs.passengers:
            if len(passenger.first_name) < len(prefix):
                continue
            l = len(prefix)
            if passenger.first_name[:l] == prefix:
                count_rhs += 1

        return count_lhs < count_rhs

    return merge_sort(plane_repository.planes, comparator)


def get_sorted_planes_by_concatenation(plane_repository):
    """
    Returns the planes sorted in ascending order by the concatenation of the number of passengers with the destination
    :param plane_repository: the Plane repository
    :type plane_repository: PlaneRepository
    :return: the list of planes
    :rtype: list of Plane
    """

    return merge_sort(plane_repository.planes,
                      lambda x, y: str(x.passengers) + x.destination < str(y.passengers) + y.destination)


def get_planes_with_common_passport_prefixes(plane_repository):
    answer = []

    for plane in plane_repository.planes:
        counts = {}
        for passenger in plane.passengers:
            if len(passenger.passport_number) >= 3:
                if passenger.passport_number[0:3] not in counts:
                    counts[passenger.passport_number[0:3]] = 1
                else:
                    counts[passenger.passport_number[0:3]] += 1

        for value in counts.values():
            if value >= 2:
                answer.append(plane)
                break


def get_passengers_on_plane_matching_prefix(plane_repository):
    plane = get_plane_by_index(plane_repository)

    prefix = input("Enter the string you want to search for in the first name and last name: ")

    return [passenger for passenger in plane.passengers if
            prefix in passenger.last_name or prefix in passenger.first_name]


def get_all_planes_containing_passenger_with_name(plane_repository):
    name = input("Enter the name of the passenger to search: ")

    answer = []

    for plane in plane_repository.planes:
        for passenger in plane.passengers:
            if passenger.last_name == name or passenger.first_name == name:
                answer.append(plane)
                break
    return answer
