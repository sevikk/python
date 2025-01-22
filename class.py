# Классы это шаблоны для обьектов
# из них можно создавать экземпляры

class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("car stopped")


my_car = Car()
second_car = Car()
# print(my_car == second_car)
# print(type(my_car))
# print(isinstance(my_car, Car))

# Car.move(my_car)

# my_car.move()
# my_car.stop()


class Comment:
    total_comments = 0

    def __init__(self, text):  # constructor
        self.text = text
        self.votes_qty = 0
        Comment.total_comments += 1

    def __add__(self, other):
        return (f"{self.text} {other.text}", self.votes_qty + other.votes_qty)
    
    def __eq__(self, other):
        return True if (self.text == other.text) and (self.votes_qty == other.votes_qty) else False

    def upvote(self, value):
        self.votes_qty += value

    @staticmethod
    def merge(first, second): # no self, no access to attributes
        return F"{first} - {second}"


comment = Comment("text here")
comment.upvote(2)
# comment.upvote(2)


comment1 = Comment("text here")
comment1.upvote(2)

print(comment == comment1)
print(comment.votes_qty, comment1.votes_qty)
print(id(comment), id(comment1))


# test = comment.merge("Great", "ok")
# print(test)
# comment.upvote = 10
# comment.upvote(2)


