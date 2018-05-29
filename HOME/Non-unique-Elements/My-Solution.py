"""
======================================================================================================================================================
你将得到一个含有整数（X）的非空列表。在这个任务里，你应该返回在此列表中的非唯一元素的列表。要做到这一点，你需要删除所有独特的元素（这是包含在一个给定的列表只有一次的元素）。解决这个任务时，不能改变列表的顺序。例如：[1，2，3，1，3] 1和3是非唯一元素，结果将是 [1, 3, 1, 3]。

输入: 一个含有整数的列表。

输出: 一个含有不唯一元素的整数列表。

范例:
checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
checkio([1, 2, 3, 4, 5]) == []
checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]

如何使用： 这个任务将帮助您了解如何操作数组，这是解决更复杂的任务的基础。这个概念可以很容易地推广到真实世界的任务。例如你需要通过删除低频的元素（噪声）来使统计数据更清楚。

前提:
0 < |X| < 1000
======================================================================================================================================================
"""

# Solution 1:
# def checkio(data: list) -> list:
#     need_remove = list()
#     for i in data:
#         if data.count(i) == 1:
#             need_remove.append(i)
#     for i in need_remove:
#         data.remove(i)
#     return data


# Solution 2: a better way
from collections import Counter


def checkio(data: list) -> list:
    for i in Counter(data).items():
        if i[1] == 1:
            data.remove(i[0])
    return data


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    assert checkio(list(range(1000000)) + [0]) == [0, 0], "big list"
    print("Test passed!")
