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
    :type passport_number: int
    :return: True if the passport number is valid, False otherwise
    :rtype: bool
    """
    return passport_number not in [x.passport_number for x in repository.passengers]


def is_passenger_data_valid(repository, first_name, last_name, passport_number):
    """
    Checks whether the specified data is valid or not
    :param repository: the Passenger repository
    :type repository: PassengerRepository
    :param passport_number: the new passport number to check, can be None to be left unchanged
    :type passport_number: int or None
    :param last_name: the new last name to check, can be None to be left unchanged
    :type last_name: str or None
    :param first_name: the new first name to check, can be None to be left unchanged
    :type first_name: str or None
    :return: True if the data is valid, False otherwise
    :rtype: bool
    """
    if passport_number is not None:
        if not is_passport_number_valid(repository, passport_number):
            return False

    if first_name is not None:
        if len(first_name) < 1:
            return False

    if last_name is not None:
        if len(last_name) < 1:
            return False

    return True
