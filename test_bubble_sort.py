import unittest   

from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):

    def test_normal_unsorted_list(self):
        """测试普通无序列表"""
        self.assertEqual(
            bubble_sort([64, 34, 25, 12, 22, 11, 90]),
            [11, 12, 22, 25, 34, 64, 90],
        )

    def test_already_sorted_list(self):
        """测试已有序列表"""
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        """测试逆序列表"""
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_single_element(self):
        """测试单元素列表"""
        self.assertEqual(bubble_sort([42]), [42])

    def test_empty_list(self):
        """测试空列表"""
        self.assertEqual(bubble_sort([]), [])

    def test_list_with_duplicates(self):
        """测试含重复元素"""
        self.assertEqual(
            bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]),
            [1, 1, 2, 3, 4, 5, 5, 6, 9],
        )

    def test_negative_numbers(self):
        """测试含负数"""
        self.assertEqual(bubble_sort([3, -1, 0, -5, 2]), [-5, -1, 0, 2, 3])

    def test_all_same_elements(self):
        """测试所有元素相同"""
        self.assertEqual(bubble_sort([7, 7, 7, 7]), [7, 7, 7, 7])

    def test_two_elements(self):
        """测试两个元素"""
        self.assertEqual(bubble_sort([2, 1]), [1, 2])

    def test_does_not_modify_original(self):
        """测试不修改原列表"""
        original = [3, 1, 2]
        bubble_sort(original)
        self.assertEqual(original, [3, 1, 2])


if __name__ == "__main__":
    unittest.main()
