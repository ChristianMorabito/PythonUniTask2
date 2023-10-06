import os
from io_interface import IOInterface
from operation_customer import CustomerOperation
from operation_order import OrderOperation
from operation_user import UserOperation
from operation_product import ProductOperation
from operation_admin import AdminOperation

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
        except ValueError or IndexError:
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
                 4: "__HISTORY__", 5: "__FIGURES__", 6: "\nLogging out..."}

    IOInterface.print_message("SUCCESS!! You are now logged in\n")

    while logged_in:

        IOInterface.customer_menu()

        try:
            raw_choice, keyword = IOInterface.get_user_input("Enter: ", num_of_args=2)
            choice = int(raw_choice)
            if 0 < int(raw_choice) < 7:
                IOInterface.print_message("\n" + input_msg[choice] + "\n")
                if choice == 1:  # show profile
                    IOInterface.text_box(user.__str__())
                elif choice == 2:  # update profile
                    user_update = customer_update(user)
                    user = user if not user_update else user_update
                elif choice == 3:  # show products (input could have keyword)
                    show("data/products.txt", ProductOperation.pages_amount,
                         ProductOperation.get_product_list, None if not keyword else keyword)
                elif choice == 4:  # show history orders
                    pass
                elif choice == 5:  # generate all consumption figures
                    pass
                else:  # log out
                    logged_in = False

            else:
                IOInterface.print_error_message("main.customer_control()",
                                                "Input out of range! Try again...")

        except ValueError or IndexError:
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
                IOInterface.print_error_message("UserOperation.login()", "\n" +
                                                ("Unexpected error!" if user_obj == 1 else "Invalid details entered."))
                return

            IOInterface.print_message("\nLoading store data...\n")
            # 1) download data to products.txt if the file is empty
            if not ProductOperation.extract_products_from_files():
                IOInterface.print_error_message("operation_product.extract_products_from_files()",
                                                "Error loading store data. Logging out...")
                return
            # 2) establish length of orders+users .txt files & then use that data to establish page number amount
            # in orders+users .txt files
            CustomerOperation.set_len_and_pages()
            OrderOperation.set_len_and_pages()

            admin_control(user_obj) if user_obj.__class__.__name__ == "Admin" else customer_control(user_obj)

        elif choice == 2:  # user registers as new customer
            process_customer()
        elif choice == 3:
            main_loop = False

    except ValueError or IndexError:
        IOInterface.print_error_message("main.login_control()",
                                        "Enter only a number! Try again...")


def show(path, pages_amount, get_list_function, keyword=None):
    """
    Function is shared between customer & admin. It's the helper function to show either products,
    orders or users
    :param path: accepts string for file path
    :param pages_amount: accepts int which is the amount of pages in a file (10 items = 1 page)
    :param get_list_function: accepts function to call specific list
    :param keyword: if customer wants to search a keyword instead of product pages, then they have that option
    :return: None
    """
    if os.path.getsize(path) == 0:  # admin pathway
        IOInterface.print_message("Unable to show contents since file is empty!")
        return
    if path == "data/users.txt" and CustomerOperation.len_users_txt == 1:  # admin pathway
        # admin is not a customer, so if only admin in the customer list, then the list is considered empty
        IOInterface.print_message("Unable to show contents since file is empty!")
        return
    if keyword:  # customer pathway
        IOInterface.show_list(list_type=ProductOperation.get_product_list_by_keyword(keyword))
        return

    while True:
        try:
            page_no = IOInterface.get_user_input(f"Enter a page no. between 1 & "
                                                 f"{pages_amount}\n"
                                                 f"__type 'menu' to go back__: ", num_of_args=1)[0]
            if page_no == "menu":
                return
            if 0 < int(page_no) <= pages_amount:
                universal_list = get_list_function(int(page_no))[0]
                IOInterface.show_list(list_type=(universal_list, int(page_no), pages_amount))
            else:
                IOInterface.print_error_message("main.admin_show()",
                                                "Input out of range! Try again...")
        except ValueError or IndexError:
            IOInterface.print_error_message("main.admin_show()",
                                            "Enter only a number! Try again...")


def admin_control(user):  # TODO: does user arg need to be there?

    logged_in = True

    input_msg = {1: "__SHOW PRODUCTS__", 2: "__ADD CUSTOMERS__", 3: "__SHOW CUSTOMERS__",
                 4: "__SHOW ORDERS__", 5: "Generating test data...", 6: "__ALL STATISTICS__",
                 7: "__DELETE ALL DATA__", 8: "\nLogging out..."}

    IOInterface.print_message("SUCCESS!! You are now logged in as ADMIN.")

    while logged_in:
        IOInterface.admin_menu()
        try:
            raw_choice, keyword = IOInterface.get_user_input("Enter: ", num_of_args=2)
            choice = int(raw_choice)
            if 0 < choice < 9:
                IOInterface.print_message("\n" + input_msg[choice] + "\n")

                if choice == 1:  # show products
                    show("data/products.txt", ProductOperation.pages_amount, ProductOperation.get_product_list)
                elif choice == 2:  # add customers
                    pass
                elif choice == 3:  # show customers
                    show("data/users.txt", CustomerOperation.pages_amount, CustomerOperation.get_customer_list)
                elif choice == 4:  # show orders
                    show("data/orders.txt", OrderOperation.pages_amount, OrderOperation.get_order_list)
                elif choice == 5:  # generate test data
                    if ProductOperation.len_products_txt == 0:
                        IOInterface.print_message("Loading store data...")
                    test_data = OrderOperation.generate_test_order_data()
                    if not test_data:
                        IOInterface.print_error_message("operation_order.generation_test_order_data()",
                                                        "Unable to generate test data!" if type(test_data) == bool
                                                        else "Test data already generated!")
                    else:
                        IOInterface.print_message("Test data has been generated.")
                elif choice == 6:  # generate all statistical figures
                    pass
                elif choice == 7:  # delete all data
                    if (CustomerOperation.delete_all_customers() and
                            OrderOperation.delete_all_orders() and
                            ProductOperation.delete_all_products()):
                        IOInterface.print_message("All data has been deleted.")
                    else:
                        IOInterface.print_error_message("operation_{product, order & customer}.delete_all...()",
                                                        "Unable to delete all data!")
                else:  # log out
                    logged_in = False

            else:
                IOInterface.print_error_message("main.customer_control()",
                                                "Input out of range! Try again...")

        except ValueError or IndexError:
            IOInterface.print_error_message("main.customer_control()",
                                            "Enter only a number! Try again...")


def main():
    if not AdminOperation.register_admin():
        IOInterface.print_error_message("operation_admin.register_admin()",
                                        "Error registering admin. Unable to login as admin")
    while main_loop:
        login_control()


if __name__ == '__main__':
    main()
