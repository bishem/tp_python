from __future__ import annotations
from typing import Any, Callable

import random
import time


def execution_time(function: Callable, *args):
  """recupere le temps d'execution et la valeur retour d'une fonction

  Args:
      function (Callable): la fonction a chronometrer
      agrs: les arguments de la fonction a chronometrer

  Returns:
      tuple[float, Unknown]: le temps d'execution de la fonction et sa valeur retour
  """

  start = time.time()
  returned = function(*args)
  return (time.time() - start, returned)


def custom_sum(numbers: list[int | float]):
  accumulator = 0
  for number in numbers:
    accumulator += number
  return accumulator


def average_of(numbers: list[int | float]):
  return custom_sum(numbers) / len(numbers)


def random_numbers(size: int, floor: int, ceil: int, of_type: type[int | float]):
  """generates a random list of numbers matching the given parameters

  Args:
      size (int): the size of the list
      floor (int): the tiniest possible number of the list
      ceil (int): the biggest possible number of the list
      of_type (type[int  |  float]): the type of elements generated

  Returns:
      list[int | float]: the generated list of numbers
  """

  pool = range(size)
  sink: list[int | float] = []
  for _ in pool:
    sink.append(random_number(floor, ceil, of_type))
  return sink


def random_number(floor: int, ceil: int, of_type: type[int | float]):
  integer = random.randint(floor, ceil)
  return integer if of_type is int else random.random()*integer


def filtered_by(pool: list, discriminator=None, of_type: type | None = None):
  """decorator returning filtered list by the provided simplified parameters

  Args:
      pool (list): the list to by filtered
      discriminator (_type_, optional): used to get list element not matching it. Defaults to None.
      of_type (type | None, optional): if provided override the probe to get list of matching type. Defaults to None.

  Returns:
      list: filtered list
  """

  return list(filter(lambda element: of_type == type(element) if of_type else element != discriminator, pool))


def exists_in(probe, pool: list):
  return len(pool) != len(filtered_by(pool, discriminator=probe))


def amount_in(probe, pool: list):
  return len(pool) - len(filtered_by(pool.copy(), discriminator=probe))


def over_or_equal_in(floor: int | float, pool: list[float | int]):
  return list(filter(lambda element: element > floor, pool.copy()))


def max_in(pool: list[float | int]):
  """gets the maximum value of any given list of number

  will raise an error if the list is empty

  Args:
      pool (list[float  |  int]): the list of numbers to get the maximum from

  Returns:
      float  |  int: the maximum value of any given list of numbers
  """

  clone = pool.copy()
  clone.sort(reverse=True)
  return clone[0]


def shuffled(pool: list):
  """wrapper that actually return the list being shuffled

  Args:
      pool (list): list of values to shuffle

  Returns:
      list: the shuffled list
  """

  random.shuffle(pool)
  return pool


def main():

  list_of_any: list = [0, 14, 'one', 'two', 2, 30, 3, 3, 3, 3, 31, 3, 3, True, 305, 3, 3, 39, 3,
                       4, 5444, 'X marks the spot', 647864, 7, 'banana', 8, 9]

  print(
      f"moyenne des elements d'une liste de nombre: {average_of(random_numbers(10, 0, 10**2, float))}",
      f"nombre d'element 3 dans liste: {amount_in(3, list_of_any)}",
      f"nombe element excedant 10 dans liste: {len(over_or_equal_in(9, filtered_by(list_of_any, of_type=int)))}",
      f"valeur max d'une liste de nombre: {max_in(filtered_by(list_of_any, of_type=int))}",
      f"valeur 'one' existe dans liste: {exists_in('one', list_of_any)}",
      f"liste de 10 entier: {random_numbers(10, 0, 10**2, int)}",
      f"liste des 10 premier entier melangé: {shuffled(list(range(10)))}",
      f"temps generation liste 1000000 entier: {execution_time(random_numbers, 1000000, 0, 1000000**2, int)[0]}",
      f"temps generation liste 1000000 premier entier melangé: {execution_time(random.shuffle, list(range(1000000)))[0]}",
      sep="\n")


if __name__ == '__main__':
  main()
