import os
import re
import random as r


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

        try:
            with open("data/users.txt", "r") as file:

                last_id = ""

                for line in list(file):
                    if line[:7] == "user_id":
                        last_id = line[11:-1]  # if test == 'user_id: u_0000000000\n', then last_id == '0000000000'
                user_id = "u_" + str(int(last_id) + 1).zfill(len(last_id))
                # reference: https://stackoverflow.com/questions/587647/how-to-increment-a-value-with-leading-zeroes

        except FileNotFoundError or OSError:
            user_id = "-1"

        return user_id

    @staticmethod
    def encrypt_password(user_pw):
        """
        Method to encode a user-provided p/w
        :param user_pw: user provided p/w str
        :return: returns encrypted p/w str
        """
        char_list = ([chr(i) for i in range(48, 58)] +  # ['0', '1', ..., '9']
                     [chr(i) for i in range(65, 91)] +  # ['A', 'B', ..., 'Z']
                     [chr(i) for i in range(97, 123)])  # ['a', 'b', ..., 'z']

        encrypted_pw = "".join([r.choice(char_list) + r.choice(char_list) + user_pw[i]
                                for i in range(len(user_pw))])
        return "^^" + encrypted_pw + "$$"

    @staticmethod
    def decrypt_password(encrypted_pw):
        """
        Method to decode the encrypted password.
        :param encrypted_pw: accepts encrypted password string
        :return: returns string of decrypted password
        """
        sliced_pw = encrypted_pw[4:-2]
        return "".join([sliced_pw[i] for i in range(len(sliced_pw)) if i % 3 == 0])

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
            if has_letter and has_int:
                break
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









