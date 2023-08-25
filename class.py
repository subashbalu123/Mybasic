class GFG:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def show(self):
        print("Hello my name is " + self.name + " and " +
              " city " + self.city + ".")


obj = GFG("subash", "trichy")
obj.show()