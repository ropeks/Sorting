"""

STEPS:
1. While your data set contains more than one item, split it in half
2. Once you have gotten down to a single element, you have also *sorted* that element 
   (a single element cannot be "out of order")
3. Start merging your single lists of one element together into larger, sorted sets
4. Repeat step 3 until the entire data set has been reassembled

arr = [8, 3, 6, 4, 7, 9, 5, 2, 1]
arr_wannabe = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lhs, rhs = [8, 3, 6, 4, 7], [9, 5, 2, 1]

[lhs call]
[8, 3, 6, 4, 7]
lhs, rhs = [8, 3, 6], [4, 7]

[lhs2 call]
[8, 3, 6]
lhs, rhs = [8, 3], [6]

[lhs3 call]
[8, 3]
lhs, rhs = [8], [3]

"""

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merger( arr1, arr2 ):
    elements = len( arr1 ) + len( arr2 )
    merged_arr = [0] * elements
    a, b = 0, 0
    for i in range(0, elements):
        if a >= len(arr1):
            merged_arr[i] = arr2[b]
            b += 1
        elif b >= len(arr2):
            merged_arr[i] = arr1[a]
            a += 1
        elif arr1[a] < arr2[b]:
            merged_arr[i] = arr1[a]
            a += 1
        else:
            merged_arr[i] = arr2[b]
            b += 1
    return merged_arr



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1:
        a = merge_sort(arr[:len(arr)//2])
        b = merge_sort(arr[len(arr)//2:])
        arr = merger(a, b)
    return arr

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
