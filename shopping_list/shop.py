import sys
from storage import load_list, save_list
from utils import item_total, calculate_total, count_items


def add_item(name, quantity, price):
    items = load_list()

    items.append({
        "name": name,
        "quantity": int(quantity),
        "price": float(price)
    })

    save_list(items)
    print(f"✓ Pievienots: {name} ({quantity} x {price} EUR)")


def list_items():
    items = load_list()

    if not items:
        print("Saraksts ir tukšs")
        return

    print("Iepirkumu saraksts:")

    for i, item in enumerate(items, start=1):
        total = item_total(item["quantity"], item["price"])
        print(f"{i}. {item['name']} ({item['quantity']} x {item['price']} EUR) = {total:.2f} EUR")


def total_items():
    items = load_list()

    total_price = calculate_total(items)
    total_products = count_items(items)

    print(f"Kopā produkti: {total_products}")
    print(f"Kopējā summa: {total_price:.2f} EUR")


def clear_items():
    save_list([])
    print("Saraksts iztīrīts")


def main():
    if len(sys.argv) < 2:
        print("Komandas:")
        print(" add NAME QUANTITY PRICE")
        print(" list")
        print(" total")
        print(" clear")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 5:
            print("Lietošana: add NAME QUANTITY PRICE")
            return

        name = sys.argv[2]
        quantity = sys.argv[3]
        price = sys.argv[4]

        add_item(name, quantity, price)

    elif command == "list":
        list_items()

    elif command == "total":
        total_items()

    elif command == "clear":
        clear_items()

    else:
        print("Nezināma komanda")


if __name__ == "__main__":
    main()