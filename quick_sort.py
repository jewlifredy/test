from collections.abc import Iterable

from sort_types import T


def quick_sort(arr: Iterable[T]) -> list[T]:
    """
    快速排序：选取基准元素，将数组划分为较小和较大两部分，再递归排序。
    返回新列表，不修改原列表。
    """
    result = list(arr)
    _quick_sort_inplace(result, 0, len(result) - 1)
    return result


def _quick_sort_inplace(arr: list[T], low: int, high: int) -> None:
    # 只递归较短的一侧，较长的一侧用循环处理，保证栈深度为 O(log n)
    while low < high:
        pivot_idx = _partition(arr, low, high)
        if pivot_idx - low < high - pivot_idx:
            _quick_sort_inplace(arr, low, pivot_idx - 1)
            low = pivot_idx + 1
        else:
            _quick_sort_inplace(arr, pivot_idx + 1, high)
            high = pivot_idx - 1


def _median_of_three(arr: list[T], low: int, high: int) -> int:
    mid = (low + high) // 2
    if arr[mid] < arr[low]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[high] < arr[mid]:
        arr[mid], arr[high] = arr[high], arr[mid]
    return mid


def _partition(arr: list[T], low: int, high: int) -> int:
    mid = _median_of_three(arr, low, high)
    arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if not pivot < arr[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
