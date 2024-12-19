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
