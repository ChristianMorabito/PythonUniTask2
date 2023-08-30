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
        pass

    @staticmethod
    def main_menu():
        """
        method displays login menu, i.e. login, register & quit
        :return: None
        """
        print("(1) Login\n"
              "(2) Register\n"
              "(3) Quit")

    @staticmethod
    def admin_menu():
        """
        method displays admin menu, i.e. show products, add customers, show customers,
        show orders, gen. test data, gen. all stat. figures, delete all data, & logout
        :return: None
        """
        pass

    @staticmethod
    def customer_menu():
        """
        method displays customer menu, i.e. show profile, update profile, show products,
        show history orders, gen. all consumption figures, logout.
        :return: None
        """
        pass

    @staticmethod
    def show_list(user_role, list_type, object_list):
        """
        method prints diff. types of list, i.e. customer, product, or order.
        :param user_role: accepts user_role str
        :param list_type: accepts list_type str
        :param object_list: accepts list of objects
        :return: None
        """
        pass

    @staticmethod
    def print_error_message(error_source, error_message):
        """
        method prints err msg & shows where err occurred.
        :param error_source: accepts error_source str
        :param error_message: accepts error_message str
        :return: None
        """
        pass

    @staticmethod
    def print_message(message):
        """
        method which prints out given msg.
        :param message: accepts message as str
        :return: None
        """
        pass

    @staticmethod
    def print_object(target_object):
        """
        method which prints otu the obj using str()
        :param target_object: accepts obj
        :return: None
        """
        pass
