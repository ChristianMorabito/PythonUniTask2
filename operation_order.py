import time
import random as r
import os
from model_order import Order
from operation_customer import CustomerOperation
from operation_product import ProductOperation
from operation_user import UserOperation


class OrderOperation:
    len_order_txt = 0
    pages_amount = 1

    @staticmethod
    def generate_unique_order_id():
        """
        method used to generate & return 5 digit unique order ID
        starting with 'o_' when a new order is created.
        :return: returns str result, e.g. 'o_12345'
        """
        try:
            if os.path.getsize("data/orders.txt") == 0:
                return "o_00000"

            with open("data/orders.txt", "r", encoding='utf-8') as file:

                last_id = ""

                for line in file:

                    if line[:8] == "order_id":
                        last_id = line[12:17]
                order_id = "o_" + str(int(last_id) + 1).zfill(len(last_id))
                # reference: https://stackoverflow.com/questions/587647/how-to-increment-a-value-with-leading-zeroes

        except FileNotFoundError or OSError:
            order_id = "-1"

        return order_id

    @staticmethod
    def create_an_order(customer_id, product_id, create_time=None):
        """
        method to create an order
        :param customer_id: accepts customer_id str
        :param product_id:  accepts product_id str
        :param create_time: accepts curr time from time module
        :return: returns bool based on success
        """

        try:
            with open("data/orders.txt", "a", encoding='utf-8') as file:
                order_id = OrderOperation.generate_unique_order_id()
                if order_id == "-1":
                    return False

                create_time = time.strftime("%d-%m-%Y_%H:%M:%S") if not create_time else create_time
                file.write(Order(order_id, customer_id, product_id, create_time).__str__() + "\n")
                OrderOperation.len_order_txt += 1
                OrderOperation.pages_amount = OrderOperation.len_order_txt // 10 + 1

        except FileNotFoundError or OSError:
            return False

        return True

    @staticmethod
    def delete_order(order_id):
        """
        method deletes order info from data/orders.txt
        file based on the provided order_id
        :param order_id: accepts order_id str
        :return: returns bool based on success
        """
        OrderOperation.len_order_txt -= 1
        OrderOperation.pages_amount = OrderOperation.len_order_txt // 10 + 1

    @staticmethod
    def get_order_list(page_number=None, customer_id=None):
        """
        method retrieves 1 pg of orders from dBase which belongs
        to the given customer. 1 page contains a max of 10 items.
        :param customer_id: accepts customer_id str
        :param page_number: accepts page_number int
        :return: returns tuple inc. list of order objects & total no. of pages.
                 e.g. ([Order(),Order(),Order()...],page_number,total_page).
        """
        try:
            with open("data/orders.txt", "r", encoding="utf-8") as file:

                if page_number < 1:
                    return None
                file = list(file)
                start, stop = (page_number * 10) - 10, page_number * 10
                order_list = []
                for i in range(len(file)):
                    if start <= i < stop:
                        order_list.append(file[i])
                    elif i == stop:
                        break

        except FileNotFoundError or OSError:
            return None

        return order_list, page_number, OrderOperation.pages_amount

    @staticmethod
    def generate_test_order_data():
        """
        method to automatically generate test data
        :return: returns bool based on success
        """
        if ProductOperation.len_products_txt < 2:  # TODO: LOOK AT THIS. WHY 2?
            ProductOperation.extract_products_from_files()
        name = ["chris_m", "jack_p", "bob_l", "jazz_f", "andrea_v", "hans_j", "sam_j", "mike_l", "luke_s", "patches_a"]
        if UserOperation.check_username_exist(name[0]):
            return 0
        pw = ["Apple1", "Badger5", "toiLet2", "Bucky8", "Cherry6", "Elf45", "Meat6", "Badger1", "Yucky1", "Glue9"]
        email = ["chris_m@gmail.com", "jack_p@gmail.com", "bob_l@gmail.com", "jazz_f@gmail.com", "andrea_v@gmail.com",
                 "hans_j@gmail.com", "sam_j@gmail.com", "mike_l@gmail.com", "luke_s@gmail.com", "patches_a@gmail.com"]
        mobile = ["0412341234", "0423452345", "0434563456", "0445674567", "0456785678",
                  "0467896789", "0478907890", "0312341234", "0323452345", "0334563456"]
        r_time_array, advance_seconds = [], 10000000
        OrderOperation.generate_random_time(r_time_array, advance_seconds,
                                            "01-01-2020_00:00:00", 10, True)
        users = {"name": name, "pw": pw, "email": email, "mobile": mobile, "r_time": r_time_array}

        # generate 10 customers
        user_id_list = [CustomerOperation.register_customer(
            users["name"][i], users["pw"][i], users["email"][i],
            users["mobile"][i], users["r_time"][i]) for i in range(len(name))]

        if not user_id_list or None in user_id_list:
            return False

        return OrderOperation.generate_test_purchases(name)

    @staticmethod
    def generate_test_purchases(name_list):
        """
        method to generate test purchase orders
        :param name_list: accepts list of names
        :return: returns bool based on success
        """
        r_order_amount = [r.randint(50, 200) for _ in range(len(name_list))]
        total_order_amount = sum(r_order_amount)
        seconds_in_a_year = 31536000
        advance = seconds_in_a_year // total_order_amount
        timestamps, product_indexes = [], []

        OrderOperation.generate_random_product_list(total_order_amount, product_indexes)
        OrderOperation.generate_random_time(timestamps, advance,
                                            "01-01-2022_00:00:00", total_order_amount)

        user_order_dict = {name_list[i]: r_order_amount[i] for i in range(len(name_list))}
        to_delete = set()
        for i in range(total_order_amount):
            if len(to_delete) > 0:
                user_order_dict = {name_list[j]: r_order_amount[j]
                                   for j in range(len(name_list)) if name_list[j] not in to_delete}
                to_delete.clear()
            if not OrderOperation.create_an_order(name_list[i % len(name_list)], product_indexes[i], timestamps[i]):
                return False
            user_order_dict[name_list[i % len(name_list)]] -= 1
            if user_order_dict[name_list[i % len(name_list)]] == 0:
                to_delete.add(name_list[i % len(name_list)])
                del name_list[i % len(name_list)]
        return True


    @staticmethod
    def generate_random_product_list(amount, product_index_list):
        try:
            with open("data/products.txt", "r", encoding="utf-8") as file:
                random_indexes = [r.randint(0, ProductOperation.len_products_txt-2) for _ in range(amount)]
                file_list = list(file)
                for index in random_indexes:
                    product_index_list.append(file_list[index].split(", ")[0][8:])

        except FileNotFoundError or IndexError or OSError:
            return None

        return product_index_list
    @staticmethod
    def generate_random_time(time_array, max_advance, start_time, amount, random_increment=None):
        """
        Method to advance a given timestamp at either random or static increments
        :param time_array: accepts an array to have the timestamps appended to
        :param max_advance: accepts int (seconds) that reps. the max amount the time can advance
        :param start_time: accepts an int, representing the given starting time
        :param amount: accepts int of the amount of timestamps to return
        :param random_increment:
        :return: returns the given amount of timestamps in an array
        """
        timestamp = time.strptime(start_time, "%d-%m-%Y_%H:%M:%S")
        for _ in range(amount):
            seconds = r.randint(1000, max_advance) if random_increment else max_advance
            timestamp = time.mktime(timestamp)
            timestamp = time.localtime(timestamp + seconds)
            timestamp = time.struct_time(timestamp)
            time_array.append(time.strftime("%d-%m-%Y_%H:%M:%S", timestamp))
            # reference: https://docs.python.org/3/library/time.html
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
        :return: returns bool depending on success
        """
        try:
            with open("data/orders.txt", "w", encoding="utf-8") as file:
                file.truncate(0)
                OrderOperation.len_order_txt = 0
                OrderOperation.pages_amount = 1
        except FileNotFoundError or OSError:
            return False
        return True
