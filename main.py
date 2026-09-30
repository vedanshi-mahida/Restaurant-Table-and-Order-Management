

from ordering import place_order
from dashboard import view_all_orders, view_order_by_table, update_order_status
from management import calculate_bill, clear_table


def main():
    while True:
        print("\n===== Restaurant Digital Ordering System =====")
        print("1. Customer - Place Order")
        print("2. Staff - View All Orders")
        print("3. Staff - View Order by Table")
        print("4. Staff - Update Order Status")
        print("5. Calculate Bill")
        print("6. Clear Table")
        print("7. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            place_order()
        elif choice == "2":
            view_all_orders()
        elif choice == "3":
            view_order_by_table()
        elif choice == "4":
            update_order_status()
        elif choice == "5":
            calculate_bill()
        elif choice == "6":
            clear_table()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
