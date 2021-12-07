class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

    def hit(self, rank):
        rank.loss(self.attack)

    def damage(self, attack):
        return attack

    def loss(self, attack):
        self.health -= self.damage(attack)

class Knight(Warrior):
    def __init__(self):
        super().__init__(attack=7)

class Defender(Warrior):
    def __init__(self):
        super().__init__(health=60, attack=3)
        self.defense = 2

    def damage(self, attack):
        return max(0, attack - self.defense)


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_1.hit(unit_2)
        if unit_2.is_alive:
            unit_2.hit(unit_1)
    return unit_1.is_alive


class Army:
    def __init__(self):
        self.composition = []

    @property
    def is_alive(self):
        return bool(self.composition)

    @property
    def frontline(self):
        return self.composition[0]

    def add_units(self, rank, number):
        [self.composition.append(rank()) for i in range(number)]

    def get_damage(self):
        return self.composition.pop(0)


class Battle:

    def fight(self, army_1, army_2):
        while army_1.is_alive and army_2.is_alive:
            fight(army_1.frontline, army_2.frontline)
            if army_1.frontline.is_alive:
                army_2.get_damage()
            else:
                army_1.get_damage()
        return army_1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")

