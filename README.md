# Demo01 - 排序算法学习项目

Python 实现的经典排序算法示例，包含冒泡排序与快速排序，并附带单元测试。

## 项目结构

```
Demo01/
├── bubble_sort.py       # 冒泡排序
├── quick_sort.py        # 快速排序
├── sort_types.py        # 共享类型定义
├── test_sorting.py      # 两种算法的 pytest 测试
├── pyproject.toml       # 项目与工具配置（pytest / ruff / mypy）
└── README.md
```

## 环境要求

- Python 3.10+

## 使用方法

```python
from bubble_sort import bubble_sort
from quick_sort import quick_sort

data = [64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(data))  # [11, 12, 22, 25, 34, 64, 90]
print(quick_sort(data))  # [11, 12, 22, 25, 34, 64, 90]
```

两个函数接受任意可迭代对象（列表、元组、生成器等），元素只需支持 `<` 比较，均返回排序后的新列表，不会修改原数据。

## 运行测试

```bash
pip install -e ".[dev]"
pytest -v
ruff check . && ruff format --check .
mypy .
```

## 算法说明

| 算法     | 平均时间复杂度 | 空间复杂度 | 特点                     |
|----------|----------------|------------|--------------------------|
| 冒泡排序 | O(n²)          | O(1)       | 实现简单，适合小规模数据 |
| 快速排序 | O(n log n)     | O(log n)   | 三数取中选基准，栈深度 O(log n) |

## 仓库地址

https://github.com/jewlifredy/test
