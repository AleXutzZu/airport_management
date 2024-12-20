from model.plane import Plane
from repository.plane_repository import PlaneRepository
from utils.utils import merge_sort
from validators.repository.plane_repository_validators import is_identification_number_valid, is_plane_index_valid


class PlaneController:
    """
    Controller responsible for operations on planes
    """

    def __init__(self, repository):
        """
        Creates a plane controller
        :param repository: the plane repository
        :type repository: PlaneRepository
        """
        self.__plane_repository = repository

    def create_new_plane(self, airline, seats, destination, passengers, identification_number):
        """
        Adds a new plane
        :param airline: airline name
        :type airline: str
        :param seats: number of seats
        :type seats: int
        :param destination: destination plane
        :type destination: str
        :param passengers: passengers
        :type passengers: list of Passenger
        :param identification_number: identification number
        :type identification_number: int
        """
        if not is_identification_number_valid(self.__plane_repository, identification_number):
            raise ValueError("Data is invalid")

        plane = Plane(airline, seats, destination, passengers, identification_number)

        self.__plane_repository.add_plane(plane)

    def get_plane_by_index(self, index):
        """
        Returns the plane at the given index
        :param index: the index of the plane
        :type index: int
        :return: the plane to return
        :rtype: Plane
        """
        if not is_plane_index_valid(self.__plane_repository, index):
            raise IndexError("Plane index is invalid")
        return self.__plane_repository.find_plane_by_index(index)

    def delete_plane_by_index(self, index):
        """
        Deletes the plane at the given index
        :param index: the index of the plane
        :type index: int
        """
        if not is_plane_index_valid(self.__plane_repository, index):
            raise IndexError("Plane index is invalid")
        self.__plane_repository.delete_plane_by_index(index)

    def update_plane_by_index(self, index, airline, seats, destination, passengers, identification_number):
        """
        Updates the plane at the given index
        :param index: the index of the plane
        :type index: int
        :param airline: the new airline company owning the plane, can be None to leave unchanged
        :type airline: str or None
        :param seats: the new number of seats
        :type seats: int or None
        :param destination: the new destination, can be None to leave unchanged
        :type destination: str or None
        :param passengers: the new passengers, can be None to leave unchanged
        :type passengers: list of Passenger or None
        :param identification_number: the new identification number, can be None to leave unchanged
        :type identification_number: int or None
        """

        if not is_plane_index_valid(self.__plane_repository, index):
            raise IndexError("Plane index is invalid")

        if identification_number is not None:
            if not is_identification_number_valid(self.__plane_repository, identification_number):
                raise ValueError("Invalid data")

        self.__plane_repository.update_plane_by_index(index, airline, seats, destination, passengers,
                                                      identification_number)

    def remove_passenger_from_planes(self, passenger):
        """
        Removes the passenger from all planes which contain them
        :param passenger: the passenger to remove
        :type passenger: Passenger
        """
        for plane in self.__plane_repository.planes:
            if passenger in plane.passengers:
                plane.passengers.remove(passenger)

    def get_all_planes(self):
        """
        Returns all planes in the repository
        :return: the list of planes
        :rtype: list of Plane
        """
        return self.__plane_repository.planes

    def get_sorted_passengers_on_plane_by_last_name(self, index):
        """
        Returns the passengers sorted by last name on a given plane
        :param index: the index of the plane
        :type index: int
        :return: the list of passengers
        :rtype: list of Passenger
        """

        plane = self.get_plane_by_index(index)
        return merge_sort(plane.passengers, lambda x, y: x.compare_by_last_name(y))

    def get_sorted_planes_by_passenger_count(self):
        """
        Returns the planes sorted in ascending order of the number of passengers
        :return: the list of planes
        :rtype: list of Plane
        """
        return merge_sort(self.get_all_planes(), lambda x, y: x.compare_by_passenger_count(y))

    def get_sorted_planes_by_count_of_passengers_matching_prefix(self, prefix):
        """
        Returns the planes sorted by the number of appearances of a given prefix in the first name
        :param prefix: the prefix to use
        :type prefix: str
        :return: the sorted list of planes
        :rtype: list of Plane
        """

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

        return merge_sort(self.__plane_repository.planes, comparator)

    def get_sorted_planes_by_concatenation(self):
        """
        Returns the planes sorted in ascending order by the concatenation of the number of passengers with the destination
        :return: the list of planes
        :rtype: list of Plane
        """
        return merge_sort(self.__plane_repository.planes,
                          lambda x, y: x.compare_by_passenger_destination_concatenation(y))

    def get_planes_with_common_passport_prefixes(self):
        """
        Returns the planes that have at least 2 passengers for which their passport numbers' matched
        the first 3 characters.
        :return: the list of planes
        :rtype: list of Plane
        """
        answer = []

        for plane in self.__plane_repository.planes:
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

        return answer

    def get_passengers_on_plane_containing_string(self, index, search):
        """
        Returns all passengers from a given plane for which their first name or last name contain the search term
        :param index: the index of the plane
        :type index: int
        :param search: the string to look for
        :type search: str
        :return: the passengers matching the search
        :rtype: list of Passenger
        """
        plane = self.get_plane_by_index(index)

        return [passenger for passenger in plane.passengers if
                search in passenger.last_name or search in passenger.first_name]

    def get_all_planes_containing_passenger_with_name(self, name):
        """Return all planes which contain a passenger with the first name or last name exactly matching a given
        name
        :param name: the name to search for
        :type name: str
        :return: all planes containing a such passenger
        :rtype: list of Plane
        """
        answer = []

        for plane in self.__plane_repository.planes:
            for passenger in plane.passengers:
                if passenger.last_name == name or passenger.first_name == name:
                    answer.append(plane)
                    break
        return answer

    def get_all_groups_of_passengers_with_differing_last_names(self, index, group_size):
        """
        Returns a list with all possible combinations of passengers on a given plane for which their last names
        differ
        :param index: the index of the plane
        :type index: int
        :param group_size: the size of the group
        :type group_size: int
        :return: a list with all possible combinations, each combination being a list of size group_size
        :rtype: list
        """
        plane = self.get_plane_by_index(index)

        def is_candidate(group):
            for pos in group[:len(group) - 1]:
                if pos >= group[-1]:
                    return False
                if plane.passengers[pos].last_name == plane.passengers[group[-1]].last_name:
                    return False
            return True

        def generate_groups(step, current_group):
            for pos in range(len(plane.passengers)):
                current_group.append(pos)
                if is_candidate(current_group):
                    if step == group_size:
                        yield [plane.passengers[p] for p in current_group]
                    else:
                        yield from generate_groups(step + 1, current_group)
                current_group.pop()

        return list(generate_groups(1, []))

    def get_all_groups_of_planes_with_same_destination_but_other_airlines(self, group_size):
        """
        Returns a list with all possible combinations of planes for which the airline company differs but all planes
        have the same destination
        :param group_size: the size of the group
        :type group_size: int
        :return: a list with all possible combinations, each combination being a list of size group_size
        :rtype: list
        """

        def is_candidate(group):
            for pos in group[:len(group) - 1]:
                if pos >= group[-1]:
                    return False

                if self.get_plane_by_index(pos).airline == self.get_plane_by_index(group[-1]).airline:
                    return False

                if self.get_plane_by_index(pos).destination != self.get_plane_by_index(group[-1]).destination:
                    return False
            return True

        def generate_groups(step, current_group):
            for pos in range(len(self.get_all_planes())):
                current_group.append(pos)
                if is_candidate(current_group):
                    if step == group_size:
                        yield [self.get_plane_by_index(p) for p in current_group]
                    else:
                        yield from generate_groups(step + 1, current_group)
                current_group.pop()

        return list(generate_groups(1, []))
