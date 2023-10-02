# Note: All the products are saved in the files “data/products.txt”
class Product:

    def __init__(self,
                 pro_id="default_id",
                 pro_model="default_model",
                 pro_category="default_category",
                 pro_name="default_name",
                 pro_current_price="0",
                 pro_raw_price="0",
                 pro_discount="0",
                 pro_likes_count="0"
                 ):

        self.pro_id = pro_id
        self.pro_model = pro_model
        self.pro_category = pro_category
        self.pro_name = pro_name
        self.pro_current_price = pro_current_price
        self.pro_raw_price = pro_raw_price
        self.pro_discount = pro_discount
        self.pro_likes_count = pro_likes_count

    def __str__(self):
        return (f"pro_id: {self.pro_id}, "
                f"pro_model: {self.pro_model}, "
                f"pro_category: {self.pro_category}, "
                f"pro_name: {self.pro_name}, "
                f"pro_current_price: {self.pro_current_price}, "
                f"pro_raw_price: {self.pro_raw_price}, "
                f"pro_discount: {self.pro_discount}, "
                f"pro_likes_count: {self.pro_likes_count}")
