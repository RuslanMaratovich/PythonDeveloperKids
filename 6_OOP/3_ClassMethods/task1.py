class Ship:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def go_swimming(self):
        print(f"{self.name} отправился в плаванье.")

    def how_many_people(self):
        print(f"На борту корабля '{self.name}' находится {self.people} человек.")

    def stop_ship(self, time):
        print(f"Корабль {self.name} кинул якорь на {time} часов.")

n1 = Ship('N1', 10)
n1.go_swimming()
n1.how_many_people()
n1.stop_ship(5)