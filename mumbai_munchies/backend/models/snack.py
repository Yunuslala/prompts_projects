class Snack:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability

    @staticmethod
    def from_dict(data):
        return Snack(data['name'], data['price'], data['availability'])

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'availability': self.availability
        }
