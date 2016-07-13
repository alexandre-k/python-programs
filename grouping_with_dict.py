from collections import defaultdict

switches = ['mgt01', 'mgt02']


grouping = {}
for switch in switches:
    if switch not in grouping:
        grouping[switch] = []
    grouping[switch].append('f0/1')

yet_another_grouping = defaultdict(list)
for switch in switches:
    if switch not in yet_another_grouping:
        yet_another_grouping[switch].append('fa0/1')

print(grouping)
print(yet_another_grouping)
