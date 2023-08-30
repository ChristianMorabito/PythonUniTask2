
class ProductOperation:

    def extract_products_from_files(self):
        """
        Method to extract product info from the given
        product data files
        :return: None
        """
        pass

    def get_product_list(self, page_number):
        """
        method which retrieves one page of
        products from the database
        :param page_number: accepts page no. int
        :return: returns tuple e.g.
        ([Product1,Product2,Product3,...Product10],page_no, total_page)
        """
        pass

    def delete_product(self, product_id):
        """
        method to delete the product info from system, i.e. data/products.txt
        based on provided product_id
        :param product_id: accepts product_id str
        :return: returns bool based on success
        """
        pass

    def get_product_list_by_keyword(self, keyword):
        """
        method to retrieve all products whose name
        contains the keyword (case sensitive)
        :param keyword: accepts keyword as str
        :return: returns list of products
        """
        pass

    def get_product_by_id(self, product_id):
        """
        method returns 1 product object based on the given ID
        :param product_id: accepts product_id as str
        :return: returns product object or None if cannot be found
        """
        pass

    def generate_category_figure(self):
        """
        method generates a bar chart that shows the total no.
        of products for each category in descending order.
        The figure is saved into the data/figure folder
        :return: None
        """
        pass

    def generate_discount_figure(self):
        """
         method generates pie chart that shows the proportion of
         products that have a discount value < 30, 30 >= 60, & > 60.
         Chart is saved into the data/figure folder.
        :return: None
        """
        pass

    def generate_likes_count_figure(self):
        """
        method generates chart displaying the sum of products’ likes_count
        for each category (ascending). Chart is saved into the data/figure folder
        :return: None
        """
        pass

    def generate_dislikes_count_figure(self):
        """
        method generates scatter chart showing relationship
        between likes_count/discount for all products.
        Chart is saved into the data/figure folder
        :return: None
        """
        pass

    def delete_all_products(self):
        """
        method removes all the product data in the data/products.txt file
        :return: None
        """
        pass


