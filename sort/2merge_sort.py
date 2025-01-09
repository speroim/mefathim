arr = [3, 1, 4, 2]

def merge_sort(array):
    if len(array) < 2:
        return array
    
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    i, j = 0, 0
    new_arr = []
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            new_arr.append(left[i])
            i += 1
        else:
            new_arr.append(right[j])
            j += 1
    
    new_arr.extend(left[i:])
    new_arr.extend(right[j:])
    
    return new_arr

sorted_array = merge_sort(arr)
print(sorted_array)

