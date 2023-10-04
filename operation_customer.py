import re
import time
import os

from model_admin import Admin
from model_customer import Customer
from operation_user import UserOperation


class CustomerOperation:
    len_users_txt = 1  # will always be at least 1 because admin is always there
    pages_amount = 1

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
    def register_customer(user_name, user_password, user_email, user_mobile, r_time=None):
        """
        Method to save the info. of the new customer into the data/users.txt file
        :param user_name: user provided name str
        :param user_password: user provided p/w str
        :param user_email: user provided email str
        :param user_mobile: user provided mobile int
        :param r_time: generates random timestamp
        :return: returns bool depending on validation to ensure all input values are valid
        """
        try:
            with open("data/users.txt", "a", encoding='utf-8') as file:
                user_id = UserOperation.generate_unique_user_id()
                if user_id == "-1":
                    return None

                user_time = time.strftime("%d-%m-%Y_%H:%M:%S") if not r_time else r_time
                encrypted_pw = UserOperation.encrypt_password(user_password)
                file.write(Customer(
                    user_id, user_name, encrypted_pw, user_time,
                    user_email=user_email, user_mobile=user_mobile).__str__() + "\n")
            CustomerOperation.len_users_txt += 1
            CustomerOperation.pages_amount = CustomerOperation.len_users_txt // 10 + 1

        except FileNotFoundError or OSError:
            return None

        return user_id

    @staticmethod
    def update_profile(update_data, customer):
        """
        Method to update the given customer object’s attribute value
        :param update_data: accepts dict. of attribute_name/value
        :param customer: accepts customer object
        :return: returns updated customer_object
        """

        try:
            with open("data/users.txt", "r", encoding='utf-8') as file:  # open file to read
                file_list = list(file)
            for i, line in enumerate(file_list):
                if line and line.split(", ")[1][11:] == customer.user_name:
                    line_split = line.split(", ")

                    if "username" in update_data:
                        line_split[1] = "user_name: " + update_data["username"]
                        customer.user_name = update_data["username"]
                    if "password" in update_data:
                        encrypted_pw = UserOperation.encrypt_password(update_data["password"])
                        line_split[2] = "user_password: " + encrypted_pw
                        customer.user_password = update_data["password"]
                    if "email address" in update_data:
                        line_split[5] = "user_email: " + update_data["email address"]
                        customer.user_email = update_data["email address"]
                    if "mobile number" in update_data:
                        line_split[6] = "user_mobile: " + update_data["mobile number"] + "\n"
                        customer.user_mobile = update_data["mobile number"]
                    line = ", ".join(line_split)
                    file_list[i] = line
                    break

            write_string = "".join(file_list)

            with open("data/users.txt", "w", encoding='utf-8') as file:  # Open file to write
                file.write(write_string)

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
        try:
            if os.path.getsize("data/users.txt") == 0:
                return False
            with open("data/users.txt", "r", encoding='utf-8') as file:
                file_list = list(file)
                found_customer = False

            for i, line in enumerate(file_list):
                if line and line[9:21] == customer_id:
                    found_customer = True
                    del file_list[i]
                    break

            write_string = "".join(file_list)

            if found_customer:
                with open("data/users.txt", "w", encoding='utf-8') as file:  # Open file to write
                    file.write(write_string)
                CustomerOperation.len_users_txt -= 1
                CustomerOperation.pages_amount = CustomerOperation.len_users_txt // 10 + 1


        except FileNotFoundError or OSError:
            return False
        return found_customer

    @staticmethod
    def get_customer_list(page_number):
        """
        method to retrieve 1 page of customers from data/users.txt
        :param page_number: accepts page_number int
        :return: returns tuple, e.g. ([Customer1,Customer2,...,Customer10], page_no, total_page)
        """
        try:
            with open("data/users.txt", "r", encoding="utf-8") as file:

                if page_number < 1:
                    return None
                file = list(file)
                start, stop = (page_number * 10) - 10, page_number * 10
                product_list = []
                for i in range(len(file)):
                    if start <= i < stop:
                        product_list.append(file[i])
                    elif i == stop:
                        break

        except FileNotFoundError or OSError:
            return None

        return product_list, page_number, CustomerOperation.pages_amount


    @staticmethod
    def delete_all_customers():
        """
        Method to remove all customers from the data/users.txt file
        :return: returns bool based on success
        """
        try:
            with open("data/users.txt", "w", encoding="utf-8") as file:
                file.truncate(0)
                encrypted_pw = UserOperation.encrypt_password(Admin.__init__.__defaults__[2])
                file.write(Admin(user_password=encrypted_pw).__str__() + "\n")
                CustomerOperation.len_users_txt = 1
                CustomerOperation.pages_amount = 1
        except FileNotFoundError or OSError:
            return False
        return True


