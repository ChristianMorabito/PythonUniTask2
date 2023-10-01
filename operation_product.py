import os
import pandas as pd
from model_product import Product
class ProductOperation:

    @staticmethod
    def extract_products_from_files():
        """
        Method to extract product info from the given
        product data files
        :return: None
        """

        try:
            files = os.listdir("product")
            for file_name in files:
                df = pd.read_csv(file_name)
                # TODO: FIX
                product = [Product(row['name'], row['age'], row['city']) for _, row in df.iterrows()]


        except FileNotFoundError or OSError:
            return False
        return True

    @staticmethod
    def get_product_list(page_number):
        """
        method which retrieves one page of
        products from the database
        :param page_number: accepts page no. int
        :return: returns tuple e.g.
        ([Product1,Product2,Product3,...Product10],page_no, total_page)
        """
        pass

    @staticmethod
    def delete_product(product_id):
        """
        method to delete the product info from system, i.e. data/products.txt
        based on provided product_id
        :param product_id: accepts product_id str
        :return: returns bool based on success
        """
        pass

    @staticmethod
    def get_product_list_by_keyword(keyword):
        """
        method to retrieve all products whose name
        contains the keyword (case sensitive)
        :param keyword: accepts keyword as str
        :return: returns list of products
        """
        pass

    @staticmethod
    def get_product_by_id(product_id):
        """
        method returns 1 product object based on the given ID
        :param product_id: accepts product_id as str
        :return: returns product object or None if cannot be found
        """
        pass

    @staticmethod
    def generate_category_figure():
        """
        method generates a bar chart that shows the total no.
        of products for each category in descending order.
        The figure is saved into the data/figure folder
        :return: None
        """
        pass

    @staticmethod
    def generate_discount_figure():
        """
         method generates pie chart that shows the proportion of
         products that have a discount value < 30, 30 >= 60, & > 60.
         Chart is saved into the data/figure folder.
        :return: None
        """
        pass

    @staticmethod
    def generate_likes_count_figure():
        """
        method generates chart displaying the sum of products’ likes_count
        for each category (ascending). Chart is saved into the data/figure folder
        :return: None
        """
        pass

    @staticmethod
    def generate_dislikes_count_figure():
        """
        method generates scatter chart showing relationship
        between likes_count/discount for all products.
        Chart is saved into the data/figure folder
        :return: None
        """
        pass

    @staticmethod
    def delete_all_products():
        """
        method removes all the product data in the data/products.txt file
        :return: None
        """
        pass


