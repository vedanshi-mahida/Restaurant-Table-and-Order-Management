# Restaurant-Table-and-Order-Management

# Overview
A console-based Python application that simulates the complete workflow of a
dine-in restaurant, from browsing the menu and placing an order, to kitchen
status updates, billing, payment, and table management. The system runs
entirely in memory (no external files or database) and is built using plain
functions, lists, and dictionaries.

# Features
- Categorized menu (Starters, Main Course, Beverages, Desserts)
- Dine-in and Takeaway order types
- Table management with capacity and live status (Available / Occupied / Reserved)
- Unique Order IDs for every order
- Item quantity and optional special instructions per item
- Order status tracking (Placed -> Preparing -> Ready -> Served -> Completed)
- Staff dashboard to view all orders, search a specific order, and update status
- Table reservations
- Itemized billing with tax calculation
- Payment handling (Cash / UPI / Card)
- Table clearing once an order is completed and paid

# Technologies Used
- Python 3 (standard library only, no external packages)

# How to Install & Run
1. Make sure Python 3 is installed on your system.
2. Clone this repository or download the files into one folder.
3. Open the folder in Sublime text (or any terminal).
4. Run:python main.py

# How to Test
1. Run the program.
2. Choose option 1 to place a Dine-in order for Table 1, add a few items
with a special instruction.
3. Choose option 5 (Staff - View Tables) to confirm the table is now Occupied.
4. Choose option 4 (Staff - Update Order Status) to move the order through
Preparing -> Ready -> Served -> Completed.
5. Choose Generate Bill to see the itemized bill with tax.
6. Choose Process Payment and select a payment method.
7. Choose Clear Table to confirm the table becomes Available again.
