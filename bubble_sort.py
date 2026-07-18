def bubble_sort(arr):
    """
    冒泡排序：相邻元素比较并交换，每轮将最大值“冒泡”到末尾。
    返回新列表，不修改原列表。
    """
    result = arr.copy() 
    n = len(result)


    
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break

    return result
