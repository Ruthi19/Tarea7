from user import User
from ownable import ownable
class Seller(User,ownable):
    def __init__(self, name):
        super().__init__(name)