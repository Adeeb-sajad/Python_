class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self,other):
        if(self.price > other.price):
            return True 
        else :
            return False

order1 = order("shoes",190)
order2 = order("shirt",100)

if(order1 > order2):
    print(f"{order1.item} is more expensive then {order2}")
else :
    print(f"{order2.item} is more expensive then {order1}") 