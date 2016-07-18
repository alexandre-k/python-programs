import os

def get_files(folder):
    for item in os.listdir(folder):
        full_item= os.path.join(folder, item)
        if os.path.isfile(full_item):
            yield full_item
        if os.path.isdir(full_item):
            yield from get_files(full_item) # recursive use of yield with from

root_dir = '/home/mengzhi'

files = get_files(root_dir)
for f in files:
    print(f)

