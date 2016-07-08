#based on the pseudo-code in the video Binary Search from CS50 on Youtube
def bubble_sort(array):
    unsorted = True
    while unsorted:
        swap = 0
        print(array)
        for i in range(0,len(array)-1):
            if array[i+1] < array[i]:
                array[i],array[i+1] = array[i+1], array[i]
                swap += 1
        if swap == 0:
            unsorted = False

    return array

def main():
    sortedArray = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 306]
    unsortedArray = [13, 5, 3, 34, 0, 2, 55, 1, 306, 233, 89, 8, 21, 144]
    print('sorted array:')
    print(sortedArray)
    print('unsorted array:')
    print(bubble_sort(unsortedArray))

if __name__ == "__main__":
    main()
