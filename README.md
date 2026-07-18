# Demo01 - 排序算法学习项目

Python 实现的经典排序算法示例，包含冒泡排序与快速排序，并附带单元测试。

## 项目结构

```
Demo01/
├── bubble_sort.py       # 冒泡排序
├── quick_sort.py        # 快速排序
├── test_bubble_sort.py  # 冒泡排序测试
├── test_quick_sort.py   # 快速排序测试
└── README.md
```

## 环境要求

- Python 3.8+

## 使用方法

```python
from bubble_sort import bubble_sort
from quick_sort import quick_sort

data = [64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(data))  # [11, 12, 22, 25, 34, 64, 90]
print(quick_sort(data))   # [11, 12, 22, 25, 34, 64, 90]
```

两个函数均返回排序后的新列表，不会修改原列表。

## 运行测试

```bash
python -m unittest test_bubble_sort.py -v
python -m unittest test_quick_sort.py -v
```

## 算法说明

| 算法     | 平均时间复杂度 | 空间复杂度 | 特点                     |
|----------|----------------|------------|--------------------------|
| 冒泡排序 | O(n²)          | O(1)       | 实现简单，适合小规模数据 |
| 快速排序 | O(n log n)     | O(log n)   | 平均性能优秀，常用排序   |

## 仓库地址

https://github.com/jewlifredy/test
