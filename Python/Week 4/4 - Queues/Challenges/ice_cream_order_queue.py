class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor in self.flavors and scoops in range(1, 4):
            print("Order created!")
            order = {"customer": customer,"flavor": flavor, "scoops": scoops}
            self.orders.enqueue(order)
        else:
            if flavor not in self.flavors:
                print("Sorry, we don't have that flavor")
            if scoops not in range(1, 4):
                print("Must be 1-3 scoops")

    def show_all_orders(self):
        print(f"\nAll pending ice cream orders:")
        for i in range(len(self.orders.items)):
            print(f'Customer: {self.orders.items[i]["customer"]} -- Flavor: {self.orders.items[i]["flavor"]} -- Scoops: {self.orders.items[i]["scoops"]}')

    def next_order(self):
        print("\nNext Order Up!")
        order = self.orders.dequeue()
        print("Customer", order["customer"], "-- Flavor:",
              order["flavor"], "-- Scoops:", order["scoops"])

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()