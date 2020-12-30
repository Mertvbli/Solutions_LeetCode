# 1662. Check If Two String Arrays are Equivalent

# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.


def arrayStringsAreEqual(word1, word2):
    true = True
    false = False
    if ''.join(word1) == ''.join(word2):
        return true
    else:
        false

# Solution 2.  return ''.join(word1) == ''.join(word2)


print(arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
print(arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))
print(arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
