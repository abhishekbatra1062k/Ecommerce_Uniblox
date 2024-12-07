from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *

class AddToCartView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        item_id = request.data.get('item_id')
        item_name = request.data.get('item_name')
        price = request.data.get('price')
        quantity = request.data.get('quantity')

        if not user_id or not item_id or not price or not quantity:
            return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)

        if user_id not in CARTS:
            CARTS[user_id] = Cart(user_id)

        cart = CARTS[user_id]
        cart.add_item(item_id, item_name, price, quantity)

        return Response({
            "message": "Item added to cart.",
            "cart": {
                "items": cart.items,
                "total": cart.total
            }
        })
    
class CheckoutView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        discount_code = request.data.get('discount_code', None)

        if user_id not in CARTS:
            return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)

        cart = CARTS[user_id]
        total = cart.total

        # Apply discount if code is valid
        discount_applied = 0
        if discount_code:
            for code in DISCOUNT_CODES:
                if code.code == discount_code and not code.used:
                    discount_applied = total * 0.10
                    total -= discount_applied
                    code.used = True
                    break

        # Save order
        ORDERS.append({
            "user_id": user_id,
            "items": cart.items,
            "total_amount": total,
            "discount_applied": discount_applied,
            "timestamp": datetime.now()
        })

        # Clear cart
        del CARTS[user_id]

        return Response({
            "message": "Order placed successfully.",
            "order_summary": {
                "total_amount": total,
                "discount_applied": discount_applied,
                "items": cart.items
            }
        })

class GenerateDiscountView(APIView):
    def post(self, request):
        nth_order = request.data.get('nth_order')

        if not nth_order or not isinstance(nth_order, int):
            return Response({"error": "Invalid nth_order value."}, status=status.HTTP_400_BAD_REQUEST)

        code = generate_discount_code(nth_order)

        return Response({
            "message": "Discount code generated.",
            "code": code,
            "nth_order": nth_order
        })

class AnalyticsView(APIView):
    def get(self, request):
        total_items_sold = sum([len(order['items']) for order in ORDERS])
        total_revenue = sum([order['total_amount'] for order in ORDERS])
        total_discount_amount = sum([order['discount_applied'] for order in ORDERS])
        discount_codes = [{"code": code.code, "used": code.used} for code in DISCOUNT_CODES]

        return Response({
            "total_items_sold": total_items_sold,
            "total_revenue": total_revenue,
            "discount_codes": discount_codes,
            "total_discount_amount": total_discount_amount
        })
