class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

class AdminUser(User):
    def __init__(self, username: str, email: str, role: str):
        super().__init__(username, email)
        self.role = role
        self.is_admin = True

admin = AdminUser("admin", "test@test.com", "admin")

# print(admin.__dict__)

class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author

class Forum:
    def __init__(self):
        self.posts = []
        self.users = []

    def register_user(self, username: str, email: str):
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, title: str, content: str, author: User):
        post = Post(title, content, author)
        self.posts.append(post)
        return post

    def find_user_by_username(self, username: str):
        for user in self.users:
            if user.username == username:
                return user

    def find_user_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user

    def find_post_by_user(self, author: User):
        found_posts = []
        for post in self.posts:
            if post.author == author:
                found_posts.append(post)
        return found_posts


forum = Forum()
user1= forum.register_user("Seva", "email1")
user2 = forum.register_user("Author", "<EMAIL>")
# print(forum.users[0].__dict__)

forum.create_post("My first post", "content", user1)
forum.create_post("Second post", "content 2", user1)
forum.create_post("First post", "content", user2)
# print(forum.posts[1].title)
#
# print(forum.find_user_by_username("Seva111")) # None
# print(forum.find_user_by_username("Seva").username)
# print(forum.find_user_by_username("Seva").__dict__)

# print(forum.find_post_by_user(user1))

# Find user bt email and show user posts:
found_user = forum.find_user_by_email("email1")
if found_user:
    print(forum.find_post_by_user(found_user))
else:
    print("No user")


# Encapsulation aтрибут
# Атрибуты управляются только внутри класса и их методов
class Email:
    def __init__(self, sender: str, recipient: str, subject: str, body: str):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def send_email(self):
        pass

    def read_email(self):
        pass

# Inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        pass

    def stop(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, doors_qty):
        super().__init__(make, model)
        self.doors_qty = doors_qty

    def lock_doors(self):
        pass

    def unlock_doors(self):
        pass

# Polyforphism
# Возможность использовать один и тот же метод для объектов разных типов, и при этом метод будет выполняться специфично для каждого типа.
import math
class Shape:
    def calc_area(self): # - Polyforphism
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self): # - Polyforphism
        # return math.pi * self.radius * self.radius
        # return math.pi * self.radius ** 2
        return math.pi * pow(self.radius, 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self): # - Polyforphism
        return self.width * self.height


shape1 = [Circle(2), Rectangle(4, 5)]

# for shape in shape1:
    # print(shape.calc_area())

# Abstraction
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def process_payment(self): pass


class CreaditCatPayment(Payment):
    def process_payment(self): pass


class StripPayment(Payment):
    def process_payment(self): pass

class PayPalPayment(Payment):
    def process_payment(self): pass




