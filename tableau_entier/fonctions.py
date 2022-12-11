import random
import time
from typing import Any


numbers: list[int] = list(range(10))
print(sum(numbers)/len(numbers))

sum: int = 0
for index in numbers:
    sum += index

average: float = sum / len(numbers)
print(average)


list_of_any: list[Any] = [0, 14, 'one', 'two', 2, 30, 3, 3, 3, 3, 31, 3, 3, 305, 3, 3, 39, 3,
                          4, 5444, 'X marks the spot', 647864, 7, 'banana', 8, 9]

subject = 3
accumulator = 0
for element in filter(lambda value: isinstance(value, type(subject)), list_of_any):
    if subject == element:
        accumulator += 1
print(accumulator)

subject = 3
accumulator = 0
for element in filter(lambda value: isinstance(value, type(subject)), list_of_any):
    if element >= 10:
        accumulator += 1
print(accumulator)

descriptor = 0
filtered = list(filter(lambda value: isinstance(
    value, type(descriptor)), list_of_any))

filtered.sort(reverse=True)
print(filtered)

max = filtered[0]
print(max)

subject = 'one'
existing = len(
    list(filter(lambda value: not (value == subject), list_of_any))) > 0
print(existing)

begin = time.time()

accumulator = []
limit = 100
pool = range(random.randint(0, limit)+1)
for _ in pool:
    accumulator.append(random.randint(0, limit))

print(accumulator)
random.shuffle(accumulator)
print(accumulator)

elapsed = time.time() - begin
print(elapsed)

begin = time.time()

subject = 42
existing = len(
    list(filter(lambda value: not (value == subject), accumulator))) > 0
print(existing)

elapsed = time.time() - begin
print(elapsed)
