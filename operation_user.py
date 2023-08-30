class UserOperation:

    def generate_unique_user_id(self):
        """
        Method to generate & return a 10-digit unique userId
        starting with ‘u_’ when new user is registered.
        :return: returns str value in the format 'u_10digits'
        """
        pass

    def encrypt_password(self, user_password):
        """
        Method to encode a user-provided p/w
        :param user_password: user provided p/w str
        :return: returns encrypted p/w str
        """
        pass

    def check_username_exist(self, user_name):
        """
        Method to verify if user exists in the system.
        :param user_name: user provided user_name str
        :return: returns bool to determine if provided user_name exists
        """
        pass

    def validate_username(self, user_name):
        """
        Method to validate user_name, to only contain
        letters & underscores, w/ len >= 5 chars.
        :param user_name: user provided user_name str
        :return: returns bool to determine if provided user_name is valid
        """
        pass

    def validate_password(self, user_password):
        """
        Validate the user p/w, which should contain:
        x1 (upper/lowercase), & x1 no; p/w len must be >= 5 char
        :param user_password: user provided p/w str
        :return: returns bool to determine if provided p/w is valid
        """
        pass

    def login(self, user_name, user_password):
        """
        Method to verify user_name & p/w
        to determine the authorization status for sys access.
        :param user_name: user provided user_name str
        :param user_password: user provided p/w str
        :return: returns Customer or Admin object
        """
        pass









