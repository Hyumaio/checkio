"""
======================================================================================================================================================
cr.Sim0000 from py.checkio.org

1."w for w in words" is a generator.
2."w in text.lower()" returns a bool signature.
3."w in text.lower() for w in words" is also a generator means that for every w in words, if w in text.lower(), return True, else False.
4.sum(True) == 1, sum(False) == 0

So sum(w in text.lower() for w in words) worked properly.
======================================================================================================================================================
"""


def count_words(text, words):
    return sum(w in text.lower() for w in words)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Test passed!")
