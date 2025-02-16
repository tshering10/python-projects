class Item:
    def __init__(self,name,price, quantity, supplier):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.supplier = supplier
    
    def __str__(self):
        return f"({self.name}, Qty: {self.quantity}, Price: RS{self.price}, Supplier: {self.supplier}) "

class Inventory:
    def __init__(self):
        self.items = []
        
    def add_item(self, item):
        self.items.append(item)
   
    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]
        
    def update_item(self, item_name, quantity = None, price = None):
        for item in self.items:
            if item.name == item_name:
                if quantity is not None:
                    self.quantity = quantity
                if price is not None:
                    self.price = price
    
    def display(self):
        for item in self.items:
            print(item)

def main():
    inventory = Inventory() 
    while True:
        print('Welcome to inventory management system.')
        print("""
             
    1. Add Item
    2. Remove Item
    3. Update Item
    4. View Item
    5. Exit 
        """)
        
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Wrong options. Choose 1/2/3/4/5 only.")
            continue
            
        if choice == 1:
            name = input("Enter item name: ")
            quantity = input('Enter quantity: ')
            price = input('Enter price: ')
            supplier = input('Enter supplier: ')
            
            item = Item(name, price, quantity, supplier)
            inventory.add_item(item)
            
        elif choice == 2:
            name = input("Enter item name: ")
            inventory.remove_item(name)
            
        elif choice == '3':
            name = input("Enter item name to update: ")
            quantity = int(input("Enter new quantity (or leave blank to skip): ") or "0")
            price = float(input("Enter new price (or leave blank to skip): ") or "0")
            inventory.update_item(name, quantity if quantity > 0 else None, price if price > 0 else None)

        elif choice == '4':
            inventory.display()

        elif choice == '5':
            print("Inventory saved. Exiting.")
            break
        else:
            print("Invalid option. try again")
            
    print("See you")
    
main()