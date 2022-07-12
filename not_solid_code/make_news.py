class TV:

    def create_news(self, hero, place):
        hero_name = getattr(hero, 'name', 'some good guy')
        place_name = getattr(place, 'city_name', 'place')
        print(f'TV announced: {hero_name} saved the {place_name}!')


class Newspaper:

    def create_news(self, hero, place):
        hero_name = getattr(hero, 'name', 'some good guy')
        place_name = getattr(place, 'city_name', 'place')
        print(f'newspapers wrote: {hero_name} saved the {place_name}!')
