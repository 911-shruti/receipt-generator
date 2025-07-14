from datetime import datetime
import uuid  # importing to help generate unique receipt no.

items = []
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
for item in items:
    print("{:<12} {:>4} {:>7.2f} {:>5.1f} {:>9.2f}".format(
        item["name"], item["qty"], item["price"], item["tax_rate"], item["total"]))
    subtotal += item["total"]

print("-" * 40)
print("{:<28} {:>8.2f}".format("Grand Total:", subtotal))
print("=" * 40)
print("Thanks for shopping with XYZ General Store!")
