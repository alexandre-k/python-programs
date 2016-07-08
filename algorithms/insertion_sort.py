#based on the video from CS50 on Youtube
def insertion_sort(unsorted):
    sorted =[]
    for to_left in range(1,len(unsorted)-1):
        unsorted_element = sorted[to_left]
        index_unsorted = to_left
        while sorted[index_unsorted-1] > unsorted_element and index_unsorted > 0:
            sorted[index_unsorted] = sorted[index_unsorted - 1]
            index_unsorted = index_unsorted - 1
        sorted[index_unsorted] = unsorted_element
    return unsorted

def main():
    sortedArray = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 306]
    unsortedArray = [13, 5, 3, 34, 0, 2, 55, 1, 306, 233, 89, 8, 21, 144]
    print('sorted array:')
    print(sortedArray)
    print('unsorted array:')
    print(insertion_sort(unsortedArray))

if __name__ == "__main__":
    main()
