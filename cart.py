from ownable import ownable
class Cart(ownable):
    from item_manager import show_items

    def __init__(self,owner):
        super().__init__()
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print ("Fondos insuficientes en el monedero del propietario del carrito.")

        for item in self.items:
            item.owner.wallet.balance += item.price  # Transferir dinero al propietario del artículo
            self.owner.wallet.balance -= item.price  # Restar dinero del propietario del carrito
            item.owner = self.owner  # Transferir propiedad del artículo al propietario del carrito

        self.items.clear()  # Vaciar el carrito
