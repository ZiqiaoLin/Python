class Animal:
    noise = "Grunt"
    size = "Large"
    color = "Brown"
    hair = 'Covers body'

    def get_color(self,abc):
        return self.color + " " + abc
    @property
    def make_noise(self):
        return self.noise

    def some_func(arg_1,arg_2,arg_3):
        pass




class Dog(Animal):
    name = "Jon"
    #color = 'brwon'

    #def get_color(self):
        #return self.color


obj = Dog()
print("---------------------")
print(obj.get_color("Red"))
print("---------------------")
print(obj.hair)
print(obj.make_noise())
print("---------------------")
print(obj.make_noise)
print("*********************")
print(obj.make_noise())