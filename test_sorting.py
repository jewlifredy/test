import random
from collections.abc import Callable

import pytest

from bubble_sort import bubble_sort
from quick_sort import quick_sort

SortFunc = Callable[[list], list]

ALGORITHMS = [bubble_sort, quick_sort]

CASES = [
    pytest.param([64, 34, 25, 12, 22, 11, 90], id="普通无序列表"),
    pytest.param([1, 2, 3, 4, 5], id="已有序列表"),
    pytest.param([5, 4, 3, 2, 1], id="逆序列表"),
    pytest.param([42], id="单元素列表"),
    pytest.param([], id="空列表"),
    pytest.param([3, 1, 4, 1, 5, 9, 2, 6, 5], id="含重复元素"),
    pytest.param([3, -1, 0, -5, 2], id="含负数"),
    pytest.param([7, 7, 7, 7], id="所有元素相同"),
    pytest.param([2, 1], id="两个元素"),
    pytest.param([1000000, 500, 123456, 42], id="含大数"),
    pytest.param([3.2, 2, 5.5, 1, 0.1], id="浮点数和整数"),
    pytest.param([-1.5, 2.2, 0, -3.3, 1], id="负浮点数"),
    pytest.param(list(range(100)), id="较大的已排序列表"),
    pytest.param(list(range(99, -1, -1)), id="较大的逆序列表"),
    pytest.param(["banana", "apple", "cherry"], id="字符串"),
]


@pytest.fixture(params=ALGORITHMS, ids=lambda f: f.__name__)
def sort(request: pytest.FixtureRequest) -> SortFunc:
    return request.param


@pytest.mark.parametrize("data", CASES)
def test_sorts_like_builtin(sort: SortFunc, data: list) -> None:
    assert sort(data) == sorted(data)


def test_does_not_modify_original(sort: SortFunc) -> None:
    original = [3, 1, 2]
    sort(original)
    assert original == [3, 1, 2]


def test_accepts_any_iterable(sort: SortFunc) -> None:
    assert sort((3, 1, 2)) == [1, 2, 3]
    assert sort(x for x in [3, 1, 2]) == [1, 2, 3]


def test_random_lists(sort: SortFunc) -> None:
    rng = random.Random(0)
    for _ in range(50):
        data = [rng.randint(-100, 100) for _ in range(rng.randint(0, 50))]
        assert sort(data) == sorted(data)


@pytest.mark.parametrize(
    "data",
    [
        pytest.param(list(range(10_000)), id="已排序"),
        pytest.param(list(range(10_000, 0, -1)), id="逆序"),
        pytest.param([1] * 10_000, id="全部相同"),
    ],
)
def test_quick_sort_large_input_no_recursion_error(data: list) -> None:
    assert quick_sort(data) == sorted(data)
