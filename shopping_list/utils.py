def item_total(quantity, price):
    return quantity * price


def calculate_total(items):
    total = 0
    for item in items:
        total += item["quantity"] * item["price"]
    return total


def count_items(items):
    total = 0
    for item in items:
        total += item["quantity"]
    return total   