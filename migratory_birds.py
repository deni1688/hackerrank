def migratoryBirds(arr):
    countDict = {}

    for n in arr:
        countDict.update({n: arr.count(n)})

    sortedCountArr = sorted(countDict.items(), key=lambda x: x[1], reverse=False)

    size = len(sortedCountArr)

    if sortedCountArr[size-1][1] != sortedCountArr[size-2][1]:
        return sortedCountArr[size-1][0]

    if sortedCountArr[size-1][0] > sortedCountArr[size-2][0]:
        return sortedCountArr[size-2][0]
    
    return  sortedCountArr[size-1][0]


print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
