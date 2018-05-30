"""
======================================================================================================================================================
……如果让我的指头漫无目的地在打字机的按键上面移动，那么我的长篇大论就可能变成一段明白易懂的话语。如果一队猿猴在许多打字机上乱按一气，它们也有可能写出大英博物馆里所有的书籍，它们这样做的机会肯定地比分子恢复到容器一半的机会要更多。
A. S. 爱丁顿，《物理世界的本质》，1927。

“福特！”他说，“外面有无数只猴子想要进来和咱们讨论他们创作的剧本《哈姆雷特》。”
道格拉斯·亚当斯，《银河系漫游指南》。

无限猴子定理是指让一只猴子在打字机上随机地按键，当时间无穷时，几乎必然能够打出任何给定的文字，例如约翰·沃利斯的全套著作，也有可能是一部丹·布朗的小说。
让我们假设我们的猴子不断地打字，它们打出了各种各样的文字片段。我们来尝试找到其中有意义的词汇。
你将得到一些可能含有有意义的词汇的文本。你需要统计在给出文本中包含的词汇数量。一个词汇可能是一个整体或者另一个词汇的一部分。检查文本时不区分大小写，你需要检查的词汇将被以小写形式给出且不会重复。如果一个词在文本中出现多次，你只需要计数一次。

举个例子，文本："How aresjfhdskfhskd you?"，词汇：("how", "are", "you", "hello")。输出结果是3。

输入：两个参数。一段文字作为字符串(str)输入，一组词汇作为一组字符串(a set of strings)输入。

输出：文本中相关词汇的数量，整数(int)。

范例：
count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3
count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2
count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            {"sum", "hamlet", "infinity", "anything"}) == 1

如何应用：Python在处理文本时有用且强大。这个任务是你未来可能编写的文字搜索工具的一个简单示范。

前提：
0 < len(text) ≤ 256
all(3 ≤ len(w) and w.islower() and w.isalpha for w in words)
======================================================================================================================================================
"""


def count_words(text: str, words: set) -> int:
    count = 0
    for i in words:
        if i in text.lower():
            count += 1
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Test passed!")
