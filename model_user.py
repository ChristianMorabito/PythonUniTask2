# Note: All the users are saved in the file "data/users.txt"

class User:

    def __init__(self,
                 user_id="u_0000000000",
                 user_name="empty_name",
                 user_password="empty_password",
                 user_register_time="00-00-0000_00:00:00",
                 user_role="customer"):

        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_register_time = user_register_time
        self.user_role = user_role

    def __str__(self):  # TODO: complete __str__ method
        return f""