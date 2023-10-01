import re
import time

import operation_user
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
        try:
            with open("data/users.txt", "a") as file:
                user_id = UserOperation.generate_unique_user_id()
                if user_id == "-1":
                    return False

                user_time = time.strftime("%d-%m-%Y_%H:%M:%S")
                encrypted_pw = UserOperation.encrypt_password(user_password)
                file.write(Customer(
                    user_id, user_name, encrypted_pw, user_time,
                    user_email=user_email, user_mobile=user_mobile).__str__())
                file.write("\n")

        except FileNotFoundError or OSError:
            return False

        return True

    @staticmethod
    def update_profile(update_data, customer):
        """
        Method to update the given customer object’s attribute value
        :param update_data: accepts dict. of attribute_name/value
        :param customer: accepts customer object
        :return: returns updated customer_object
        """
        try:
            # TODO: send file_list to overwrite the old users.txt file
            with open("data/users.txt", "r") as file:
                flist = [" ".join(line.split()) for line in file]

                for i, line in enumerate(flist):
                    if line and line[:9] == "user_name" and line[:11] == customer.user_name:
                        if "username" in update_data:
                            flist[i] = "user_name: " + update_data["username"]
                            customer.user_name = update_data["username"]
                        if "password" in update_data:
                            encrypted_pw = UserOperation.encrypt_password(update_data["password"])
                            flist[i+1] = encrypted_pw
                            customer.user_password = "user_password: " + update_data["password"]
                        if "email address" in update_data:
                            flist[i+4] = "user_email" + update_data["email address"]
                            customer.user_email = update_data["email address"]
                        if "mobile number" in update_data:
                            flist[i+5] = "user_mobile: " + update_data["mobile number"]
                            customer.user_mobile = update_data["mobile number"]
                        break

                write_string = "\n".join(flist)
                print(write_string)

        except FileNotFoundError or OSError:
            return None
        return customer



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
