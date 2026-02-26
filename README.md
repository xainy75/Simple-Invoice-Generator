# 🧾 Simple Invoice Generator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python 3.x" />
  <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status" />
  <img src="https://img.shields.io/badge/Type-Console%20App-orange" alt="Console App" />
</p>

<p align="center">
  A lightweight, beginner-friendly Python invoice generator that computes item totals, applies automatic tax, and prints a clean, formatted invoice — all in seconds.
</p>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#️-tech-stack)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Sample Output](#-sample-output)
- [Screenshots](#-screenshots)
- [Author](#-author)

---

## 🔍 Overview

**Simple Invoice Generator** is a console-based Python application designed for learning and practical use. It allows you to build an invoice by adding line items, then automatically calculates subtotals, taxes, and a grand total — printing a neatly formatted receipt to the terminal.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📦 Multi-item support | Add as many products/services as needed |
| 🔢 Quantity & price tracking | Specify quantity and unit price per item |
| ➕ Subtotal calculation | Automatically sums all line-item totals |
| 💸 Auto tax calculation | Applies an 8% tax rate on the subtotal |
| 🧮 Grand total | Displays the final amount including tax |
| 📅 Date stamping | Automatically adds today's date to every invoice |
| 🖨️ Formatted output | Clean, aligned, console-friendly invoice layout |

---

## 🛠️ Tech Stack

| Component | Detail |
|---|---|
| **Language** | Python 3.x |
| **Application Type** | Console / CLI |
| **Standard Libraries** | `datetime` |
| **Dependencies** | None — zero third-party packages required |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/xainy75/Simple-Invoice-Generator.git
   cd Simple-Invoice-Generator
   ```

2. **Run the script**

   ```bash
   python "invoice system.py"
   ```

> No virtual environment or package installation required — the app uses only Python's standard library.

---

## 📖 Usage

You can customise the invoice by editing the `__main__` block at the bottom of `invoice system.py`:

```python
# Create an invoice for a client
my_invoice = InvoiceSystem("Alice Wonderland")

# Add line items: (item name, quantity, unit price)
my_invoice.add_item("Mechanical Keyboard", 1, 120.00)
my_invoice.add_item("USB-C Cable",          3,  15.50)
my_invoice.add_item("Ergonomic Mouse",      1,  85.00)

# Print the formatted invoice
my_invoice.generate_invoice()
```

You can also use `InvoiceSystem` programmatically in your own projects:

```python
from invoice_system import InvoiceSystem

invoice = InvoiceSystem("John Doe")
invoice.add_item("Web Design", 1, 500.00)
invoice.add_item("Hosting (1 yr)", 1, 120.00)
invoice.generate_invoice()
```

---

## 🖥️ Sample Output

```
========================================
           OFFICIAL INVOICE
========================================
Customer: Alice Wonderland
Date: 2026-01-30
----------------------------------------
Item                 Qty   Price    Total
Mechanical Keyboard  1     $120.00  $120.00
USB-C Cable          3     $15.50   $46.50
Ergonomic Mouse      1     $85.00   $85.00
----------------------------------------
Subtotal:                           $251.50
Tax (8%):                            $20.12
**GRAND TOTAL:                      $271.62**
========================================
        Thank you for your business!
========================================
```

---

## 📸 Screenshots

### Code

<img width="1396" height="1069" alt="Invoice Generator Code" src="https://github.com/user-attachments/assets/77cb6b3a-a69b-40fd-aa2c-7441c9d701e3" />

### Invoice Output

<img width="502" height="456" alt="Invoice Generator Output" src="https://github.com/user-attachments/assets/302742d2-1dcd-4f59-8095-0f66d0d21494" />

---

## 👤 Author

**Zain Ul Abidin**

- GitHub: [@xainy75](https://github.com/xainy75)

---

<p align="center">Made with ❤️ in Python</p>
