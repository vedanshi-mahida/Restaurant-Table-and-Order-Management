"""
management.py
Module 3: Table and Order Management Module
"""

from data import tables


def calculate_bill():
    try:
        table_no = int(input("Enter table number: "))
    except ValueError:
        print("Invalid input.")
        return

    if table_no not in tables or not tables[table_no]["order"]:
        print("No order found for this table.")
        return

    total = 0
    print(f"\n--- Bill for Table {table_no} ---")
    for item in tables[table_no]["order"]:
        cost = item["price"] * item["qty"]
        total += cost
        print(f"{item['name']} x{item['qty']} = Rs.{cost}")
    print(f"Total Bill: Rs.{total}")


def clear_table():
    try:
        table_no = int(input("Enter table number: "))
    except ValueError:
        print("Invalid input.")
        return

    if table_no in tables:
        del tables[table_no]
        print(f"Table {table_no} cleared and is now available.")
    else:
        print("No such table.")
