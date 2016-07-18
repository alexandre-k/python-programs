#Some code from Ned Batchelder

def give_func(myfile):
    for line in myfile:
        line = line.strip()
        if line.startswith('def'):
            yield line
        else:
            continue

with open('pycon_decorators.py') as myfile:
    for line in give_func(myfile):
        print(line)

#Breaking from 2 loops by making the double loop single:
def range_2d(width, height):
    for y in range(height):
        for x in range(width):
            yield x, y

# for col,row in range_2d(width, height):
#     value = spreadsheet.get_value(col, row)
#     do_something(value)

#     if this_is_my_value(value):
#         break

# Iterating cells
# for cell in sreadsheet.cells():
#     value = cell.get_value()
#     do_something(value)

#     if this_is_my_value(value):
#         break


class IpRange(object):
    def __init__(self, ip_max, ip_min):
        self.ip_max = ip_max
        self.ip_min = ip_min
        self.ip_range = self.ip_max - self.ip_min

    def __iter__(self):
        for ip in self.ip_range:
            if not ip.done:
                yield ip
    def all(self):
        return iter(self.ips)

    def done(self):
        return (ip for ip in self. ips if ip.done)

ips = IpRange(9, 4)

for ip in ips:
    print(ip)
