import csv

class App:
    category_dict = {}
    rating_dict = {}
    price_dict = {}

    def __init__(self, ID, name, developer, description, price, rating, review_count, category):
        self.id = ID
        self.name = name
        self.developer = developer
        self.description = description
        self.price = '0' if price == "Free" else price
        self.rating = rating
        self.review_count = review_count
        self.category = category

        # Update the category, price, and rating dictionaries with the current app object
        App.category_dict.setdefault(self.category, []).append(self)
        App.price_dict.setdefault(int(float(self.price)), []).append(self)
        App.rating_dict.setdefault(int(float(self.rating)), []).append(self)

    def get_name(self):
        return self.name

    def get_rating(self):
        return self.rating

    def get_category(self):
        return self.category

    def get_price(self):
        return self.price

    def get_id(self):
        return self.id

    def get_developer(self):
        return self.developer

    def get_description(self):
        return self.description


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)


# Open the CSV file containing the top 50 Shopify apps
filename = 'Top50ShopifyApps.csv'
with open(filename, 'r', encoding='ISO-8859-1') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        app = App(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) 
