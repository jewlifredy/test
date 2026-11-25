from collections.abc import Iterable

from sort_types import T


def bubble_sort(arr: Iterable[T]) -> list[T]:
    """
    冒泡排序：相邻元素比较并交换，每轮将最大值"冒泡"到末尾。
    返回新列表，不修改原列表。
    """
    result = list(arr)
    n = len(result)

    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if result[j + 1] < result[j]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break

    return result
