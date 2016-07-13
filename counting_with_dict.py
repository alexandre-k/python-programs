#Taken from transforming code into beautiful, idiomatic python
import simplejson as json
from collections import defaultdict
colors = ['red', 'green', 'red', 'blue', 'yellow', 'blue' ]

counter = {}
for color in colors:
    if color not in counter:
        counter[color] = 0
    counter[color] += 1

simplified_counter = {}
for color in colors:
    simplified_counter[color] = simplified_counter.get(color, 0) + 1


yet_another_counter = defaultdict(int)
for color in colors:
    yet_another_counter[color] += 1

print(colors)
print(json.dumps(counter, indent=4))
print(json.dumps(simplified_counter, indent=4))
print(json.dumps(yet_another_counter, indent=4))
