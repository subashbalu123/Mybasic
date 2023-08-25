class GFG:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def show(self):
        print("Hello my name is " + self.name + " and my" +
              " city " + self.city + ".")


obj = GFG("John", "Trichy")
obj.show()
