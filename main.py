from io_interface import IOInterface
from operation_customer import CustomerOperation
from operation_user import UserOperation
from operation_product import ProductOperation

main_loop = True


def customer_update(user):
    input_reference = {"1": "username", "2": "password", "3": "email address", "4": "mobile number"}
    update_set = set()
    IOInterface.update_details()
    choice_list = IOInterface.get_user_input("Enter: ", num_of_args=4)
    for choice in choice_list:
        try:
            if choice and not (0 < int(choice) < 5):
                IOInterface.print_error_message("main.customer_update()", "Input out of range!")
                return  # escape function if input is out of range
        except ValueError:
            IOInterface.print_error_message("main.customer_update()", "Enter only a number!")
            return  # escape function if input is not a value

        if choice in input_reference:
            update_set.add(input_reference[choice])
    if not update_set:
        update_set = {input_reference[item] for item in input_reference}
    update_data = process_customer(update_set, user.user_name)
    return None if not update_data else CustomerOperation.update_profile(update_data, user)


def process_customer(register_update=None, customer_name=None):
    reg = {  # the value in dict is a list w/ x3 items:
        # 1) an empty string to accept user input & 2) display function to show user input requirements
        # 3) corresponding validation function to check input
        "username": ["", IOInterface.register_username, UserOperation.validate_username],
        "password": ["", IOInterface.register_password, UserOperation.validate_password],
        "email address": ["", IOInterface.register_email, CustomerOperation.validate_email],
        "mobile number": ["", IOInterface.register_mobile, CustomerOperation.validate_mobile]
    }

    if not register_update:
        IOInterface.register_requirement()
    else:
        IOInterface.print_message("__UPDATE PROFILE__\n")
    for area in reg:  # 'area' is a str: e.g: 'username', [...], 'mobile'
        if register_update and area not in register_update:
            continue
        while True:
            display_requirement, validation = reg[area][1], reg[area][2]
            display_requirement()
            IOInterface.go_to_menu()
            reg[area][0] = IOInterface.get_user_input(f"Enter {area}: ", num_of_args=1)[0]  # returns string
            if UserOperation.validate_menu(reg[area][0]):
                IOInterface.print_going_back()
                return
            if area == "username":
                if customer_name and customer_name == reg["username"][0]:
                    IOInterface.print_error_message("UserOperation.process_customer()",
                                                    "Username is identical. Try a different username!")
                    continue
                name_check = UserOperation.check_username_exist(reg["username"][0])
                if name_check:
                    IOInterface.print_error_message("UserOperation.check_username_exist()",
                                                    "Username already exists!" if type(name_check) == bool
                                                    else "FileNotFound or OS error")
                    continue
            if validation(reg[area][0]):
                break
            IOInterface.print_error_message(f"{validation.__module__}.{validation.__name__}()",
                                            f"\nINVALID: {area} failed the requirements. Please try again.")
    if register_update:
        return {data: reg[data][0] for data in register_update}
    if not CustomerOperation.register_customer(reg["username"][0], reg["password"][0],
                                               reg["email address"][0], reg["mobile number"][0]):
        IOInterface.print_error_message("UserOperation.generate_unique_user_id()",
                                        f"FileNotFound or OS error")


def customer_control(user):

    logged_in = True

    input_msg = {1: "__PROFILE__", 2: "__UPDATE PROFILE__", 3: "__PRODUCTS__",
                 4: "__HISTORY__", 5: "__FIGURES__", 6: "Logging out..."}

    while logged_in:

        IOInterface.customer_menu()

        try:
            raw_choice, keyword = IOInterface.get_user_input("Enter: ", num_of_args=2)
            choice = int(raw_choice[0])
            if 0 < int(raw_choice) < 7:
                IOInterface.print_message(input_msg[choice] + "\n")

                if choice == 1:  # show profile
                    IOInterface.text_box(user.__str__())
                elif choice == 2:  # update profile
                    user_update = customer_update(user)
                    user = user if not user_update else user_update
                elif choice == 3:  # show products (input could have keyword)
                    ProductOperation.extract_products_from_files()
                elif choice == 4:  # show history orders
                    pass
                elif choice == 5:  # generate all consumption figures
                    pass
                else:  # log out
                    logged_in = False

            else:
                IOInterface.print_error_message("main.customer_control()",
                                                "Input out of range! Try again...")

        except ValueError:
            IOInterface.print_error_message("main.customer_control()",
                                            "Enter only a number! Try again...")


def login_control():
    global main_loop

    IOInterface.main_menu()
    try:
        choice = int(IOInterface.get_user_input("Enter: ", num_of_args=1)[0])  # returns int
        if 0 < choice < 4:
            IOInterface.print_message(
                "\n__LOGIN__\n" if choice == 1 else "\n__REGISTER__\n" if choice == 2 else "Quitting...")

        else:
            IOInterface.print_error_message("main.login_control()",
                                            "Input out of range! Try again...")

        if choice == 1:  # user enters username & p/w to login
            user_name = IOInterface.get_user_input("Enter USERNAME: ",
                                                   num_of_args=1)[0]  # returns username @ 0th index
            user_password = IOInterface.get_user_input("Enter PASSWORD: ",
                                                       num_of_args=1)[0]  # returns p/w @ 0th index
            user_obj = UserOperation.login(user_name, user_password)
            if not user_obj or user_obj == 1:
                IOInterface.print_error_message("UserOperation.login()",
                                                "Unexpected error!" if user_obj == 1 else "Invalid details entered.")
                return
            customer_control(user_obj)

        elif choice == 2:  # user registers as new customer
            process_customer()
        elif choice == 3:
            main_loop = False

    except ValueError:
        IOInterface.print_error_message("main.login_control()",
                                        "Enter only a number! Try again...")


def admin_control():
    pass


def main():
    # TODO: REMOVE THIS
    ProductOperation.extract_products_from_files()
    while main_loop:
        login_control()


if __name__ == '__main__':
    main()
