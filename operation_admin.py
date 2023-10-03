import time
import os
from model_admin import Admin
from operation_user import UserOperation


class AdminOperation:

    @staticmethod
    def register_admin():
        """Method to write admin account info into the database"""
        try:
            with open("data/users.txt", "r", encoding="utf-8") as r_file:
                if os.path.getsize("data/users.txt") != 0:
                    admin_default_name, file_name = Admin.__init__.__defaults__[1], r_file.read().split(", ")[1][11:]
                    return admin_default_name == file_name
            with open("data/users.txt", "w", encoding="utf-8") as w_file:
                user_time = time.strftime("%d-%m-%Y_%H:%M:%S")
                encrypted_pw = UserOperation.encrypt_password(Admin.__init__.__defaults__[2])
                w_file.write(Admin(user_password=encrypted_pw, user_register_time=user_time).__str__() + "\n")

        except FileNotFoundError or OSError:
            return False

        return True


