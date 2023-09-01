# Note: All the customers are saved in the file “data/users.txt”
from model_user import User


class Customer(User):

    def __init__(self,
                 user_id="u_0000000000",
                 user_name="empty_name",
                 user_password="empty_password",
                 user_register_time="00-00-0000_00:00:00",
                 user_role="customer",
                 user_email="empty@email.com",
                 user_mobile="0400-000-000"
                 ):

        super().__init__(user_id, user_name, user_password, user_register_time, user_role)
        self.user_email = user_email
        self.user_mobile = user_mobile

    def __str__(self):
        return (f"user_id: {self.user_id}\n"
                f"user_name: {self.user_name}\n"
                f"user_password: {self.user_password}\n"
                f"user_register_time: {self.user_register_time}\n"
                f"user_role: {self.user_role}\n"
                f"user_email: {self.user_email}\n"
                f"user_mobile: {self.user_mobile}\n")
