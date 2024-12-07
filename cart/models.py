from datetime import datetime

# In-memory storage
CARTS = {}
ORDERS = []
DISCOUNT_CODES = []

class Cart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []
        self.total = 0.0

    def add_item(self, item_id, item_name, price, quantity):
        self.items.append({
            "item_id": item_id,
            "item_name": item_name,
            "price": price,
            "quantity": quantity,
        })
        self.total += price * quantity

class DiscountCode:
    def __init__(self, code, nth_order):
        self.code = code
        self.nth_order = nth_order
        self.used = False

def generate_discount_code(nth_order):
    code = f"DISCOUNT{nth_order}"
    DISCOUNT_CODES.append(DiscountCode(code, nth_order))
    return code
