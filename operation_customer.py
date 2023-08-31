class CustomerOperation:

    @staticmethod
    def validate_email(user_email):
        """
        Method to validate user_email
        :param user_email: user provided email str
        :return: returns bool depending on validation
        """
        pass

    @staticmethod
    def validate_mobile(user_mobile):
        """
        Method to validate user_mobile
        :param user_mobile: user provided mobile int
        :return: returns bool depending on validation
        """
        pass

    @staticmethod
    def register_customer(user_name, user_password, user_email, user_mobile):
        """
        Method to save the info. of the new customer into the
        data/users.txt file
        :param user_name: user provided name str
        :param user_password: user provided p/w str
        :param user_email: user provided email str
        :param user_mobile: user provided mobile int
        :return: returns bool depending on validation
                 to ensure all input values are valid
        """
        print(user_name, user_password, user_email, user_mobile)

    @staticmethod
    def update_profile(attribute_name, value, customer_object):
        """
        Method to update the given customer object’s attribute value
        :param attribute_name: accepts str for attribute name
        :param value: accepts str for attribute value
        :param customer_object: accepts customer object
        :return: returns bool depending on validation
                 to ensure input value is valid
        """
        pass

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
