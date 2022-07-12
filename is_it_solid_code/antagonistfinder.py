from abc import ABC, abstractmethod


class Place(ABC):

    @abstractmethod
    def get_antagonist(self, place):
        ...


class AntagonistFinder(Place):

    def get_antagonist(self, place):
        place.get_monster()
