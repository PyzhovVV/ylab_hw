from typing import Union
from heroes import Superman, SuperHero, WonderWoman, Batman
from places import Kostroma, Tokyo, NewYork
from make_news import TV, Newspaper


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo, NewYork], news):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    news.create_news(hero, place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), TV())
    print('-' * 20)
    save_the_place(SuperHero('Chack Norris', False), Tokyo(), Newspaper())
    print('-' * 20)
    save_the_place(WonderWoman(), NewYork(), TV())
    print('-' * 20)
    save_the_place(Batman(), NewYork(), Newspaper())
