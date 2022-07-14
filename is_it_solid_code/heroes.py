from antagonistfinder import AntagonistFinder


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


class SuperHero:

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def type_ultimate(self):
        print('Baaaaaaang!')

    def attack(self):
        print('Kick')

    def find(self, place):
        self.finder.get_antagonist(place)

    def ultimate(self):
        self.type_ultimate()


class Batman(SuperHero, Punches):

    def __init__(self):
        super(Batman, self).__init__('Bruce Wayne', False)

    def attack(self):
        self.roundhouse_kick()


class WonderWoman(SuperHero, Punches):

    def __init__(self):
        super(WonderWoman, self).__init__('Diana Prince', True)

    def attack(self):
        self.right_hook()

    def type_ultimate(self):
        print('Scccrrruuushhh!')


class Superman(SuperHero, Punches):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        self.left_hook()

    def type_ultimate(self):
        print('Wzzzuuuup!')
