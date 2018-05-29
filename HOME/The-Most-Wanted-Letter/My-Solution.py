"""
======================================================================================================================================================
给你一段文本，其中包含不同的英文字母和标点符号。
你要找到其中那个出现最多的 字母，返回的字母必须是 小写形式。
找这个“头号通缉字母”时，大小写不重要，所以对于你的搜索而言 "A" == "a"。 注意不要管标点符号、数字和空格，我们只要 字母！
如果你找到 两个或两个以上出现频率相同的字母， 那么返回字母表中靠前的那个。 例如“one”包含“o”、“n”、“e”每个字母一次，因此我们选择“e”。

输入: 包含待分析文本的字符串

输出: 那个出现最多的字母的字符串（小写哦）

范例:
checkio("Hello World!") == "l"
checkio("How do you do?") == "o"
checkio("One") == "e"
checkio("Oops!") == "o"
checkio("AAaooo!!!!") == "a"
checkio("abe") == "a"

有何功用: 大多数的解密任务都需要搞清一段文本中各种字符的出现频率。例如，有了字母的出现频率，我们就可以轻易地破解一个简单的移位密码或替换式密码了。语言专家们对此总是乐此不疲！

前提::
输入的文本 text 只包含 ASCII 码字符
0 < len(text) ≤ 10**5
======================================================================================================================================================
"""


def checkio(text):
    # 生成字典（key&value: letter&times）
    times_dict = dict()
    for _ in text.lower():  # 同一个字母不区分大小写
        if _.isalpha():
            times_dict[_] = times_dict.get(_, 0) + 1

    # 降序排列得到一个元祖列表[(letter1, times1), (letter2, times2), ...]
    times_list = sorted(times_dict.items(), key=lambda item: item[1], reverse=True)

    # 生成出现次数最多的字母列表
    most_wanted_list = [times_list[i][0] for i in range(len(times_list)) if times_list[i][1] == times_list[0][1]]

    # 第一种情况：此最高次数出现在多个字母身上，此时生成的列表将会存在多个元素，需要按ASCII表排序再返回
    # 第二种情况：此最高次数只出现在一个字母身上，直接返回对应字母
    return sorted(most_wanted_list, key=lambda x: ascii(x))[0] if len(most_wanted_list) > 1 else most_wanted_list[0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("b" * 9000 + "a" * 1000) == "b", "Long."  # changed for a better test
    assert checkio("b" * 9000 + "a" * 9000) == "a", "Long."  # added for a better test
    print("Test passed!")
