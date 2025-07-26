import json
import os
from datetime import datetime
import uuid  # importing to help generate unique receipt no.

items = []

# defining file name
filename = "receipts.json"

# checking if path exists
if os.path.exists(filename):
    with open(filename, "r") as file:
        all_receipts = json.load(file) #load existing data
else:
    all_receipts = {}  # Start with an empty dictionary


while True:
    # taking input from user about item purchase
    print("\nEnter item details:")
    name = input("Item name: ")
    qty = int(input("Quantity: "))
    price = float(input("Price per unit: "))
    tax_rate = float(input("Tax rate (%): "))

    item_total = qty * price
    item_tax = (tax_rate / 100) * item_total
    final_price = item_total + item_tax

    # storing items in a list of dictionaries
    items.append({
        "name": name,
        "qty": qty,
        "price": price,
        "tax_rate": tax_rate,
        "tax": item_tax,
        "total": final_price
    })

    more = input("Add more items? (Y/n): ")
    if more.lower() != "y":
        break

# adding current date and time to receipt
now = datetime.now()
date_str = now.strftime("%Y-%m-%d %H:%M:%S")
# strftime method is used to format a datetime object into 
# a string representation based on a specified format
receipt_no = "RCPT" + str(uuid.uuid4())[:8].upper()

# printing the receipt
print("\n" + "=" * 40)
print("            XYZ GENERAL STORE")
print("=" * 40)
print("Date: {}".format(date_str))
print("Receipt No: {}".format(receipt_no))
print("{:<12}{:>4}{:>7}{:>6}{:>9}".format("Item", "Qty", "Price", "Tax%", "Total"))
print("-" * 40)

# adding up the total for each item
subtotal = 0
for it in items:
    print("{:<12} {:>4} {:>7.2f} {:>5.1f} {:>9.2f}".format(
        it["name"], it["qty"], it["price"], it["tax_rate"], it["total"]))
    subtotal += it["total"]

print("-" * 40)
print("{:<28} {:>8.2f}".format("Grand Total:", subtotal))
print("=" * 40)
print("Thanks for shopping with XYZ General Store!")

# creating the receipt data dictionary
receipt_data = {
    "date": date_str,
    "receipt_no": receipt_no,
    "items": items,
    "total": subtotal
}
 
# Step 4: Add new receipt using receipt_no as key
all_receipts[receipt_no] = receipt_data

# Step 5: Save back to file
with open(filename, "w") as file:
    json.dump(all_receipts, file, indent=4)
    # ident =4 says print with identation of 4 spaces

print("✅ Receipt saved successfully to 'receipts.json'")
