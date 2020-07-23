import random


class Robot:
    population = 0
    Army_1 = []
    Army_2 = []

    def __init__(self, name, health, defense=0, attack=0, status='Alive', hit=0):
        self.name = name
        self.health = health
        self.defense = defense
        self.attack = attack
        self.status = status
        self.hit = hit
        Robot.population += 1
        if random.uniform(0, 1) > random.uniform(0.5, 0.5):
            Robot.Army_1.append(self)
        else:
            Robot.Army_2.append(self)

    def __sub__(self, other):
        self.hit = round(random.uniform(self.attack - 25, self.attack + 25))
        if other.defense - self.hit < 0:
            if other.defense - self.hit + other.health <= 0:
                other.health = 0
                other.defense = 0
                other.status = 'Dead'
                Robot.population -= 1
            else:
                other.health = other.defense - self.hit + other.health
                other.defense = 0

        else:
            other.defense = other.defense - self.hit

        print(self, 'Attacked for ', self.hit, ' ', other)
        print(other, ' Current defense points', other.defense)
        print(other, ' Current Health points', other.health)
        return ' '

    def get_parameters(self):
        pass
        return self.health, self.defense, self.attack, self.status


class RobotHeavy(Robot):
    def __init__(self, name, health):
        Robot.__init__(self, name, health)
        self.defense = 100
        self.attack = 125


class RobotEasy(Robot):
    def __init__(self, name, health):
        Robot.__init__(self, name, health)
        self.defense = 50
        self.attack = 75


t32_1 = RobotEasy('t32_1', 750)
t34_1 = RobotHeavy('t32_1', 1000)
t32_2 = RobotEasy('t32_2', 750)
t34_2 = RobotHeavy('t32_2', 1000)
t32_3 = RobotEasy('t32_3', 750)
t34_3 = RobotHeavy('t32_3', 1000)
t32_4 = RobotEasy('t32_4', 750)
t34_4 = RobotHeavy('t32_4', 1000)
t32_5 = RobotEasy('t32_5', 750)
t34_5 = RobotHeavy('t32_5', 1000)
t32_6 = RobotEasy('t32_6', 750)
t34_6 = RobotHeavy('t32_6', 1000)
t32_7 = RobotEasy('t32_7', 750)
t34_7 = RobotHeavy('t32_7', 1000)
t32_8 = RobotEasy('t32_8', 750)
t34_8 = RobotHeavy('t32_8', 1000)
t32_9 = RobotEasy('t32_9', 750)
t34_9 = RobotHeavy('t32_9', 1000)
t32_10 = RobotEasy('t32_10', 750)
t34_10 = RobotHeavy('t32_10', 1000)
print(Robot.population)


print(len(Robot.Army_1))
print(len(Robot.Army_2))

Fights = 0

while Robot.population > 0:
    list1 = random.sample(Robot.Army_1, 1)
    list2 = random.sample(Robot.Army_2, 1)
    list1[0] - list2[0]
    print(Robot.population)
    Fights += 1

print(Fights)
