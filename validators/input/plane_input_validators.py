from exceptions.invalid_input import InvalidInputError


def get_validated_plane_data(airline, seats, destination, passengers, identification_number):
    """
    Validates the data necessary to create or update a plane and returns the processed data.
    Parameters passed as None are not checked but are still returned
    :param airline: the airline name
    :type airline: str or None
    :param seats: the number of seats
    :type seats: str or None
    :param destination: the destination
    :type destination: str or None
    :param passengers: the listo of passengers
    :type passengers: str or None
    :param identification_number: the identification number
    :type identification_number: str or None
    :return: a tuple with all processed values
    :rtype: tuple
    """
    if airline is not None:
        if len(airline) < 1:
            raise InvalidInputError("Airline name must not be empty")

    if seats is not None:
        try:
            seats = int(seats)
            if seats <= 0:
                raise InvalidInputError("Seats must be greater than zero")
        except ValueError:
            raise InvalidInputError("Seats must be an integer")

    if destination is not None:
        if len(destination) < 1:
            raise InvalidInputError("Destination name must not be empty")

    passenger_indices = None
    if passengers is not None:
        try:
            passenger_indices = [int(x) for x in passengers.split()]
        except ValueError:
            raise InvalidInputError("Expected a list of integers")

    if identification_number is not None:
        try:
            identification_number = int(identification_number)
            if identification_number <= 0:
                raise InvalidInputError("Identification number must be greater than zero")
        except ValueError:
            raise InvalidInputError("Identification number must be an integer")

    return airline, seats, destination, passenger_indices, identification_number


def get_validated_index(index):
    """
    Validates an index to be an integer value
    :param index: the index
    :return: the given index as an integer, or throws InvalidInputError
    :rtype: int
    """
    try:
        index = int(index)
    except ValueError:
        raise InvalidInputError("Index must be an integer")
    return index


def get_validated_group_size(group_size):
    """
    Validates a group size to be an integer
    :param group_size: the group size
    :return: the given group size as an integer
    :rtype: int
    """
    try:
        group_size = int(group_size)
        if group_size <= 0:
            raise InvalidInputError("Group size must be greater than zero")
    except ValueError:
        raise InvalidInputError("Group size must be an integer")
    return group_size
