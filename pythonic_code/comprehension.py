import collections
import uuid

Measurement = collections.namedtuple('Measurement', 'id x y value')

measurements = [
    Measurement(str(uuid.uuid4()), 1, 1, 72),
    Measurement(str(uuid.uuid4()), 2, 1, 40),
    Measurement(str(uuid.uuid4()), 3, 1, 11),
    Measurement(str(uuid.uuid4()), 3, 3, 90)
]

# C-style
high_measurements1 = []
for m in measurements:
    if m.value > 40:
        high_measurements1.append(m.value)
print(high_measurements1)

# List comprehension
high_measurements2 = [m.value for m in measurements if m.value > 40]
print(high_measurements2)

# Generator
high_measurements3 = (m.value for m in measurements if m.value > 40)
print(list(high_measurements3))

# dict comprehension
high_measurements4 = {m.id: m.value for m in measurements if m.value > 40}
print(high_measurements4)


# dict comprehension
high_measurements5 = {m.value for m in measurements if m.value > 40}
print(high_measurements5)
