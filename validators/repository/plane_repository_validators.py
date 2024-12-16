def is_plane_index_valid(repository, index):
    """
    Checks whether a plane index is valid.
    :param repository: the Plane repository
    :type repository: PlaneRepository
    :param index: the plane index
    :type index: int
    :return: True if the plane index is valid, False otherwise
    :rtype: bool
    """
    return 0 <= index < len(repository.planes)


def is_identification_number_valid(repository, identification_number):
    """
    Checks whether the identification number is not already used
    :param repository: the Plane repository
    :type repository: PlaneRepository
    :param identification_number: the identification number
    :return: True if the identification number is unique, False otherwise
    :rtype: bool
    """
    return identification_number not in [x.identification_number for x in repository.planes]


def is_plane_data_valid(repository, airline, seats, destination, passengers, identification_number):
    """
    Checks whether a plane update data is valid.
    :param passengers: the new list of passengers to check, can be None to be left unchanged
    :type passengers: list of Passenger or None
    :param repository: the plane repository
    :type repository: PlaneRepository
    :param airline: the new airline name to check, can be None to be left unchanged
    :type airline: str or None
    :param seats: the number of seats to check, can be None to be left unchanged
    :type seats: int or None
    :param destination: the destination to check, can be None to be left unchanged
    :type destination: str or None
    :param identification_number: the identification number to check, can be None to be left unchanged
    :type identification_number: int or None
    :return: True if the plane update data is valid, False otherwise
    :rtype: bool
    """

    if identification_number is not None:
        if not is_identification_number_valid(repository, identification_number):
            return False

    if airline is not None:
        if len(airline) < 1:
            return False

    if seats is not None:
        if seats < 0:
            return False

    if destination is not None:
        if len(destination) < 1:
            return False

    if passengers is not None:
        if len(passengers) < 1:
            return False

    return True
