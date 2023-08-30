import time


class OrderOperation:

    def generate_unique_order_id(self):
        """
        method used to generate & return 5 digit unique order ID
        starting with 'o_' when a new order is created.
        :return: returns str result, e.g. 'o_12345'
        """
        pass

    def create_an_order(self, customer_id, product_id, create_time=time.time()):
        """
        When new order, a unique ID is generated, w/ curr time.
        The order data is saved into the data/orders.txt file.
        :param customer_id: accepts customer_id str
        :param product_id:  accepts product_id str
        :param create_time: curr time as default value is generated
        :return: returns bool based on success
        """
        pass

    def delete_order(self, order_id):
        """
        method deletes order info from data/orders.txt
        file based on the provided order_id
        :param order_id: accepts order_id str
        :return: returns bool based on success
        """
        pass

    def get_order_list(self, customer_id, page_number):
        """
        method retrieves 1 pg of orders from dBase which belongs
        to the given customer. 1 page contains a max of 10 items.
        :param customer_id: accepts customer_id str
        :param page_number: accepts page_number int
        :return: returns tuple inc. list of order objects & total no. of pages.
                 e.g. ([Order(),Order(),Order()...],page_number,total_page).
        """
        pass

    def generate_test_order_data(self):
        """
        method to automatically generate test data
        :return: None
        """
        pass

    def generate_single_customer_consumption_figure(self, customer_id):
        """
        method to generate a chart to show sum of order price & 12 diff. months
        for given customer
        :param customer_id: accepts customer_id str
        :return: None
        """
        pass

    def generate_all_customers_consumption_figure(self):
        """
        method to generate a chart to show sum of order price & 12 diff. months
        for all customers
        :return: None
        """
        pass

    def generate_all_top_10_best_sellers_figure(self):
        """
        method to generate a graph to show the top 10 best-selling products
        and sort the result in descending order.
        :return: None
        """
        pass

    def delete_all_orders(self):
        """
        method removes all the data in the data/orders.txt file
        :return: None
        """
        pass
