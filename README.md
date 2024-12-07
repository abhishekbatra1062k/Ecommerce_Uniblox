# Ecommerce Store API

## Project Overview
This project is a Django-based eCommerce store backend with core functionalities like:
1. Adding items to the cart.
2. Placing orders and applying discount codes.
3. Admin APIs for generating discount codes and viewing analytics.

The project is built with an in-memory storage approach for simplicity but is extensible for database integration.

---

## Features
- **User APIs**:
  - Add items to a cart.
  - Checkout and validate discount codes.
- **Admin APIs**:
  - Generate discount codes for every nth order.
  - View analytics for sales, revenue, and discounts.

---

## Technologies Used
- **Backend**: Django, Django REST Framework
- **Language**: Python
- **Testing**: Postman Collection
- **In-memory Storage**: Python objects (extendable to MongoDB or relational databases)

