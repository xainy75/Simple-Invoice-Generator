import datetime

class InvoiceItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total = quantity * price

class InvoiceSystem:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        self.tax_rate = 0.08  # Custom Feature: Automatic Tax Calculation (8%)

    def add_item(self, name, quantity, price):
        item = InvoiceItem(name, quantity, price)
        self.items.append(item)

    def generate_invoice(self):
        subtotal = sum(item.total for item in self.items)
        tax_amount = subtotal * self.tax_rate
        grand_total = subtotal + tax_amount

        # Formatting the Output
        print("\n" + "="*40)
        print(f"{'OFFICIAL INVOICE':^40}")
        print("="*40)
        print(f"Customer: {self.customer_name}")
        print(f"Date: {datetime.date.today()}")
        print("-"*40)
        print(f"{'Item':<20} {'Qty':<5} {'Price':<8} {'Total':<5}")
        
        for item in self.items:
            print(f"{item.name:<20} {item.quantity:<5} ${item.price:<7.2f} ${item.total:<5.2f}")
        
        print("-"*40)
        print(f"{'Subtotal:':<32} ${subtotal:>6.2f}")
        print(f"{'Tax (8%):':<32} ${tax_amount:>6.2f}")
        print(f"**{'GRAND TOTAL:':<30} ${grand_total:>6.2f}**")
        print("="*40)
        print(f"{'Thank you for your business!':^40}\n")

# --- Execution ---
if __name__ == "__main__":
    # Create an invoice for a client
    my_invoice = InvoiceSystem("Alice Wonderland")
    
    # Adding items
    my_invoice.add_item("Mechanical Keyboard", 1, 120.00)
    my_invoice.add_item("USB-C Cable", 3, 15.50)
    my_invoice.add_item("Ergonomic Mouse", 1, 85.00)
    
    # Generate the result
    my_invoice.generate_invoice()