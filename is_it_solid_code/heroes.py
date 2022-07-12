from antagonistfinder import AntagonistFinder
from random import randint


class Guns:

    def fire_a_gun(self):
        print('PIU PIU')


class Punches:

    def right_hook(self):
        print('Right punch')

    def left_hook(self):
        print('left punch')

    def roundhouse_kick(self):
        print('Bump')


class SuperHero(Guns, Punches):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def arbitrary_ultimate(self):
        print('Baaaaaaang!')

    def attack(self):
        type_attack = randint(1, 4)
        match type_attack:
            case 1:
                self.fire_a_gun()
            case 2:
                self.right_hook()
            case 3:
                self.left_hook()
            case 4:
                self.roundhouse_kick()

    def ultimate(self):
        self.arbitrary_ultimate()


class Batman(SuperHero):

    def __init__(self):
        super(Batman, self).__init__('Bruce Wayne', True)

    def throw_a_batarang(self):
        print('Fruuuuwww!')

    def ultimate(self):
        self.throw_a_batarang()


class WonderWoman(SuperHero):

    def __init__(self):
        super(WonderWoman, self).__init__('Diana Prince', True)

    def use_zeus_bracelets(self):
        print('Scccrrruuushhh!')

    def ultimate(self):
        self.use_zeus_bracelets()


class Superman(SuperHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def incinerate_with_lasers(self):
        print('Wzzzuuuup!')

    def ultimate(self):
        self.incinerate_with_lasers()

