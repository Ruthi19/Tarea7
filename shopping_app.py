from customer import Customer
from item import Item
from seller import Seller

seller = Seller("DIC Store")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memoria", 13880, seller)
    Item("Placa Base", 28980, seller)
    Item("Fuente de Alimentación", 8980, seller)
    Item("Caja de PC", 8727, seller)
    Item("HDD de 3.5 pulgadas", 10980, seller)
    Item("SSD de 2.5 pulgadas", 13370, seller)
    Item("SSD M.2", 12980, seller)
    Item("Refrigerador de CPU", 13400, seller)
    Item("Tarjeta Gráfica", 23800, seller)

print("🤖 Por favor, dime tu nombre")
customer = Customer(input())

print("🏧 Por favor, introduce la cantidad a depositar en el monedero")
customer.wallet.deposit(int(input()))

print("🛍️ Empezando a comprar")
end_shopping = False
while not end_shopping:
    print("📜 Lista de productos")
    seller.show_items()

    print("️️⛏ Por favor, introduce el número del producto")
    number = int(input())

    print("⛏ Por favor, introduce la cantidad del producto")
    quantity = int(input())

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contenido del carrito")
    customer.cart.show_items()
    print(f"🤑 Importe total: {customer.cart.total_amount()}")

    print("😭 ¿Quieres terminar de comprar? (yes/no)")
    end_shopping = input().lower() == "yes"

print("💸 ¿Quieres confirmar la compra? (yes/no)")
if input().lower() == "yes":
    customer.cart.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Resultados┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ Propiedades de {customer.name}")
customer.show_items()
print(f"😱👛 Saldo del monedero de {customer.name}: {customer.wallet.balance}")

print(f"📦 Inventario de {seller.name}")
seller.show_items()
print(f"😻👛 Saldo del monedero de {seller.name}: {seller.wallet.balance}")

print("🛒 Contenido del carrito")
customer.cart.show_items()
print(f"🌚 Importe total: {customer.cart.total_amount()}")

print("🎉 Fin")