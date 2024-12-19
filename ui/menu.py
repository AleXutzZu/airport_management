from exceptions.invalid_input import InvalidInputError
from model.passenger import Passenger
from model.plane import Plane
from repository.passenger_repository import PassengerRepository
from repository.plane_repository import PlaneRepository
from service.passenger_controller import create_new_passenger, get_passenger_by_index, delete_passenger_by_index, \
    update_passenger_by_index, get_all_passengers
from service.plane_controller import get_plane_by_index, delete_plane_by_index, create_new_plane, update_plane_by_index, \
    get_all_planes, get_sorted_passengers_on_plane_by_last_name, get_sorted_planes_by_passenger_count, \
    get_sorted_planes_by_count_of_passengers_matching_prefix, get_sorted_planes_by_concatenation, \
    get_planes_with_common_passport_prefixes, get_passengers_on_plane_matching_prefix, \
    get_all_planes_containing_passenger_with_name


def print_menu():
    print("Airport management - 2nd iteration")
    print("----------------------------------")
    print("-------Passenger operations-------")
    print("1. Add a passenger")
    print("2. Display passenger info by given index")
    print("3. Delete a passenger by given index")
    print("4. Update passenger info by given index")
    print("5. List all passengers")
    print("--------Plane operations---------")
    print("6. Add a new plane")
    print("7. Display plane info by given index")
    print("8. Delete a plane by given index")
    print("9. Update plane info by given index")
    print("10. List all planes")
    print("---------Sort & filter-----------")
    print("11. Sort passengers on a plane by last name")
    print("12. Sort all planes by the number of passengers")
    print("13. Sort all planes by the number of passengers which match a given prefix as a first name")
    print("14. Sort all planes by the concatenation of the count of passengers and the destination")
    print("15. Find planes on which there exists passengers with equal prefix of length 3 of the passport number")
    print("16. Find passengers on a plane which contain in the first or last name a given string")
    print("17. Find all planes boarded by a passenger with the given name")
    print("0. Exit")
    print("----------------------------------")


def start():
    passenger_repository = PassengerRepository()
    plane_repository = PlaneRepository()

    dummy_passengers = [
        Passenger("A", "B", "1"),
        Passenger("C", "D", "2"),
        Passenger("E", "F", "3"),
    ]

    dummy_planes = [
        Plane("A", 10, "d1", [dummy_passengers[0], dummy_passengers[1]], 1),
        Plane("B", 200, "d2", [dummy_passengers[0], dummy_passengers[2]], 2),
        Plane("C", 50, "d3", dummy_passengers, 3),
    ]

    for passenger in dummy_passengers:
        passenger_repository.add_passenger(passenger.first_name, passenger.last_name, passenger.passport_number)

    for plane in dummy_planes:
        plane_repository.add_plane(plane.airline, plane.seats, plane.destination, plane.passengers,
                                   plane.identification_number)

    while True:
        print_menu()
        choice = input("Enter a command: ")

        if choice == "1":
            execute_command(create_new_passenger, passenger_repository)
        elif choice == "2":
            execute_command(get_passenger_by_index, passenger_repository)
        elif choice == "3":
            execute_command(delete_passenger_by_index, passenger_repository, plane_repository)
        elif choice == "4":
            execute_command(update_passenger_by_index, passenger_repository)
        elif choice == "5":
            execute_command(get_all_passengers, passenger_repository)
        elif choice == "6":
            execute_command(create_new_plane, plane_repository, passenger_repository)
        elif choice == "7":
            execute_command(get_plane_by_index, plane_repository)
        elif choice == "8":
            execute_command(delete_plane_by_index, plane_repository)
        elif choice == "9":
            execute_command(update_plane_by_index, plane_repository, passenger_repository)
        elif choice == "10":
            execute_command(get_all_planes, plane_repository)
        elif choice == "11":
            execute_command(get_sorted_passengers_on_plane_by_last_name, plane_repository)
        elif choice == "12":
            execute_command(get_sorted_planes_by_passenger_count, plane_repository)
        elif choice == "13":
            execute_command(get_sorted_planes_by_count_of_passengers_matching_prefix, plane_repository)
        elif choice == "14":
            execute_command(get_sorted_planes_by_concatenation, plane_repository)
        elif choice == "15":
            execute_command(get_planes_with_common_passport_prefixes, plane_repository)
        elif choice == "16":
            execute_command(get_passengers_on_plane_matching_prefix, plane_repository)
        elif choice == "17":
            execute_command(get_all_planes_containing_passenger_with_name, plane_repository)
        elif choice == "0":
            break
        else:
            print("Invalid command, try again")


def execute_command(function, *repositories):
    try:
        data = function(*repositories)
        if data is not None:
            if isinstance(data, list):
                print(*data, sep="\n")
            else:
                print(data)

    except InvalidInputError as e:
        print(f"Input is invalid, please try again ({e.args[0]})")
