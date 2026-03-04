import json

FILE = "contacts.json"


def load_contacts():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact(name, phone):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print("Kontakts pievienots")


def list_contacts():
    contacts = load_contacts()
    for c in contacts:
        print(c["name"], "-", c["phone"])


def search_contact(name):
    contacts = load_contacts()
    for c in contacts:
        if c["name"].lower() == name.lower():
            print(c["name"], "-", c["phone"])


def main():
    while True:
        command = input("Komanda (add/list/search/quit): ")

        if command == "add":
            name = input("Vārds: ")
            phone = input("Telefons: ")
            add_contact(name, phone)

        elif command == "list":
            list_contacts()

        elif command == "search":
            name = input("Vārds: ")
            search_contact(name)

        elif command == "quit":
            break


if __name__ == "__main__":
    main()