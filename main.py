from __future__ import annotations
import requests
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class Starship(BaseModel):
    name: str
    model: str
    manufacturer: str
    cost_in_credits: str
    length: str
    max_atmosphering_speed: str
    crew: str
    passengers: str
    cargo_capacity: str
    consumables: str
    hyperdrive_rating: str
    MGLT: str
    starship_class: str
    pilots: List[str] = []
    films: List[str] = []
    created: datetime
    edited: datetime
    url: str

    def __str__(self):
        return str(self.__dict__)


class StarshipsDto(BaseModel):
    count: int
    next: Optional[str] = None
    previous: Optional[str] = None
    results: List[Starship] = []


def sort_starships(starwarship):
    try:
        return float(starwarship.hyperdrive_rating)
    except:
        return 0.0


def main():

    response = requests.get('https://swapi.dev/api/starships/')
    starships = []
    while (response.json()['next'] is not None):

        starships_dto_response = StarshipsDto(**(response.json()))
        starships.extend(starships_dto_response.results)
        response = requests.get(starships_dto_response.next)

    starships_dto_response = StarshipsDto(**(response.json()))
    starships.extend(starships_dto_response.results)

    starships.sort(reverse=True, key=sort_starships)
    for i in range(len(starships)):
        print(starships[i])


if __name__ == "__main__":
    main()
