class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu:
    def __init__(self, name):
        self.name = name
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"{item_name} not found in {self.name} menu.")

    def display(self):
        print(f"\n{self.name} Menu:")
        for item_name, item in self.items.items():
            print(f"{item_name}: ₹{item.price}")

class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append(OrderItem(item, quantity))

    def calculate_total(self):
        total = sum(item.menu_item.price * item.quantity for item in self.items)
        return total
    
    def remove_item(self, item_name, quantity):
        for item in self.items:
            if item.menu_item.name == item_name:
                if item.quantity <= quantity:
                    self.items.remove(item)
                    print(f"{item_name} removed from order.")
                    return
                else:
                    item.quantity -= quantity
                    print(f"{quantity} {item_name}(s) removed from order.")
                    return
        print(f"{item_name} not found in order.")

    def display_order(self):
        print("\nYour Order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.menu_item.name} x {item.quantity}: ₹{item.menu_item.price * item.quantity}")

def main():
    # Create menus
    north_menu = Menu("North Indian Food")
    bangal_menu = Menu("Bangali Food")
    south_menu = Menu("South Indian Food")
    chin_menu = Menu("Chinese Food")
    itn_menu = Menu("Italian Food")
    drinks_menu = Menu("Drinks")

    # Add items to menus
    north_menu.add_item(MenuItem("Amritsari Kulcha", 60))
    north_menu.add_item(MenuItem("Tandoori Chicken", 180))
    north_menu.add_item(MenuItem("Chole Bhature", 35))
    north_menu.add_item(MenuItem("Malai Kofta", 130))
    north_menu.add_item(MenuItem("Dhokla", 30))

    bangal_menu.add_item(MenuItem("Luchi and Cholar Dal", 50))
    bangal_menu.add_item(MenuItem("Radhaballabhi", 45))
    bangal_menu.add_item(MenuItem("Kolkata Dum Biriyani", 240))
    bangal_menu.add_item(MenuItem("Non Veg Special Main Course", 145))
    bangal_menu.add_item(MenuItem("Fish Finger", 70))


    south_menu.add_item(MenuItem("Idli Sambar", 30))
    south_menu.add_item(MenuItem("Vada Sambar", 30))
    south_menu.add_item(MenuItem("Masala Dosa", 40))
    south_menu.add_item(MenuItem("Mexican Spl Dosa", 90))
    south_menu.add_item(MenuItem("Upma", 40))
    south_menu.add_item(MenuItem("Pongal", 50))
    south_menu.add_item(MenuItem("Uttapam", 45))
   

    
    chin_menu.add_item(MenuItem("Chilli Chicken", 180))
    chin_menu.add_item(MenuItem("Chow Mein", 80))
    chin_menu.add_item(MenuItem("Spring Rolls", 45))
    chin_menu.add_item(MenuItem("Manchurian-8pcs", 140))
    chin_menu.add_item(MenuItem("Spl Chicken Soup", 110))
    chin_menu.add_item(MenuItem("Kung Pao Chicken", 180))
    chin_menu.add_item(MenuItem("Sweet and Sour Pork", 165))



    itn_menu.add_item(MenuItem("Margherita Pizza", 130))
    itn_menu.add_item(MenuItem("Spl Delite Pizza", 160))
    itn_menu.add_item(MenuItem("Pln Pasta", 70))
    itn_menu.add_item(MenuItem("Red Sause Pasta", 90))
    itn_menu.add_item(MenuItem("White Sause Pasta", 100))
    itn_menu.add_item(MenuItem("Ribollita", 195))



    drinks_menu.add_item(MenuItem("Water-750ml", 15))
    drinks_menu.add_item(MenuItem("Soda", 20))
    drinks_menu.add_item(MenuItem("Coffee", 35))
    drinks_menu.add_item(MenuItem("Lassi Special", 60))
    drinks_menu.add_item(MenuItem("Mojito", 40))



    # Create order
    order = Order()

    while True:
        print("\n\n\n RESTAURANT SKYLIGHTERS \n")
        
        print("\nSelect Menu:")
        print("1. North Indian Food")
        print("2. Bangali Food")
        print("3. South Indian Food")
        print("4. Chinese Food")
        print("5. Italian Food")
        print("6. Drinks")
        print("7. Recheck Your Order")
        print("8. Done and Calculate Total \n")
      
    
       
        

        choice = input("Enter your choice: ")

        if choice == "1":
            north_menu.display()
            item_name = input("Enter item name to add to order: ")
            if item_name in north_menu.items:
                quantity = int(input("Enter quantity: "))
                order.add_item(north_menu.items[item_name], quantity)
            else:
                print("Invalid item!")

        elif choice == "2":
            bangal_menu.display()
            item_name = input("Enter item name to add to order: ")
            if item_name in bangal_menu.items:
                quantity = int(input("Enter quantity: "))
                order.add_item(bangal_menu.items[item_name], quantity)
            else:
                print("Invalid item!")

        elif choice == "3":
            south_menu.display()
            item_name = input("Enter item name to add to order: ")
            if item_name in south_menu.items:
                quantity = int(input("Enter quantity: "))
                order.add_item(south_menu.items[item_name], quantity)
            else:
                print("Invalid item!")

        elif choice == "4":
            chin_menu.display()
            item_name = input("Enter item name to add to order: ")
            if item_name in chin_menu.items:
                quantity = int(input("Enter quantity: "))
                order.add_item(chin_menu.items[item_name], quantity)
            else:
                print("Invalid item!")

        elif choice == "5":
            itn_menu.display()
            item_name = input("Enter item name to add to order: ")
            if item_name in itn_menu.items:
                quantity = int(input("Enter quantity: "))
                order.add_item(itn_menu.items[item_name], quantity)
            else:
                print("Invalid item!")        



        elif choice == "6":
            drinks_menu.display()
            item_name = input("Enter item name to add to order: ")
            if item_name in drinks_menu.items:
                quantity = int(input("Enter quantity: "))
                order.add_item(drinks_menu.items[item_name], quantity)
            else:
                print("Invalid item!")

        elif choice == "7":

            order.display_order()
            opt = "y"
            opt = input("Press ['Y'/'y'] to remove an item added by  mistake -> ")
            if(opt == "y" or opt == "Y") :
                itemName = input("Enter name of  item : ")
                noOfItem = int(input("Enter quantity to remove : "))
                order.remove_item(itemName, noOfItem)
           
        elif choice == "8":
            order.display_order()
            total = order.calculate_total()
            print(f"\nTotal: ₹{total}")
            print("\n \n THANK YOU ")
            print(" VISIT AGAIN \n")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()