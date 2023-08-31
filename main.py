from io_interface import IOInterface
from operation_customer import CustomerOperation
from operation_user import UserOperation
from operation_order import OrderOperation
from operation_product import ProductOperation


def login_control():
    while True:  # receive & validate input for: login/register/quit
        try:
            choice = int(IOInterface.get_user_input("Enter 1, 2 or 3: ", num_of_args=1)[0])  # returns str @ 0th index
            if 0 < choice < 4:
                IOInterface.print_message(
                    "\n__LOGIN__\n" if choice == 1 else "\n__REGISTER__\n" if choice == 2 else "Quitting...")
                break
            IOInterface.print_error_message("main.login_control()", "Input out of range! Try again...")
        except ValueError:
            IOInterface.print_error_message("main.login_control()", "Enter only a number! Try again...")

    if choice == 1:  # user enters username & p/w to login
        user_name = IOInterface.get_user_input("Enter USERNAME: ", num_of_args=1)[0]  # returns username @ 0th index
        user_password = IOInterface.get_user_input("Enter PASSWORD: ", num_of_args=1)[0]  # returns p/w @ 0th index
        UserOperation.login(user_name, user_password)
    elif choice == 2:  # user registers as new customer
        customer_control()


def customer_control():
    reg = {
        "username": ["", UserOperation.validate_username],
        "password": ["", UserOperation.validate_password],
        "email address": ["", CustomerOperation.validate_email],
        "mobile number": ["", CustomerOperation.validate_mobile]
    }
    IOInterface.print_message("Customer registration requires:"
                              "\n\t\tuser-name, password, email address, & mobile number.\n")
    for area in reg:
        while True:
            reg[area][0] = IOInterface.get_user_input(f"Enter {area}: ", num_of_args=1)[0]  # returns str @ 0th index
            if reg[area][1](reg[area][0]):  # reg[area][1] is the function, & reg[area][0] is the str. arg.
                break
            IOInterface.print_error_message(f"{reg[area][1].__module__}.{reg[area][1].__name__}()",
                                            f"INVALID: {area} did not meet login requirements")


    CustomerOperation.register_customer(reg["username"], reg["password"], reg["email address"], reg["mobile number"])



def admin_control():
    pass


def main():
    IOInterface.main_menu()
    login_control()


if __name__ == '__main__':
    main()
