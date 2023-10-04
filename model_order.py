# Note: All the orders are saved in the file “data/orders.txt”
class Order:

    def __init__(self,
                 order_id="o_00000",
                 user_id="u_0000000000",
                 prod_id="0000000",
                 order_time="00-00-0000_00:00:00"):

        self.order_id = order_id
        self.user_id = user_id
        self.prod_id = prod_id
        self.order_time = order_time

    def __str__(self):
        return (f"order_id: {self.order_id}, "
                f"user_id: {self.user_id}, " 
                f"prod_id: {self.prod_id}, " 
                f"order_time: {self.order_time}")


