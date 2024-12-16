from exceptions.invalid_input import InvalidInputError
from repository.passenger_repository import PassengerRepository
from repository.plane_repository import PlaneRepository
from service.passenger_controller import create_new_passenger, get_passenger_by_index, delete_passenger_by_index, \
    update_passenger_by_index, get_all_passengers
from service.plane_controller import get_plane_by_index, delete_plane_by_index, create_new_plane, update_plane_by_index, \
    get_all_planes


def print_menu():
    print("Airport management - 1st iteration")
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
    print("0. Exit")
    print("----------------------------------")


def start():
    passenger_repository = PassengerRepository()
    plane_repository = PlaneRepository()
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
        elif choice == "0":
            break
        else:
            print("Invalid command, try again")


def execute_command(function, *repositories):
    try:
        data = function(*repositories)
        if data is not None:
            print(data)
    except InvalidInputError as e:
        print(f"Input is invalid, please try again ({e.args[0]})")
