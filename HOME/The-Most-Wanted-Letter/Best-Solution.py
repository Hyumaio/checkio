"""
======================================================================================================================================================
cr.bryukh from py.checkio.org
======================================================================================================================================================
"""

import string


def checkio(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)  # == return max(string.ascii_lowercase, key=lambda x: text.count(x))


# ====================================================================================================================================================
# the following line is added by me just for test, not original
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
