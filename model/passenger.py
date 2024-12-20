class Passenger:
    """Class representing a passenger on a plane
    """

    def __init__(self, first_name, last_name, passport_number):
        """Constructor for Passenger class

        :param first_name: the first name of the passenger
        :type first_name: str
        :param last_name: the last name of the passenger
        :type last_name: str
        :param passport_number: the passport number of the passenger
        :type passport_number: str
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__passport_number = passport_number

    def __repr__(self):
        return f"Passenger(full_name: {self.first_name} {self.last_name}, passport: {self.passport_number})"

    @property
    def first_name(self):
        """
        Returns the first name of the passenger
        :return: the first name of the passenger
        :rtype: str
        """
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        """
        Sets the first name of the passenger
        :param value: the first name of the passenger
        :type value: str
        """
        self.__first_name = value

    @property
    def last_name(self):
        """
        Returns the last name of the passenger
        :return: the last name of the passenger
        :rtype: str
        """
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        """
        Sets the last name of the passenger
        :param value: the last name of the passenger
        :type value: str
        """
        self.__last_name = value

    @property
    def passport_number(self):
        """
        Returns the passport number of the passenger
        :return: the passport number of the passenger
        :rtype: str
        """
        return self.__passport_number

    @passport_number.setter
    def passport_number(self, value):
        """
        Sets the passport number of the passenger
        :param value: the passport number of the passenger
        :type value: str
        """
        self.__passport_number = value

    def __eq__(self, other):
        """
        Checks for equality between two Passenger objects
        :param other: the other passenger to compare with
        :type other: Passenger
        :return: True if all of their fields match, False otherwise
        :rtype: bool
        """
        if not isinstance(other, Passenger):
            return False

        return self.first_name == other.first_name and self.last_name == other.last_name and self.passport_number == other.passport_number

    def compare_by_last_name(self, other):
        """
        Compares this passenger to another passenger by their last names. This function provides strict ordering.
        :param other: the other passenger to compare with
        :type other: Passenger
        :return: True if this object comes before the other passenger, False otherwise
        :rtype: bool
        """
        return self.last_name < other.last_name
