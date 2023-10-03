import time
import random as r
from operation_customer import CustomerOperation


class OrderOperation:

    @staticmethod
    def generate_unique_order_id():
        """
        method used to generate & return 5 digit unique order ID
        starting with 'o_' when a new order is created.
        :return: returns str result, e.g. 'o_12345'
        """
        pass

    @staticmethod
    def create_an_order(customer_id, product_id, create_time):
        """
        When new order, a unique ID is generated, w/ curr time.
        The order data is saved into the data/orders.txt file.
        :param customer_id: accepts customer_id str
        :param product_id:  accepts product_id str
        :param create_time: accepts curr time from time module
        :return: returns bool based on success
        """
        pass

    @staticmethod
    def delete_order(order_id):
        """
        method deletes order info from data/orders.txt
        file based on the provided order_id
        :param order_id: accepts order_id str
        :return: returns bool based on success
        """
        pass

    @staticmethod
    def get_order_list(customer_id, page_number):
        """
        method retrieves 1 pg of orders from dBase which belongs
        to the given customer. 1 page contains a max of 10 items.
        :param customer_id: accepts customer_id str
        :param page_number: accepts page_number int
        :return: returns tuple inc. list of order objects & total no. of pages.
                 e.g. ([Order(),Order(),Order()...],page_number,total_page).
        """
        pass


    # create 10 customers and randomly generate 50
    # to 200 orders for each customer. Try to control the order time for
    # each order and let the time be scattered into different 12 months of
    # the year. The product of each order is obtained randomly from the
    # database. Use some functions defined in previous tasks.

    @staticmethod
    def generate_test_order_data():
        """
        method to automatically generate test data
        :return: None
        """
        name = ["chris_m", "jack_p", "bob_l", "jazz_f", "andrea_v", "hans_j", "sam_j", "mike_l", "luke_s", "patches_a"]
        pw = ["Apple1", "Badger5", "toiLet2", "Bucky8", "Cherry6", "Elf45", "Meat6", "Badger1", "Yucky1", "Glue9"]
        email = ["chris_m@gmail.com", "jack_p@gmail.com", "bob_l@gmail.com", "jazz_f@gmail.com", "andrea_v@gmail.com",
                 "hans_j@gmail.com", "sam_j@gmail.com", "mike_l@gmail.com", "luke_s@gmail.com", "patches_a@gmail.com"]
        mobile = ["0412341234", "0423452345", "0434563456", "0445674567", "0456785678",
                  "0467896789", "0478907890", "0312341234", "0323452345", "0334563456"]
        r_time_array = []
        OrderOperation.generate_random_time(r_time_array, 10000000,
                                            "01-01-2020_00:00:00", 10)
        users = {"name": name, "pw": pw, "email": email, "mobile": mobile, "r_time": r_time_array}

        for i in range(10):
            CustomerOperation.register_customer(users["name"][i], users["pw"][i],
                                                users["email"][i], users["mobile"][i], users["r_time"][i])

    @staticmethod
    def generate_random_time(time_array, max_advance, start_time, amount):
        timestamp = time.strptime(start_time, "%d-%m-%Y_%H:%M:%S")
        for _ in range(amount):
            seconds = r.randint(1000, max_advance)
            timestamp = time.mktime(timestamp)
            timestamp = time.localtime(timestamp + seconds)
            timestamp = time.struct_time(timestamp)
            time_array.append(time.strftime("%d-%m-%Y_%H:%M:%S", timestamp))
        return time_array


    @staticmethod
    def generate_single_customer_consumption_figure(customer_id):
        """
        method to generate a chart to show sum of order price & 12 diff. months
        for given customer
        :param customer_id: accepts customer_id str
        :return: None
        """
        pass

    @staticmethod
    def generate_all_customers_consumption_figure():
        """
        method to generate a chart to show sum of order price & 12 diff. months
        for all customers
        :return: None
        """
        pass

    @staticmethod
    def generate_all_top_10_best_sellers_figure():
        """
        method to generate a graph to show the top 10 best-selling products
        and sort the result in descending order.
        :return: None
        """
        pass

    @staticmethod
    def delete_all_orders():
        """
        method removes all the data in the data/orders.txt file
        :return: None
        """
        pass


OrderOperation.generate_test_order_data()