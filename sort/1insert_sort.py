array = [10,17,4,9]
arr1 = [3,6,4,35]
miki = [9,54,23,16,1]



def insert_sort(arr):
    i=0
    j=0
    counter_changes =0
    counter_comparison = 0
    while j <len(arr)-1:
        while i < len(arr)-1: 
            if arr[i+1] >= arr[i]:
                i += 1
            else:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                counter_changes +=1
                i += 1
            counter_comparison +=1
        j +=1
        i = 0

    print(f"my new array is: {arr}, changes counter: {counter_changes}, counter comparison: {counter_comparison}")

insert_sort(miki)