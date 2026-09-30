#DASHBOARD

from data import tables, status

def view_all_orders():
    if not tables:
        print("No orders yet.")
        return
    for table_no, info in tables.items():
        print(f"\nTable {table_no} - Status: {info['status']}")
        for item in info["order"]:
            print(f"  {item['name']} x{item['qty']}")


def view_order_by_table():
    try:
        table_no = int(input("Enter table number: "))
    except ValueError:
        print("Invalid input.")
        return

    if table_no not in tables:
        print("No such table/order.")
        return

    info = tables[table_no]
    print(f"\nTable {table_no} - Status: {info['status']}")
    for item in info["order"]:
        print(f"  {item['name']} x{item['qty']}")


def update_order_status():
    try:
        table_no = int(input("Enter table number: "))
    except ValueError:
        print("Invalid input.")
        return

    if table_no not in tables:
        print("No such table/order.")
        return

    print("Statuses:", ", ".join(status))
    new_status = input("Enter new status: ").strip().title()

    if new_status not in status:
        print("Invalid status.")
        return

    tables[table_no]["status"] = new_status
    print(f"Table {table_no} status updated to {new_status}.")
