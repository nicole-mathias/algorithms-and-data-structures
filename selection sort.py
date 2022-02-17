# selection sort 2
# to sort numbers from smallest to highest

def findSmallest(arr):
    index = 0
    smallest_no = arr[index]

    for i in range(len(arr)):
        if(smallest_no > arr[i]):
            smallest_no = arr[i]
            index = i
    return index


def selectionSort(arr):
    sorted_arr = []

    for i in range(len(arr)):
        index = findSmallest(arr)
        sorted_arr.append(arr[index])
        arr.pop(index)
    print("sorted array:",sorted_arr)
    # print("arr:", arr)
    


array = [5,9,1,7,3]
selectionSort(array)
