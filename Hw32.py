class Character:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Character's name is {self.name}")


def special_ability(max_uses):
    def decorator(func):
        func.uses_left = max_uses
        def wrapper(*args, **kwargs):
            if func.uses_left > 0:
                func.uses_left -= 1
                return func(*args, **kwargs)
            else:
                print("No uses left for this ability!")
                return None
        return wrapper
    return decorator


class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.inventory = Inventory()

    def introduce(self):
        print(f"Player's name is {self.name}")

    @special_ability(3)
    def special_move(self):
        print("Special move activated!")


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item} to inventory")

    def __iter__(self):
        return iter(self.items)


def health_manager(initial_health=100):
    health = initial_health
    def manage_health(amount=0):
        nonlocal health
        health += amount
        return health
    return manage_health


def find_item(inventory, item_name):
    for item in inventory:
        if item == item_name:
            yield item
            return
    yield "Item not found"
