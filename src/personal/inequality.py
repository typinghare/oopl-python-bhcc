# How inequality forms?
import math
from random import random
from typing import List
from typing import Callable


class Person:
    def __init__(self, _id: int, asset: float):
        self.id = _id
        self.asset: float = asset

    def __repr__(self):
        return f"({self.id}, {self.asset})"


def inequality(
    numPeople: int,
    asset: float,
    amount: float,
    times: int,
    simulation_func: Callable[[List[Person], float], None],
):
    """
    :param numPeople: The number of people.
    :param asset: The initial asset of each person.
    :param amount: The amount of money to transfer in each simulation.
    :param times: The number of simulations.
    :param simulation_func:
    :return:
    """
    person_list: List[Person] = [Person(i, asset) for i in range(numPeople)]

    for i in range(times):
        simulation_func(person_list, amount)

    person_list.sort(key=lambda person: person.asset, reverse=True)
    print(person_list)


def simulate(personList: List[Person], amount: float):
    """
    Conducts a round of simulations.
    """
    num_people = len(personList)
    for i in range(num_people):
        person1 = personList[i]
        person2 = personList[rand(0, num_people)]
        transfer(person1, person2, amount)


def simulate_random(personList: List[Person], amount: float):
    num_people = len(personList)
    for i in range(num_people):
        person1 = personList[rand(0, num_people)]
        person2 = personList[rand(0, num_people)]
        transfer(person1, person2, amount)


def rand(lower: int, upper: int):
    return math.floor(random() * (upper - lower)) + lower


def transfer(person1: Person, person2: Person, amount: float):
    person1.asset -= amount
    person2.asset += amount


inequality(100, 1000, 3, 10000, simulate)
inequality(100, 1000, 3, 10000, simulate_random)
