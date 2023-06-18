class Cellphone:

    def __init__(self, manufacturer, model, price):
        self.__manufacturer = manufacturer
        self.__model = model
        self.__price = price

    # Mutators

    def set_manufacturer(self, manufacturer):
        self.__manufacturer = manufacturer

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        self.__price = price

    # Accessors for manufacturer, model, and retail price.
    def get_manufacturer(self):
        return self.__manufacturer

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__price
