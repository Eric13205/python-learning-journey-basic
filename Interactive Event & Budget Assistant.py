print("      Hello, Welcome to Event      ")
book_fee = 5
tax_rate  = 0.1
full_name = input("Full Name : ")
ticket_category = input("Preferred ticket category (e.g., General or VIP) : ")
print('General = $25.50, VIP = $50.00)')
quantity_input = input("How many tickets do you want? ")
quantity = int(quantity_input)
if ticket_category == 'General':
    ticket_price = 25.50
    quantity_ticket = ticket_price*float(quantity_input)
    final_amount = quantity_ticket+book_fee  
elif ticket_category == 'VIP':
    ticket_price = 50.00
    quantity_ticket = ticket_price*float(quantity_input)
    final_amount = quantity_ticket+book_fee
print(f'Name : {full_name}')
print(f'category : {ticket_category}')
print(f'Number of ticket : {quantity}')
print(f'book fee : {book_fee} $')
print(f'tax rate : 10% ')
print("Final Amount :",final_amount+(final_amount*tax_rate))
