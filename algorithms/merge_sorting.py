#based on the code in the video from Joe James on Youtube
def merge_sort(array):
    if len(array)>1:
        midpoint = len(array) // 2
        left_half = array[:midpoint]
        right_half = array[midpoint:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i<len(left_half) and j<len(right_half):
            print(array)
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i = i+1
            else:
                array[k] = right_half[j]
                j = j+1
            k = k+1

        while i<len(left_half):
            array[k] = left_half[i]
            i = i+1
            k = k+1

        while j<len(right_half):
            array[k] = right_half[j]
            j = j+1
            k = k+1

    return array

def main():
    sortedArray = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 306]
    unsortedArray = [13, 5, 3, 34, 0, 2, 55, 1, 306, 233, 89, 8, 21, 144]
    print('sorted array:')
    print(sortedArray)
    print('unsorted array:')
    print(merge_sort(unsortedArray))

if __name__ == "__main__":
    main()
