def is_passenger_index_valid(repository, index):
    """
    Checks whether an index is valid for the list of passengers
    :param repository: the Passenger repository
    :type repository: PassengerRepository
    :param index: the index to check
    :return: True if the index is valid, False otherwise
    :rtype: bool
    """
    return 0 <= index < len(repository.passengers)


def is_passport_number_valid(repository, passport_number):
    """
    Checks whether the specified passport number already exists or not
    :param repository: the Passenger repository
    :type repository: PassengerRepository
    :param passport_number: the passport number to check
    :type passport_number: str
    :return: True if the passport number is valid, False otherwise
    :rtype: bool
    """
    return passport_number not in [x.passport_number for x in repository.passengers]
