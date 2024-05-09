import random
from datetime import date
from random import choice
from faker import Faker
fake = Faker()


class Film:
    def __init__(self, tytuł, rok_wydania, gatunek, liczba_odtworzeń):
        self.tytuł = tytuł
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self.liczba_odtworzeń = liczba_odtworzeń

    def __str__(self):
        return f'{self.tytuł} {self.rok_wydania} {self.gatunek} {self.liczba_odtworzeń}'
    
    def __repr__(self):
        return f"Film(tytuł={self.tytuł}, rok_wydania={self.rok_wydania}, gatunek={self.gatunek}, " \
               f"liczba_odtworzeń={self.liczba_odtworzeń})"

    def play(self):
        print(f"{self.tytuł}, ({self.rok_wydania}).")
        self.liczba_odtworzeń += 1
        return self.liczba_odtworzeń


class Serial(Film):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def __str__(self):
        return f'{self.tytuł} {self.rok_wydania} {self.gatunek} {self.numer_odcinka} {self.numer_sezonu}' \
               f' {self.liczba_odtworzeń}'
    
    def __repr__(self):
        return f"Serial(tytuł={self.tytuł}, rok_wydania={self.rok_wydania}, gatunek={self.gatunek}, " \
               f"numer_odcinka={self.numer_odcinka}, numer_sezonu={self.numer_sezonu}, " \
               f"liczba_odtworzeń={self.liczba_odtworzeń})"

    def play(self):
        print(f"{self.tytuł}, S0{self.numer_sezonu}E0{self.numer_odcinka}.")
        self.liczba_odtworzeń += 1
        return self.liczba_odtworzeń


gatunek = ["Komedia", "Dramat", "Sensacja", "Horror", "Thriller", "Obyczajowy", "Biograficzny"]
biblioteka = []
today = date.today()


def get_movies():
    return sorted([film.tytuł for film in biblioteka if not isinstance(film, Serial)])


def get_series():
    return sorted([serial.tytuł for serial in biblioteka if isinstance(serial, Serial)])


def search():
    wyszukanie = str(input("Podaj tytuł jakiego szukasz: "))
    for element in biblioteka:
        if element.tytuł == wyszukanie:
            return element.tytuł


def generate_views():
    element = random.choice(biblioteka)
    element.liczba_odtworzeń += random.randint(1, 101)
    return element


def generate_views10(k=10):
    i = 0
    while i < k:
        generate_views()
        i += 1


def top_titles():
    top = sorted(biblioteka, key=lambda element: element.liczba_odtworzeń, reverse=True)
    return top[:3]


def create_biblioteka(type, how_many):
    for i in range(how_many):
        if type == "Film":
            biblioteka.append(Film(
                tytuł=fake.word().title(),
                rok_wydania=fake.year(),
                gatunek=choice(gatunek),
                liczba_odtworzeń=0
            ))
        elif type == "Serial":
            biblioteka.append(Serial(
                tytuł=fake.word().title(),
                rok_wydania=fake.year(),
                gatunek=choice(gatunek),
                numer_odcinka=fake.random_int(min=1, max=8),
                numer_sezonu=fake.random_int(min=1, max=3),
                liczba_odtworzeń=0
            ))


if __name__ == "__main__":
    print("Biblioteka filmów\n")
    create_biblioteka("Film", 3)
    create_biblioteka("Serial", 3)
    print(biblioteka, "\n")
    print(get_movies())
    print(get_series(), "\n")
    print(search(), "\n")
    generate_views()
    generate_views10()
    print(biblioteka, "\n")
    print(f"Najpopularniejsze filmy i seriale dnia {today.day}.{today.month}.{today.year}:")
    print(top_titles())
