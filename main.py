import re

# Formatting number to currency 
def num2idr(number):
    number = str(number)
    idr = 'Rp'
    while len(number) > 0:
        head = len(number) % 3
        if head == 0: head = 3
        idr += number[:head] + '.'
        number = number[head:]
    idr = idr[:-1] + ',-'
    return idr

# List of items and prices
all_items = [{'item': "susu", 'harga': 50000}, 
             {'item': "daging", 'harga': 20000}, 
             {'item': "lampu", 'harga': 15000}, 
             {'item': "masker", 'harga': 25000},
             {'item': "apel", 'harga': 30000}]
promotional_items = [{'item': "susu", 'harga': 50000},
                     {'item': "masker", 'harga': 25000}]
item_prices = {}
for c in all_items:
    item_prices[c['item']] = c['harga']

# Greetings to consumer
greeting_message = f"""Salam Sehat Selalu, promo istimewa dari Supermarket X hanya untuk anda.
Nikmati promo minggu ini:"""
for item in promotional_items:
    name = item['item']
    price = item['harga']
    space = " " * (10-len(name))
    greeting_message += f"\n- {name.capitalize()}{space}: {num2idr(price)}"

greeting_message += f"\n\nApakah anda ingin membeli item promo? (beli/lainnya)\n"

# First input to choose direct buy or get another items
input1 = input(greeting_message)
all_items_message = ''

if input1 == 'lainnya':
    for item in all_items:
        name = item['item']
        price = item['harga']
        space = " " * (10-len(name))
        all_items_message += f"\n- {name.capitalize()}{space}: {num2idr(price)}"
all_items_message += f"""\n\nCara membeli, ketik: [jumlah 1]<spasi>[nama item 1]<spasi>[jumlah 2]<spasi>[nama item 2][jumlah n]<spasi>[nama item n]. 
Misal: 2 apel and 2 susu

Apa yang ingin anda beli?\n"""

# Case 1: "buy 3 masker and 2 susu"
input2 = input(all_items_message)
items_to_buy = re.findall('[0-9]+ [A-z]+', input2)

total_price = 0
cart_message = "=" * 33 + '\nKeranjang belanja anda'
for item in items_to_buy:
    count, item_name = item.strip().split(' ')
    count = int(count)
    item_name = item_name.lower()
    price = item_prices[item_name] * count
    price_str = num2idr(price)
    total_price += price
    cart = f"\n- {count} x {item_name}"
    cart += " " * (20 - len(cart))
    cart += f":{' '*(14-(len(price_str)))}{price_str}"
    cart_message += cart

print(cart_message)
total_message = "=" * 33
total_message += f"\nTotal :                {num2idr(total_price)}"
print(total_message)