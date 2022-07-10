from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        """Функция, выводящая все дни проката фильма"""
        for i in range(len(self.dates)):
            delta = self.dates[i][1] - self.dates[i][0]
            for j in range(delta.days + 1):
                yield self.dates[i][0] + timedelta(days=j)


if __name__ == '__main__':
    m = Movie('sw', [
        (datetime(2020, 1, 1), datetime(2020, 1, 7)),
        (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])
    for d in m.schedule():
        print(d)
