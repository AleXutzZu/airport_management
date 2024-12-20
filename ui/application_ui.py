from exceptions.invalid_input import InvalidInputError
from service.plane_controller import PlaneController
from validators.input.passenger_input_validators import get_validated_passenger_data
from validators.input.plane_input_validators import get_validated_plane_data, get_validated_index, \
    get_validated_group_size
from service.passenger_controller import PassengerController


class ApplicationUI:
    """
    UI for the application
    """

    def __init__(self, plane_controller, passenger_controller):
        """
        Initializes the view
        :param plane_controller: the plane controller
        :type plane_controller: PlaneController
        :param passenger_controller: the passenger controller
        :type passenger_controller: PassengerController
        """
        self.__plane_controller = plane_controller
        self.__passenger_controller = passenger_controller

    def add_passenger(self):
        """
        Reads user input necessary to add a new passenger to the repository, and adds it
        """

        first_name = input("Enter first name of passenger: ")
        last_name = input("Enter last name of passenger: ")
        passport_number = input("Enter passport number: ")

        first_name, last_name, passport_number = get_validated_passenger_data(first_name, last_name, passport_number)

        self.__passenger_controller.create_new_passenger(first_name, last_name, passport_number)

    def get_passenger_by_index(self):
        """
        Reads index of the passenger to get, then returns it
        :return: the requested passenger, if it exists
        :rtype: Passenger
        """
        index = input("Enter index of passenger: ")
        index = get_validated_index(index)

        try:
            passenger = self.__passenger_controller.get_passenger_by_index(index)
            return passenger
        except IndexError:
            raise InvalidInputError("Index is out of range")

    def delete_passenger_by_index(self):
        """
        Reads index of the passenger to delete, then deletes it
        """

        index = input("Enter index of passenger: ")
        index = get_validated_index(index)

        try:
            passenger = self.__passenger_controller.get_passenger_by_index(index)
            self.__plane_controller.remove_passenger_from_planes(passenger)
            self.__passenger_controller.delete_passenger_by_index(index)
        except IndexError:
            raise InvalidInputError("Index is out of range")

    def update_passenger_by_index(self):
        """
        Reads index of the passenger to update, then updates it with the data provided
        """

        index = input("Enter index of passenger: ")
        index = get_validated_index(index)

        first_name = input("Enter first name of passenger, leave blank to skip: ")
        last_name = input("Enter last name of passenger, leave blank to skip: ")
        passport_number = input("Enter passport number, leave blank to skip: ")

        if len(first_name) < 1:
            first_name = None

        if len(last_name) < 1:
            last_name = None

        if len(passport_number) < 1:
            passport_number = None

        first_name, last_name, passport_number = get_validated_passenger_data(first_name, last_name, passport_number)
        try:
            self.__passenger_controller.update_passenger_by_index(index, last_name, first_name, passport_number)
        except IndexError:
            raise InvalidInputError("Index is out of range")
        except ValueError:
            raise InvalidInputError("Passport is not unique")

    def get_all_passengers(self):
        """
        Returns all passengers in the repository
        :return: the list of passengers
        :rtype: list of Passenger
        """
        return self.__passenger_controller.get_all_passengers()

    def add_plane(self):
        airline = input("Enter the airline name: ")

        seats = input("Enter the number of seats: ")
        destination = input("Enter the destination: ")

        passengers = input("Enter the indices of the passengers: ")
        identification_number = input("Enter the identification number: ")

        airline, seats, destination, passengers, identification_number = get_validated_plane_data(airline, seats,
                                                                                                  destination,
                                                                                                  passengers,
                                                                                                  identification_number)
        try:
            passengers_objects = [self.__passenger_controller.get_passenger_by_index(x) for x in passengers]
            self.__plane_controller.create_new_plane(airline, seats, destination, passengers_objects,
                                                     identification_number)
        except ValueError:
            raise InvalidInputError("Invalid data")

    def get_plane_by_index(self):
        """
        Reads index of the plane to print, then returns it
        :return: the plane to search
        :rtype: Plane
        """
        index = input("Enter index of plane: ")
        index = get_validated_index(index)

        try:
            plane = self.__plane_controller.get_plane_by_index(index)
            return plane
        except IndexError:
            raise InvalidInputError("Index is out of range")

    def delete_plane_by_index(self):
        """
        Reads index of the plane to delete, then deletes it
        """

        index = input("Enter index of plane: ")
        index = get_validated_index(index)

        try:
            self.__plane_controller.delete_plane_by_index(index)
        except IndexError:
            raise InvalidInputError("Index is out of range")

    def update_plane_by_index(self):
        """
        Reads index of the plane to update, then updates it with the data provided
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
                                                                                                  destination,
                                                                                                  passengers,
                                                                                                  identification_number)
        try:
            passengers_objects = None
            if passengers is not None:
                passengers_objects = [self.__passenger_controller.get_passenger_by_index(x) for x in passengers]

            self.__plane_controller.update_plane_by_index(index, airline, seats, destination, passengers_objects,
                                                          identification_number)
        except ValueError:
            raise InvalidInputError("Invalid data")

    def get_all_planes(self):
        """
        Returns all the planes in the application
        :return: the list of planes
        :rtype: list of Plane
        """
        return self.__plane_controller.get_all_planes()

    def get_sorted_passengers_on_plane_by_last_name(self):
        """
        Reads index of the plane and returns all passengers in order of their last names
        :return: the sorted list of passengers
        :rtype: list of Passenger
        """
        index = input("Enter index of plane: ")
        index = get_validated_index(index)

        return self.__plane_controller.get_sorted_passengers_on_plane_by_last_name(index)

    def get_sorted_planes_by_passenger_count(self):
        """
        Returns the planes sorted in ascending order of the number of passengers
        :return: the list of planes
        :rtype: list of Plane
        """
        return self.__plane_controller.get_sorted_planes_by_passenger_count()

    def get_sorted_planes_by_count_of_passengers_matching_prefix(self):
        """
        Reads a string to count the number of passengers matching this as a prefix, and orders the planes by
        this count
        :return: the list of planes
        :rtype: list of Plane
        """
        prefix = input("Enter string: ")
        return self.__plane_controller.get_sorted_planes_by_count_of_passengers_matching_prefix(prefix)

    def get_sorted_planes_by_concatenation(self):
        """
        Returns the planes sorted by the concatenation of the length of passengers with their destination
        :return: the list of planes
        :rtype: list of Plane
        """
        return self.__plane_controller.get_sorted_planes_by_concatenation()

    def get_planes_with_common_passport_prefixes(self):
        """
        Returns all the planes on which there are at least 2 passengers for which the first 3 letters of their passport
        numbers' match
        :return: the list of planes
        :rtype: list of Plane
        """
        return self.__plane_controller.get_planes_with_common_passport_prefixes()

    def get_passengers_on_plane_containing_string(self):
        """
        Reads a string and returns all passengers on a given plane for which their first or last name contain this string
        :return: the list of passengers
        :rtype: list of Passenger
        """

        index = input("Enter index of plane: ")
        index = get_validated_index(index)

        string = input("Enter string: ")
        return self.__plane_controller.get_passengers_on_plane_containing_string(index, string)

    def get_all_planes_containing_passenger_with_name(self):
        """
        Reads a name and returns all planes on which a passenger's first or last name exactly matches the given string
        :return: the list of planes
        :rtype: list of Plane
        """

        name = input("Enter passenger's name: ")
        return self.__plane_controller.get_all_planes_containing_passenger_with_name(name)

    def generate_groups_of_passengers_with_differing_last_names(self):
        """
        Reads the index of a plane and a group size and generates all groups of passengers which are on this plane
        and have differing last names
        :return: the list of groups
        :rtype: list
        """
        index = input("Enter index of plane: ")
        index = get_validated_index(index)

        group_size = input("Enter the size of the groups: ")
        group_size = get_validated_group_size(group_size)

        return self.__plane_controller.get_all_groups_of_passengers_with_differing_last_names(index, group_size)

    def generate_groups_of_planes_with_same_destination_and_differing_airline(self):
        """
        Reads the group size and generates all groups of planes which have the same destination but are owned
        by different airlines
        :return: the list of groups
        :rtype: list
        """

        group_size = input("Enter the size of the groups: ")
        group_size = get_validated_group_size(group_size)

        return self.__plane_controller.get_all_groups_of_planes_with_same_destination_but_other_airlines(group_size)
