import os
import re


class UserOperation:

    @staticmethod
    def generate_unique_user_id():
        """
        Method to generate & return a 10-digit unique userId
        starting with ‘u_’ when new user is registered.
        :return: returns str value in the format 'u_10digits'
        """
        if os.path.getsize("data/users.txt") == 0:
            return "u_0000000000"

        # try:
        #     with open("data/users.txt", "r") as file:
        #
        #         for line in list(file)
        #
        #
        # except FileNotFoundError or OSError:
        #     return "-1"
        # return "test"


    @staticmethod
    def encrypt_password(user_password):
        """
        Method to encode a user-provided p/w
        :param user_password: user provided p/w str
        :return: returns encrypted p/w str
        """
        pass

    @staticmethod
    def check_username_exist(user_name):
        """
        Method to verify if user exists in the system.
        :param user_name: user provided user_name str
        :return: returns bool to determine if provided user_name exists
        """
        pass

    @staticmethod
    def validate_username(user_name):
        """
        Method to validate user_name, to only contain
        letters & underscores, w/ len >= 5 chars.
        :param user_name: user provided user_name str
        :return: returns bool to determine if provided user_name is valid
        """
        return re.match(r'^[a-zA-Z_]+$', user_name) and len(user_name) >= 5

    @staticmethod
    def validate_password(user_password):
        """
        Validate the user p/w, which should contain:
        x1 (upper/lowercase), & x1 no; p/w len must be >= 5 char
        :param user_password: user provided p/w str
        :return: returns bool to determine if provided p/w is valid
        """
        if len(user_password) < 5:
            return False
        has_letter = has_int = False
        for char in user_password:
            if not has_letter:
                has_letter = True if char.isalpha() else False
            if not has_int:
                has_int = True if char.isdigit() else False
        return has_letter and has_int

    @staticmethod
    def login(user_name, user_password):
        """
        Method to verify user_name & p/w
        to determine the authorization status for sys access.
        :param user_name: user provided user_name str
        :param user_password: user provided p/w str
        :return: returns Customer or Admin object
        """
        pass









