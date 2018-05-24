"""
斯蒂芬和索菲亚对于一切都使用简单的密码，忘记了安全性。
请你帮助尼古拉开发一个密码安全检查模块。如果密码的长度大于或等于10个字符，且其中至少有一个数字、一个大写字母和一个小写字母，该密码将被视为足够强大。
密码只包含ASCII拉丁字母或数字。

输入: 密码。

输出: 密码的安全与否，作为布尔值(bool)，或者任何可以转换和处理为布尔值的数据类型。你会在结果看到转换后的结果(True 或 False)。
"""


def checkio(data: str) -> bool:
    # IF-ELSE
    _is_len_gt10 = False
    _is_alnum = False
    _is_lower = False
    _is_upper = False
    _is_digit = False
    if len(data) >= 10:
        _is_len_gt10 = True
    if data.isalnum():
        _is_alnum = True
    for _ in data:
        if _.islower():
            _is_lower = True
        if _.isupper():
            _is_upper = True
        if _.isdigit():
            _is_digit = True
    if all([_is_len_gt10, _is_alnum, _is_lower, _is_upper, _is_digit]):
        return True
    return False


# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
