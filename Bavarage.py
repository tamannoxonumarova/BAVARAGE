import json


class Cards:
    def __init__(self):
        self.card_data = self.get_card()

    def get_card(self):
        try:
            with open("card_baza.json", "r") as f:
                card_data = json.load(f)
        except FileNotFoundError:
            with open("card_baza.json", "x") as f:
                card_data = []
                json.dump(card_data, f)
        return card_data

    def as_card(self, id: int, value: int):
        return {"id": id, 'value': value}

    def commitation(self):
        with open("card_baza.json", "w") as f:
            json.dump(self.card_data, f, indent=4)

    def add_cards(self, id: int, value: int):
        object_ad = self.as_card(id, value)
        self.card_data.append(object_ad)
        self.commitation()

    def get_cards_valur(self, id: int):
        for card in self.card_data:
            if card['id'] == id:
                return card['value']
        return -1

    def show_cards(self):
        print('Number | Value')
        for i in self.card_data:
            print(i['id'], '|', i['value'])

    def price(self, id: int, price: int):
        for card in self.card_data:
            if card['id'] == id and card['value'] >= price:
                return 1
        return -1

    def money(self, id: int, price: int):
        for card in self.card_data:
            if card['id'] == id and card['value'] >= price:
                card['value'] -= price
        self.commitation()


class Bavarage:
    def __init__(self):
        self.data = self.get_data()

    def get_data(self):
        try:
            with open("baza.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("baza.json", "x") as f:
                data = []
                json.dump(data, f)
        return data

    def as_dictin(self, name: str, price: int, count: int):
        return {"name": name.title(), "price": price, "count": count}

    def commit(self):
        with open("baza.json", "w") as f:
            json.dump(self.data, f, indent=4)

    def add_varages(self, name: str, price: int, count: int):
        object_ad = self.as_dictin(name, price, count)
        self.data.append(object_ad)
        self.commit()

    def show_bavarages(self):
        print("Name | Count")
        for bavarage in self.data:
            print(bavarage["name"], "|", bavarage["count"])

    def get_bavrage_price(self, name: str):
        name = name.title()
        for bavrage in self.data:
            if bavrage["name"] == name:
                return bavrage["price"]
        return -1

    def get_bavrage_count(self, name: str):
        name = name.title()
        for bavrage in self.data:
            if bavrage["name"] == name:
                return bavrage["count"]
        return -1

    def purchase_bavarage(self, name: str):
        print('Name | Money | Count')
        for bavrage in self.data:
            if bavrage["name"] == name:
                return f"{bavrage['name']} | {bavrage['price']} | {bavrage['count']}"

    def money_wisit(self, name: str, id: int):
        for bavarage in self.data:
            if bavarage["name"] == name:
                for card in Cards().card_data:
                    if card["id"] == id:
                        emal = Cards().price(id, bavarage['price'])
                        if emal != -1:
                            bavarage['count'] -= 1
                            Cards().money(id, bavarage['price'])
                        else:
                            return -1
        self.commit()


def menu():
    s = Cards()
    b = Bavarage()
    print("\n1. Bavarages")
    print("2. Cards")
    print("3. Bavarages count")
    print("4. Purchase")
    d = input('>')
    match d:
        case '1':
            print("\n1. Show Bavarages")
            print("2. Add Bavarage")
            print("3. Get Bavarages Price")
            c = input(">")
            match c:
                case "1":
                    b.show_bavarages()
                case "2":
                    name: str = input("Name: ")
                    price: int = int(input("Price: "))
                    count: int = int(input("Count: "))
                    b.add_varages(name, price, count)
                    print("Barage succecfully added\n")
                case "3":
                    name = input("Enter bavarage name: ")
                    price = b.get_bavrage_price(name)
                    if price != -1:
                        print("{} bravarage price {}".format(name.title(), price))
                    else:
                        print("No such bavrage")
        case "2":
            print("\n1. Show Cards")
            print("2. Add Cards")
            print("3. Get Cards Value")
            c = input(">")
            match c:
                case '1':
                    print(s.show_cards())
                case '2':
                    id: int = int(input('Enter a card number : '))
                    value: int = int(input('Enter a card value : '))
                    s.add_cards(id, value)
                    print("Card successfully added")

                case '3':
                    id: int = int(input('Enter a card number : '))
                    value = s.get_cards_valur(id)
                    if value != -1:
                        print('{} card value {}'.format(id, value))
                    else:
                        print('No such card')
        case '3':
            print("\n1. Get Bavarage Count")
            c = input(">")
            match c:
                case '1':
                    name = input("Enter bavarage name: ")
                    price = b.get_bavrage_count(name)
                    if price != -1:
                        print("{} bravarage count {}".format(name.title(), price))
                    else:
                        print("No such bavrage")
        case "4":
            print("\n1.Purchase Bavarage")
            c = input(">")
            match c:
                case "1":
                    name = input("Enter bavarage name: ").title()
                    price = b.get_bavrage_count(name)
                    if price != -1:
                        print(b.purchase_bavarage(name))
                        id: int = int(input('Enter a card number : '))
                        value = s.get_cards_valur(id)
                        if value != -1:
                            kil = b.money_wisit(name, id)
                            if kil != -1:
                                print('Succesfully purchase')
                            else:
                                print('No such money')
                        else:
                            print('No such card')
                    else:
                        print("No such bavrage")
    menu()

if __name__ == '__main__':
    menu()