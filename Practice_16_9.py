#16.9.1
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f"Rectangle: {self.x}, {self.y}, {self.width}, {self.height}"

# 16.9.2
# class Rectangle:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b

# 16.9.3
# class Client:
#     def __init__(self, name, surname, city, balance):
#         self. name = name
#         self. surname = surname
#         self.city = city
#         self.balance = balance
#     def clients_info(self):
#         return f'"{self.name}{self.surname}. {self.city}. Баланс: {self.balance} руб."'
#
# client_1 = Client('Иван', 'Петров', 'Москва', 50)
# print(client_1.clients_info())

#16.9.4
# class Client:
#     def __init__(self, name, surname, city, balance):
#         self. name = name
#         self. surname = surname
#         self.city = city
#         self.balance = balance
#     def clients_info(self):
#         return f'"{self.name}{self.surname}. {self.city}. Баланс: {self.balance} руб."'
#     def clients_list(self):
#         return f'{self.name} {self.surname}, {self.city}'
#
# client_1 = Client('Иван', 'Петров', 'Москва', 50)
# client_2 = Client('Антон', 'Сидоров', 'Новгород', 60)
# client_3 = Client('Олег', 'Иванов', 'Суздаль', 40)
#
# clients = [client_1, client_2, client_3]
# for guest in clients:
#     print(guest.clients_list())

