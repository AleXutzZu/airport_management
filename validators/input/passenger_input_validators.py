from exceptions.invalid_input import InvalidInputError


def get_validated_passenger_data(first_name, last_name, passport_number):
    """
    Validates passenger data
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
        pass

    if last_name is not None:
        pass

    if passport_number is not None:
        pass

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
