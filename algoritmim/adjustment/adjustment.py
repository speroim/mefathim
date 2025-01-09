
def maxWeight(item, weight):
    if len(item) == 0 or weight == 0:
        return 0
    
    firstItem = item[0]
    restItem = item [1:] 

    withItem  = 0
    if weight >= firstItem:
        withItem = maxWeight(restItem, weight-firstItem) + firstItem
    withOutItem = maxWeight(restItem, weight)
    return max(withItem, withOutItem)

item = [10,30,20]
weight = 50
result = maxWeight(item, weight)

print (result)



def dp(item,weight):
    rows, column = len(item) , weight
    table = [[-1 for _ in range(column + 1)] for _ in range (rows + 1)]
    for col in range (column+1):
        table[0][col] =0
    for row in range (rows+1): 
        table[row][0] = 0
    item, weight = 0,0
    for col in range (1, column+1):
        if item[0] =< table[1][col] = 


    table[item][weight]
    for row in table: 
        print (row)
item = [2,3,1]
weight = 5


dp(sorted(item),weight)