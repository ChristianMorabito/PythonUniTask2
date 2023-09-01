import re
import time
from model_customer import Customer
from operation_user import UserOperation


class CustomerOperation:


    @staticmethod
    def validate_email(user_email):
        """
        :param user_email: user provided email str
        :return: returns bool depending on validation
        """
        user_email = user_email.strip()
        if len(user_email) < 4:  # shortest email can only be: a@b.
            return False
        i = 0
        check_name = ""
        while i < len(user_email) and user_email[i] != "@":
            if i == 0 and not user_email[i].isalpha():  # checks if first letter in email address is an alphabet char.
                return False
            check_name += user_email[i]
            i += 1

        if not re.match(r'^[a-zA-Z0-9_.]+$', check_name) or i < len(user_email) and user_email[i] != "@":
            return False

        i += 1
        if i == len(user_email):
            return False

        check_domain = ""
        while i < len(user_email) and user_email[i] != ".":
            if user_email[i-1] == "@" and not user_email[i].isalpha():
                return False
            check_domain += user_email[i]
            i += 1

        if not re.match(r'^[a-zA-Z0-9_.]+$', check_domain) or i < len(user_email) and user_email[i] != ".":
            return False

        return True


    @staticmethod
    def validate_mobile(mobile):
        mobile = mobile.strip()
        """
        Method to validate user_mobile
        :param user_mobile: user provided mobile int
        :return: returns bool depending on validation
        """
        return len(mobile) == 10 and re.match(r'^[0-9]+$', mobile) and mobile[:2] == "04" or mobile[:2] == "03"

    @staticmethod
    def register_customer(user_name, user_password, user_email, user_mobile):
        """
        Method to save the info. of the new customer into the data/users.txt file
        :param user_name: user provided name str
        :param user_password: user provided p/w str
        :param user_email: user provided email str
        :param user_mobile: user provided mobile int
        :return: returns bool depending on validation to ensure all input values are valid
        """
        try:  #TODO: FIX GENERATE USER_ID_NUMBER
            with open("data/users.txt", "a") as file:
                user_id = UserOperation.generate_unique_user_id()
                user_time = time.strftime("%d-%m-%Y_%H:%M:%S")
                file.write(Customer(
                    user_id, user_name, user_password, user_time,
                    user_email=user_email, user_mobile=user_mobile).__str__())
                file.write("\n")
        except FileNotFoundError:
            return False

        return True





    @staticmethod
    def update_profile(attribute_name, value, customer_object):
        """
        Method to update the given customer object’s attribute value
        :param attribute_name: accepts str for attribute name
        :param value: accepts str for attribute value
        :param customer_object: accepts customer object
        :return: returns bool depending on validation
                 to ensure input value is valid
        """
        pass

    @staticmethod
    def delete_customer(customer_id):
        """
        method to delete the customer from data/users.txt file based on the
        provided customer_id
        :param customer_id: accepts customer_id str
        :return: returns bool depending on success
        """
        pass

    @staticmethod
    def get_customer_list(page_number):
        """
        method to retrieve 1 page of customers from data/users.txt
        :param page_number: accepts page_number int
        :return: returns tuple, e.g. ([Customer1,Customer2,...,Customer10], page_no, total_page)
        """
        pass

    @staticmethod
    def delete_all_customers():
        """
        Method to remove all customers from the data/users.txt file
        :return: None
        """
        pass
