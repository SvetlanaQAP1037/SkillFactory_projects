class Cat:
    def __init__(self, name, gender, age=0):
        self.name = name
        self.gender = gender
        self.age = age
    def get_card_cat(self):
        return f"Имя: {self.name}, Пол: {self.gender}, Возраст: {self.age}"

