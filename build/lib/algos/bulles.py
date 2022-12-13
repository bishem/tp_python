from __future__ import annotations

from typing import Any
from ..lists.fonctions import random_numbers


import random


def index_minimum(tableau: list[int | float], left: int, right: int):
  """_summary_

  Args:
      tableau (list[int]): _description_
      left (int): _description_
      right (int): _description_

  Returns:
      _type_: _description_
  """

  return tableau[left] if tableau[left] < tableau[right] else tableau[right]


def bubble_sort(tableau: list[int | float]):
  """_summary_

  Args:
      tableau (list[int]): _description_
  """

  for scope in range(len(tableau)-1, 0, -1):
    sorted = True
    print(tableau)
    for cursor in range(scope):
      if tableau[cursor] > tableau[cursor+1]:
        tableau[cursor], tableau[cursor+1] = tableau[cursor+1], tableau[cursor]
        sorted = False
    if sorted:
      break


def search_matching_in(probe: int | float, tableau: list[int | float]):
  """_summary_

  Args:
      probe (int): _description_
      tableau (list[int]): _description_

  Returns:
      _type_: _description_
  """

  for element in tableau:
    if probe < element:
      return 'not in the list'
    if probe == element:
      return f'exists at index {tableau.index(element)} of list'


def search_with_dichotomy_matching_in(probe: int | float, tableau: list[int | float]):
  """_summary_

  Args:
      probe (int): _description_
      tableau (list[int]): _description_

  Returns:
      _type_: _description_
  """

  pool = tableau.copy()
  while len(pool) > 1:
    half_length = len(pool) // 2
    if probe < tableau[half_length]:
      pool = pool[:half_length]
    else:
      pool = pool[half_length:]
    print(pool)

  if probe is not pool[0]:
    return 'not in the list'
  else:
    return f'exists at index {tableau.index(pool[0])} of list'


def insert(element: int | float, tableau: list[int | float]):
  return


def main():
  numbers = random_numbers(10, 0, 10**2, int)

  print(index_minimum(numbers, 2, 8),
        search_with_dichotomy_matching_in(50, numbers))


if __name__ == '__main__':
  main()
