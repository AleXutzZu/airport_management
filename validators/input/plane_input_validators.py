from exceptions.invalid_input import InvalidInputError


def get_validated_plane_data(airline, seats, destination, passengers, identification_number):
    if airline is not None:
        pass

    if seats is not None:
        try:
            seats = int(seats)
        except ValueError:
            raise InvalidInputError("Seats must be an integer")

    if destination is not None:
        pass

    passenger_indices = None
    if passengers is not None:
        try:
            passenger_indices = [int(x) for x in passengers.split()]
        except ValueError:
            raise InvalidInputError("Expected a list of integers")

    if identification_number is not None:
        try:
            identification_number = int(identification_number)
        except ValueError:
            raise InvalidInputError("Identification number must be an integer")

    return airline, seats, destination, passenger_indices, identification_number


def get_validated_index(index):
    """
    Validates an index to be an integer value
    :param index: the index
    :return: the given index as an integer, or throws InvalidInputError
    """
    try:
        index = int(index)
    except ValueError:
        raise InvalidInputError("Index must be an integer")
    return index
