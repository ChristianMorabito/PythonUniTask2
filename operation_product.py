import os
from model_product import Product
import pandas as pd
import matplotlib.pyplot as plt

from operation_user import UserOperation


class ProductOperation:
    len_products_txt = 0
    pages_amount = 1

    @staticmethod
    def extract_products_from_files():
        """ Method to extract product info from the given product data file """
        try:
            # if products.txt already written, then just set the len_products_txt & pages_amount numbers
            # without bothering to write products.txt again
            if os.path.getsize("data/products.txt") > 0:
                return ProductOperation.set_len_and_pages()
            data_set = set()
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
    def set_len_and_pages():
        """ method to set the len_products_txt & pages_amount without writing to the products.txt file """
        try:
            with open("data/products.txt", "r", encoding='utf-8') as file:
                ProductOperation.len_products_txt = len(list(file))
                ProductOperation.set_pages_amount()
        except FileNotFoundError or OSError or IndexError:
            return False
        return True

    @staticmethod
    def set_pages_amount():
        """ Method to establish the amount of pages in a file, i.e. 1 page = 10 lines of txt """
        ProductOperation.pages_amount = ProductOperation.len_products_txt // 10 + 1

    @staticmethod
    def get_product_list(page_number):
        """
        method which retrieves one page of products from the database
        :param page_number: accepts page no. int
        :return: returns tuple e.g. ([Product1,Product2,Product3,...Product10],page_no, total_page)
        """
        try:
            with open("data/products.txt", "r", encoding="utf-8") as file:
                product_list = []
                UserOperation.traverse_pages(product_list, page_number, file)

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
        ProductOperation.set_pages_amount()

    @staticmethod
    def get_product_list_by_keyword(keyword):
        """
        method to retrieve all products whose name
        contains the keyword (case-sensitive)
        :param keyword: accepts keyword as str
        :return: returns list of products
        """
        try:
            with open("data/products.txt", "r", encoding="utf-8") as file:
                keyword_references = []
                file_list = list(file)
                count = 0
                word_dict = {}
                for i, line in enumerate(file_list):
                    left_comma_count = right_comma_count = 0
                    left, right = 0, len(line)-1
                    while left_comma_count < 3:
                        if line[left] == ",":
                            left_comma_count += 1
                        left += 1
                    while right_comma_count < 4:
                        if line[right] == ",":
                            right_comma_count += 1
                        right -= 1
                    count += 1

                    word_list = line[left+11:right].split()
                    for word in word_list:
                        if word.lower() in word_dict:
                            word_dict[word.lower()].append(i)
                        else:
                            word_dict[word.lower()] = [i]

                if keyword in word_dict:
                    for i, num in enumerate(word_dict[keyword]):
                        if i > 0 and word_dict[keyword][i] == word_dict[keyword][i-1]:
                            continue
                        keyword_references.append(file_list[num])

        except FileNotFoundError or OSError:
            return None
        return keyword_references


    @staticmethod
    def get_product_by_id(product_id):
        """
        method returns 1 product object based on the given ID
        :param product_id: accepts product_id as str
        :return: returns product object or None if cannot be found
        """
        try:
            with open("data/products.txt", "r", encoding="utf-8") as file:
                file_list = list(file)
                id_dict = {}
                result_list = []
                for i, line in enumerate(file_list):
                    for j, char in enumerate(line):
                        if char == ",":
                            word = line[8:j]
                            for left in range(len(word) + 1):
                                for right in range(left, len(word)):
                                    if int(word[left:right + 1]) in id_dict:
                                        id_dict[int(word[left:right + 1])].add(i)
                                    else:
                                        id_dict[int(word[left:right + 1])] = set()
                                        id_dict[int(word[left:right + 1])].add(i)
                            break

                if int(product_id) in id_dict:
                    for num in id_dict[int(product_id)]:
                        result_list.append(file_list[num])
                        if len(result_list) == 50:
                            break

        except FileNotFoundError or OSError:
            return None
        return result_list

    @staticmethod
    def generate_category_figure():
        """
        method generates a bar chart that shows the total no.
        of products for each category in descending order.
        The figure is saved into the data/figure folder
        """

        try:
            with open("data/products.txt", "r", encoding="utf-8") as file:
                categories = []
                for line in file:
                    categories.append(line.split(", ")[2][14:])

            series = pd.Series(categories)
            count = series.value_counts()
            count = count.sort_values(ascending=False)

            plt.figure(figsize=(10, 6))
            count.plot(kind='bar')

            plt.ylabel('Count')
            plt.title('Category Figure')
            plt.xticks(fontsize=8, rotation=45)

            figure_path = os.path.join("data/figure", 'category_figure.png')
            plt.savefig(figure_path)
            plt.close()
        except FileNotFoundError or OSError or Exception:
            return False
        return True


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
                ProductOperation.len_products_txt = 0
                ProductOperation.pages_amount = 1
        except FileNotFoundError or OSError:
            return False
        return True

ProductOperation.generate_category_figure()