from io_interface import IOInterface
from operation_customer import CustomerOperation
from operation_user import UserOperation

MAIN_LOOP = True


def login_control():
    global MAIN_LOOP
    while True:  # receive & validate input for: login/register/quit
        try:
            choice = int(IOInterface.get_user_input("Enter 1, 2 or 3: ", num_of_args=1)[0])  # returns int
            if 0 < choice < 4:
                IOInterface.print_message(
                    "\n__LOGIN__\n" if choice == 1 else "\n__REGISTER__\n" if choice == 2 else "Quitting...")
                break
            IOInterface.print_error_message("main.login_control()",
                                            "Input out of range! Try again...")
        except ValueError:
            IOInterface.print_error_message("main.login_control()",
                                            "Enter only a number! Try again...")

    if choice == 1:  # user enters username & p/w to login
        user_name = IOInterface.get_user_input("Enter USERNAME: ",
                                               num_of_args=1)[0]  # returns username @ 0th index
        user_password = IOInterface.get_user_input("Enter PASSWORD: ",
                                                   num_of_args=1)[0]  # returns p/w @ 0th index
        logged_obj = UserOperation.login(user_name, user_password)
        if not logged_obj or logged_obj == 1:
            IOInterface.print_error_message("UserOperation.login()",
                                            "Unexpected error!" if logged_obj == 1 else "Invalid details entered.")

    elif choice == 2:  # user registers as new customer
        customer_control()
    else:
        MAIN_LOOP = False


def customer_control():
    reg = {  # the value in dict is a list w/ x3 items:
             # 1) an empty string to accept user input & 2) display function to show user input requirements
             # 3) corresponding validation function to check input
        "username": ["", IOInterface.register_username, UserOperation.validate_username],
        "password": ["", IOInterface.register_password, UserOperation.validate_password],
        "email address": ["", IOInterface.register_email, CustomerOperation.validate_email],
        "mobile number": ["", IOInterface.register_mobile, CustomerOperation.validate_mobile]
    }
    IOInterface.register_requirement()
    for area in reg:  # 'area' is a str: e.g: 'username', [...], 'mobile'
        while True:
            display_requirement, validation = reg[area][1], reg[area][2]
            display_requirement()
            IOInterface.go_to_menu()
            reg[area][0] = IOInterface.get_user_input(f"Enter {area}: ", num_of_args=1)[0]  # returns string

            name_check = UserOperation.check_username_exist(reg["username"][0])
            if area == "username" and name_check:
                IOInterface.print_error_message("UserOperation.check_username_exist()",
                                                "Username already exists!" if type(name_check) == bool
                                                else "FileNotFound or OS error")
                continue
            if UserOperation.validate_menu(reg[area][0]):
                IOInterface.returning_to_menu()
                return
            if validation(reg[area][0]):
                break
            IOInterface.print_error_message(f"{validation.__module__}.{validation.__name__}()",
                                            f"\nINVALID: {area} failed the requirements. Please try again.")

    if not CustomerOperation.register_customer(reg["username"][0], reg["password"][0],
                                               reg["email address"][0], reg["mobile number"][0]):
        IOInterface.print_error_message("UserOperation.generate_unique_user_id()",
                                        f"FileNotFound or OS error")


def admin_control():
    pass


def main():
    while MAIN_LOOP:
        IOInterface.main_menu()
        login_control()


if __name__ == '__main__':
    main()
