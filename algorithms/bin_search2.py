#based on the pseudo-code in the video Binary Search from CS50 on Youtube
def binary_search(key, array):
    if len(array) == 0:
        return False
    else:
        midpoint = len(array) // 2
    if array[midpoint] < key:
        return binary_search(key, array[midpoint+1:])
    elif array[midpoint] > key:
        return binary_search(key, array[:midpoint-1])
    else:
        return array[midpoint]

def main():
    array = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 306]
    midpoint=binary_search(144, array)
    print(midpoint)

if __name__ == "__main__":
    main()
