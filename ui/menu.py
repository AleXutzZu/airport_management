from exceptions.invalid_input import InvalidInputError
from model.passenger import Passenger
from model.plane import Plane
from repository.passenger_repository import PassengerRepository
from repository.plane_repository import PlaneRepository
from service.passenger_controller import PassengerController
from service.plane_controller import PlaneController
from ui.application_ui import ApplicationUI


def print_menu():
    print("Airport management - 3rd iteration")
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
    print("---------Miscellaneous----------")
    print("18. Form groups of given size from passengers on a plane but with differing last names")
    print("19. Form groups of given size from planes with the same destination but different airline companies")
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
        passenger_repository.add_passenger(passenger)

    for plane in dummy_planes:
        plane_repository.add_plane(plane)

    plane_controller = PlaneController(plane_repository)
    passenger_controller = PassengerController(passenger_repository)
    application_ui = ApplicationUI(plane_controller, passenger_controller)

    while True:
        print_menu()
        try:
            data = execute_command(application_ui)
            if data is not None:
                if isinstance(data, list):
                    print(*data, sep="\n")
                else:
                    print(data)
        except InvalidInputError as e:
            print(f"Input is invalid, please try again ({e.args[0]})")


def execute_command(application_ui):
    choice = input("Enter a command: ")

    if choice == "1":
        return application_ui.add_passenger()
    elif choice == "2":
        return application_ui.get_passenger_by_index()
    elif choice == "3":
        return application_ui.delete_passenger_by_index()
    elif choice == "4":
        return application_ui.update_passenger_by_index()
    elif choice == "5":
        return application_ui.get_all_passengers()
    elif choice == "6":
        return application_ui.add_plane()
    elif choice == "7":
        return application_ui.get_plane_by_index()
    elif choice == "8":
        return application_ui.delete_plane_by_index()
    elif choice == "9":
        return application_ui.update_plane_by_index()
    elif choice == "10":
        return application_ui.get_all_planes()
    elif choice == "11":
        return application_ui.get_sorted_passengers_on_plane_by_last_name()
    elif choice == "12":
        return application_ui.get_sorted_planes_by_passenger_count()
    elif choice == "13":
        return application_ui.get_sorted_planes_by_count_of_passengers_matching_prefix()
    elif choice == "14":
        return application_ui.get_sorted_planes_by_concatenation()
    elif choice == "15":
        return application_ui.get_planes_with_common_passport_prefixes()
    elif choice == "16":
        return application_ui.get_passengers_on_plane_containing_string()
    elif choice == "17":
        return application_ui.get_all_planes_containing_passenger_with_name()
    elif choice == "18":
        return application_ui.generate_groups_of_passengers_with_differing_last_names()
    elif choice == "19":
        return application_ui.generate_groups_of_planes_with_same_destination_and_differing_airline()
    elif choice == "0":
        exit(0)
    else:
        print("Invalid command, try again")
