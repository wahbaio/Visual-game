class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_name(self, item_name):
        self.name = item_name

    def set_description(self, item_description):
        self.description = item_description

    def describe_item(self):
        print(self.description)
