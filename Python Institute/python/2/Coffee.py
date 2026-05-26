class CoffeeMenuItem:
    def __init__(self, name, prize, size):
        self.name = name
        self.prize = prize
        self.size = size

latte = CoffeeMenuItem("Latte", 5.50, "20")
cold_brew = CoffeeMenuItem("Cold Brew", 4.50, "16")

print(f"Drink: {latte.name} costs ${latte.prize} and is size {latte.size} oz.")
print(f"Drink: {cold_brew.name} costs ${cold_brew.prize} and is size {cold_brew.size} oz.")