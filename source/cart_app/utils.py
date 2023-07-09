# Returns the total sum for items in cart.
def counting_total_for_cart_items(cart: dict):
    total = 0
    for item_id, item in cart.items():
        total += float(item['price']) * float(item['quantity'])
    return total
