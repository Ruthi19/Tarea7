from user import User
from cart import Cart
from ownable import ownable
class Customer(User, ownable):

    def __init__(self, name):
        super().__init__(name)
        self.cart = Cart(self)  # Customerインスタンスは生成されると、自身をオーナーとするカートを持ちます。
