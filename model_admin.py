# Note: All the admins are saved in the file “data/users.txt.
from model_user import User


class Admin(User):
    def __init__(self,
                 user_id="u_0000000000",
                 user_name="admin",
                 user_password="admin1",
                 user_register_time="00-00-0000_00:00:00",
                 user_role="admin"
                 ):

        super().__init__(user_id, user_name, user_password, user_register_time, user_role)

    def __str__(self):
        return (f"user_id: {self.user_id}, "
                f"user_name: {self.user_name}, "
                f"user_password: {self.user_password}, "
                f"user_register_time: {self.user_register_time}, "
                f"user_role: {self.user_role}")


