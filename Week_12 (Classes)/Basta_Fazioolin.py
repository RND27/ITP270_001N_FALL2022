class Franchise:
    pass
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
        
    def __repr__(self):
        return self.address
        
    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menus.append(menu)
        return available_menus

class Menu:
    pass
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        return f'{self.name} is available from {self.start_time} to {self.end_time}.'
    
    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
            else:
                print('At least one item is not available on the menu.')
                return None
        return bill

# Brunch Menu
brunch_menu = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50,
    'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50,
    'orange juice': 3.50
    }
brunch = Menu('Brunch', brunch_menu, 1100, 1600)

# Early Bird Menu
early_bird_menu = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
    }
early_bird = Menu('Early Bird', early_bird_menu, 1500, 1800)

# Dinner Menu
dinner_menu = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00,
    'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
    }
dinner = Menu('Dinner', dinner_menu, 1700, 2300)

# Kids Menu
kids_menu = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
    }
kids = Menu('Kids', kids_menu, 1100, 2100)

# All Menu OBJECTS
menus = [brunch, early_bird, dinner, kids]

# 12
flagship_store = Franchise('1232 West End Road', menus)
new_installment = Franchise('12 East Mulberry Street', menus)


print(flagship_store.available_menus(1200))
