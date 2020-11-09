import operator

def migratoryBirds(arr):
    countDict = {}
 
    for n in arr:
        if n in countDict:
            continue
        countDict.update({n: arr.count(n)})

    sortedCountArr = sorted(countDict.items(), key=operator.itemgetter(1))

    if sortedCountArr[-1][1] != sortedCountArr[-2][1]:
        return sortedCountArr[-1][0]

    if sortedCountArr[-1][0] > sortedCountArr[-2][0]:
        return sortedCountArr[-2][0]
    
    return  sortedCountArr[-1][0]


print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
