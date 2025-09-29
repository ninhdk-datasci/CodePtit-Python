class Invoice: 
    def __init__(self, product, name, amount, price, discount):
        self.product = product
        self.name = name 
        self.amount = amount 
        self.price = price 
        self.discount = discount 
        self.pay = amount * price - discount 
    def __repr__(self): 
        return self.product + " " + self.name + " " + str(self.amount) + " " + str(self.price) + " " + str(self.discount) + " " + str(self.pay)


invoice = int(input()) 

invoice_list = []

for _ in range(invoice): 
    product = input()
    name = input()
    amount = int(input())
    price = int(input())
    discount = int(input())
    inv = Invoice(product, name, amount, price, discount) 
    invoice_list.append(inv) 

invoice_list.sort(key = lambda inv : -inv.pay) 

for inv in invoice_list: 
    print(inv) 












