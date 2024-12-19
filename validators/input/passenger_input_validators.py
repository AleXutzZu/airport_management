from exceptions.invalid_input import InvalidInputError


def get_validated_passenger_data(first_name, last_name, passport_number):
    """
    Validates and returns passenger data necessary to create or update a passenger
    :param first_name: the first name
    :type first_name: str or None
    :param last_name: the last name
    :type last_name: str or None
    :param passport_number: the passport number
    :type passport_number: str or None
    :return: the passenger data
    :rtype: tuple
    """

    if first_name is not None:
        if len(first_name) < 1:
            raise InvalidInputError("First name cannot be empty")

    if last_name is not None:
        if len(last_name) < 1:
            raise InvalidInputError("Last name cannot be empty")

    if passport_number is not None:
        if len(passport_number) < 1:
            raise InvalidInputError("Passport number cannot be empty")

    return first_name, last_name, passport_number


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
