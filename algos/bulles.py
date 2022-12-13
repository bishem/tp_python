from __future__ import annotations

from lists.fonctions import random_numbers


def minimum_at(pool: list[int | float]):
  minimum = pool[0]
  for element in pool[1:]:
    if element < minimum:
      minimum = element

  return pool.index(minimum)


def bubble_sort(pool: list[int | float]):
  for scope in range(len(pool)-1, 0, -1):
    sorted = True
    for cursor in range(scope):
      if pool[cursor] > pool[cursor+1]:
        pool[cursor], pool[cursor+1] = pool[cursor+1], pool[cursor]
        sorted = False
    if sorted:
      break

  return pool


def ordered_search(probe: int | float, ordered: list[int | float]):
  if not ordered:
    return 0

  if probe > ordered[len(ordered)-1]:
    # why is it not resulting in out of bound in insert sort ?
    return len(ordered)

  for element in ordered:
    if probe <= element:
      return ordered.index(element)


def extraction_sort(pool: list[int | float]):
  minimum = pool[minimum_at(pool)]
  pool.remove(minimum)

  if pool:
    return [minimum, *extraction_sort(pool)]
  else:
    return [minimum]


def basic_dichotomy(hole: list, alice, inside=False):
  """recursive dichotomous search algorithm for unordered list

  Args:
      hole (list): list in which to search
      alice (_type_): value to search
      inside (bool, optional): makes possible to know when to return the index of the target if it exists. Defaults to False.

  changing the inside argument will break the algorithm

  Returns:
      _type_: the index of the target if found or nothing otherwise
  """

  half_length = len(hole) // 2

  if not hole:
    return None

  if (len(hole) == 1) and hole[0] == alice:
    return hole[0]

  for rabbit in hole[:half_length]:
    if (alice == rabbit) and not inside:
      return hole.index(rabbit)
    if (alice == rabbit):
      return rabbit

  rabbit = basic_dichotomy(hole[half_length:], alice, inside=True)

  if inside:
    return rabbit
  else:
    return hole.index(rabbit)


def ordered_dichotomy(hole: list[int | float], alice: int | float, inside=False):
  """recursive dichotomous search algorithm for list of numbers

  Args:
      hole (list): list in which to search
      alice (_type_): value to search
      inside (bool, optional): makes it possible to know when to return the index. Defaults to False.

  changing the inside argument will break the algorithm

  Returns:
      _type_: the index of the target if found or nothing otherwise
  """
  ordered = hole

  half_length = len(ordered) // 2

  if not inside:
    ordered = extraction_sort(hole.copy())

  if not ordered:
    return None

  if (len(ordered) == 1) and ordered[0] == alice:
    return ordered[0]

  if alice < ordered[half_length]:
    rabbit = ordered_dichotomy(ordered[:half_length], alice, inside=True)
  else:
    rabbit = ordered_dichotomy(ordered[half_length:], alice, inside=True)

  if inside:
    return rabbit
  else:
    return hole.index(rabbit)


def inserting(probe: int | float, ordered: list[int | float]):
  cursor = ordered_search(probe, ordered)

  # my theory is that if i try spliting the table at the last value
  # this syntax does not allow it unless shenannigans
  left = ordered[:cursor]
  right = ordered[cursor:]

  return [*left, probe, *right]


def insertion_sort(pool: list[int | float]):
  if pool:
    return inserting(pool[0], insertion_sort(pool[1:]))
  else:
    return pool


def main():
  size = 10
  floor = 0
  of_type = int

  ceil = size**2
  numbers = random_numbers(size, floor, ceil, of_type)
  probe = numbers[minimum_at(numbers)]

  print(
      f'subject list {numbers}',
      f'minimux at index {minimum_at(numbers)}',
      f'bubble sort {bubble_sort(numbers.copy())}',
      f'dichotomy {probe} {ordered_dichotomy(numbers, probe)}',
      f'insert {probe} {inserting(probe, bubble_sort(numbers.copy()))}',
      f'extraction sort {extraction_sort(numbers.copy())}',
      f'insertion sort {insertion_sort(numbers.copy())}',
      sep='\n')


if __name__ == '__main__':
  main()
