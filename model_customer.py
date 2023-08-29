from model_user import User


class Customer(User):

    def __init__(self,
                 user_id="u_0000000000",
                 user_name="empty_name",
                 user_password="empty_password",
                 user_register_time="00-00-0000_00:00:00",
                 user_role="customer",
                 user_email="empty@email.com",
                 user_mobile="0400-000-000"):

        super().__init__(user_id, user_name, user_password, user_register_time, user_role)
        self.user_email = user_email
        self.user_mobile = user_mobile

    def __str__(self):  # TODO: complete __str__ method
        return f""