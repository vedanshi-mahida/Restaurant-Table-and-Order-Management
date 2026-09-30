# Problem Statement

Manual order-taking in dine-in restaurants is slow and error-prone: orders
are written on paper, communicated verbally to the kitchen, and tracked with
no clear record of status or billing. This leads to delayed service,
miscommunication between staff and kitchen, and billing mistakes.

## Scope

This project builds a simplified digital ordering and table management
system that simulates the core dine-in workflow: menu browsing, order
placement, kitchen status tracking, table reservations, itemized billing,
payment, and table clearing.

The project intentionally excludes: a persistent database, real payment
gateway integration, user authentication/accounts, delivery logistics,
inventory management, and discount systems - to keep the scope focused and
achievable within the course requirements.

## Target Users

- **Customers** placing Dine-in or Takeaway orders
- **Restaurant staff** managing orders, updating kitchen status, handling
  reservations, generating bills, and processing payments

## High-Level Features

- Digital menu with categorized items
- Order placement with quantity and special instructions
- Real-time order status tracking through the kitchen workflow
- Table status and reservation management
- Itemized billing with tax calculation
- Payment recording and table release
