class IOInterface:

    @staticmethod
    def get_user_input(message, num_of_args):
        """
        method accepts user input
        :param message: accepts str for input() arg prompt
        :param num_of_args: accepts int for num_of_args
        :return: returns [“arg1”, “arg2”, “arg3”]. If no. of input args is < num_of_args,
                 return the rest as empty str “”
        """
        try:
            arg_list = input(message).split()
            return [arg_list[i] if i < len(arg_list) else "" for i in range(num_of_args)]
        except IndexError:
            return

    @staticmethod
    def main_menu():
        """ method displays login menu, i.e. login, register & quit """
        print("\n__MAIN MENU__\n\n"
              "(1) Login\n"
              "(2) Register\n"
              "(3) Quit\n")

    @staticmethod
    def admin_menu():
        """
        method displays admin menu, i.e. show products, add customers, show customers,
        show orders, gen. test data, gen. all stat. figures, delete all data, & logout
        :return: None
        """
        print("__ADMIN MENU__\n\n"
              "(1) Show products\n"
              "(2) Add customers\n"
              "(3) Show customers\n"
              "(4) Show orders\n"
              "(5) Generate test data\n"
              "(6) Generate all statistical figures\n"
              "(7) Delete all data\n"
              "(8) Logout\n")

    @staticmethod
    def customer_menu():
        """
        method displays customer menu, i.e. show profile, update profile, show products,
        show history orders, gen. all consumption figures, logout.
        :return: None
        """
        print("__CUSTOMER MENU__\n\n"
              "(1) Show profile\n"
              "(2) Update profile\n"
              "(3) Show products ('3 keyword' or '3')\n"
              "(4) Show history orders\n"
              "(5) Generate all consumption figures\n"
              "(6) Logout\n")

    @staticmethod
    def update_details():
        """ method to display msg to update user details"""
        print("Input number/s between 1 - 4, separated by space/s\n"
              "of the detail/s you'd like to update. Or leave input\n"
              "blank to update all details.\n"
              "\t\t1) username\n"
              "\t\t2) password\n"
              "\t\t3) email address\n"
              "\t\t4) mobile number\n")

    @staticmethod
    def register_requirement():
        """ method displays requirements for user registration"""
        print("Registration requires:\n"
              "\t\t• username\n"
              "\t\t• password\n"
              "\t\t• email address\n"
              "\t\t• mobile number\n")

    @staticmethod
    def register_username():
        """ method displays requirement to pass username validation """
        print("USERNAME: should only contain letters or underscores. Length should be at least 5 characters.")

    @staticmethod
    def register_password():
        """ method displays requirement to pass password validation """
        print("PASSWORD: should contain at least 1 letter & 1 number. Length should be at least 5 characters.")

    @staticmethod
    def register_email():
        """ method displays requirement to pass email address validation """
        print("EMAIL: must contain username, @ symbol, domain name, & dot.")

    @staticmethod
    def register_mobile():
        """ method displays requirement to pass email mobile validation """
        print("MOBILE: must be exactly 10 digits, only numbers & starting with either 04 or 03.")

    @staticmethod
    def go_to_menu():
        """ method that displays command option for user to go back"""
        print("__type 'menu' to quit & return to previous menu. NOTE: changes won't be saved__\n")

    @staticmethod
    def print_going_back():
        """ method that displays msg that user is going back to main menu"""
        print("\nGoing back...")

    @staticmethod
    def text_box(string):
        string_to_list = string.split(", ")
        string = "".join(
            [line + "\n" if i < len(string_to_list) - 1 else line for i, line in enumerate(string_to_list)])
        vertical, horizontal = "|", "-"
        max_len = local_len = 0
        temp_string = ""
        lines_list = []
        for i in range(len(string)):
            temp_string += string[i]
            if string[i] != "\n":
                local_len += 1
            else:
                lines_list.append(vertical + " " + temp_string)
                temp_string = ""
                max_len = max(max_len, local_len)
                local_len = 0

        for i in range(len(lines_list)):
            lines_list[i] = lines_list[i][:-1] + (" " * (max_len - len(lines_list[i]) + 4)) + "|" + "\n"

        top = "+" + ("-" * (max_len + 2)) + "+\n"
        base = "+" + ("-" * (max_len + 2)) + "+"
        print(top + "".join(lines_list) + base)

    @staticmethod
    def show_list(user_role=None, list_type=None, object_list=None):
        """
        method prints diff. types of list, i.e. customer, product, or order.
        :param user_role: accepts user_role str
        :param list_type: accepts list_type str
        :param object_list: accepts list of objects
        """
        print("\n")
        def string_to_list(string):
            result = []
            current = ""
            flag = False

            for char in string:
                if char == '"':
                    flag = not flag
                elif char == "," and not flag:
                    result.append(current.strip())
                    current = ""
                else:
                    current += char

            result.append(current.strip())

            string = "\n".join(result) + "\n"
            print(string)

        if list_type:
            for line in list_type:
                string_to_list(line)
        # print(user_role if True else ("\n".join(list_type) if True else object_list))


    @staticmethod
    def print_error_message(error_source, error_message):
        """
        method prints err msg & shows where err occurred.
        :param error_source: accepts error_source str
        :param error_message: accepts error_message str
        :return: None
        """
        print(error_message, f"\t # ERROR_SOURCE -> {error_source}\n")

    @staticmethod
    def print_message(message):
        """
        method which prints out given msg.
        :param message: accepts message as str
        :return: None
        """
        print(message)

    @staticmethod
    def print_object(target_object):
        """
        method which prints out the obj using str()
        :param target_object: accepts obj
        :return: None
        """
        print(target_object.__str__())