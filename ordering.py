
from data import menu, tables

def show_menu():
    print("\n--- MENU ---")
    for item_id, item in menu.items():
        print(f"{item_id}. {item['name']} - Rs.{item['price']}")


def add_item(table_no, item_id, qty):
    item = menu[item_id]
    tables[table_no]["order"].append(
        {"name": item["name"], "price": item["price"], "qty": qty}
    )
    print(f"Added {qty} x {item['name']} to Table {table_no}'s order.")


def place_order():
    try:
        table_no = int(input("Enter table number: "))
    except ValueError:
        print("Invalid table number.")
        return

    if table_no <= 0:
        print("Table number must be a positive number.")
        return

    show_menu()
    items_added = 0
    while True:
        try:
            item_id = int(input("Enter item ID to add (0 to finish): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if item_id == 0:
            break
        if item_id not in menu:
            print("Invalid item ID.")
            continue

        try:
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                print("Quantity must be a positive number.")
                continue
        except ValueError:
            print("Please enter a valid quantity.")
            continue

        if table_no not in tables:
            tables[table_no] = {"order": [], "status": "Placed"}

        add_item(table_no, item_id, qty)
        items_added += 1

    if items_added == 0:
        print("No items were added. Order not placed.")
        return

    tables[table_no]["status"] = "Placed"
    print(f"Order placed for Table {table_no}.")
