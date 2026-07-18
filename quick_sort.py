def quick_sort(arr):
    """
    快速排序：选取基准元素，将数组划分为较小和较大两部分，再递归排序。
    返回新列表，不修改原列表。
    """
    result = arr.copy()
    _quick_sort_inplace(result, 0, len(result) - 1)
    return result


def _quick_sort_inplace(arr, low, high):
    if low < high:
        pivot_idx = _partition(arr, low, high)
        _quick_sort_inplace(arr, low, pivot_idx - 1)
        _quick_sort_inplace(arr, pivot_idx + 1, high)


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
