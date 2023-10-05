import os
from model_product import Product
import pandas as pd


class ProductOperation:
    len_products_txt = 0
    pages_amount = 1

    @staticmethod
    def extract_products_from_files():
        """ Method to extract product info from the given product data file """
        data_set = set()
        try:
            files = os.listdir("product")
            with open("data/products.txt", "w", encoding='utf-8') as w_file:
                for file_name in files:
                    df = pd.read_csv("product/" + file_name)
                    for i, row in df.iterrows():
                        pro_id = row["id"]
                        if pro_id in data_set:  # add product ids into set to skip over duplicates
                            continue
                        data_set.add(pro_id)
                        model = row["model"]
                        category = row["category"]
                        name = row["name"]
                        current_price = row["current_price"]
                        raw_price = row["raw_price"]
                        discount = row["discount"]
                        likes_count = row["likes_count"]
                        w_file.write(Product(pro_id, model, category, name, current_price,
                                             raw_price, discount, likes_count).__str__() + "\n")
                        ProductOperation.len_products_txt += 1  # increment to get the len(products.txt)

                # establish the amount of pages
                ProductOperation.pages_amount = ProductOperation.len_products_txt // 10 + 1

        except FileNotFoundError or OSError:
            return False
        return True

    @staticmethod
    def get_product_list(page_number):
        """
        method which retrieves one page of products from the database
        :param page_number: accepts page no. int
        :return: returns tuple e.g. ([Product1,Product2,Product3,...Product10],page_no, total_page)
        """
        try:
            with open("data/products.txt", "r", encoding="utf-8") as file:
                if page_number < 1:
                    return None
                file = list(file)
                start, stop = (page_number * 10) - 10, page_number * 10
                product_list = []
                for i in range(len(file)):
                    if start <= i < stop:
                        product_list.append(file[i])
                    elif i == stop:
                        break

        except FileNotFoundError or OSError:
            return None

        return product_list, page_number, ProductOperation.pages_amount

    @staticmethod
    def delete_product(product_id):
        """
        method to delete the product info from system, i.e. data/products.txt
        based on provided product_id
        :param product_id: accepts product_id str
        :return: returns bool based on success
        """
        ProductOperation.len_products_txt -= 1
        ProductOperation.pages_amount = ProductOperation.len_products_txt // 10 + 1

    @staticmethod
    def get_product_list_by_keyword(keyword):
        """
        method to retrieve all products whose name
        contains the keyword (case-sensitive)
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
        :return: returns bool based on success
        """
        try:
            with open("data/products.txt", "w", encoding="utf-8") as file:
                file.truncate(0)
                ProductOperation.len_products_txt = 1
                ProductOperation.pages_amount = 1
        except FileNotFoundError or OSError:
            return False
        return True
