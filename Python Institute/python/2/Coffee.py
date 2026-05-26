class CoffeeMenuItem:
    def __init__(self, name, prize, size):
        self.name = name
        self.prize = prize
        self.size = size

items = [
    CoffeeMenuItem("Latte", 5.50, "20"),
    CoffeeMenuItem("Cold Brew", 4.50, "16")
]
for item in items:
    print(f"Drink: {item.name} costs ${item.prize} and is size {item.size} oz.")