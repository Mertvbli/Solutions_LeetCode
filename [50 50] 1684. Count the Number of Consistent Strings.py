# 1684. Count the Number of Consistent Strings
# You are given a string allowed consisting of distinct characters and an array of strings words.
# A string is consistent if all characters in the string appear in the string allowed.
#
# Return the number of consistent strings in the array words.

def countConsistentStrings(allowed, words):
    count = 0
    for word in words:
        count += 1
        for letter in word:
            if letter not in allowed:
                count -= 1
                break
    return count


print(countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))
print(countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]))
print(countConsistentStrings("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]))
print(countConsistentStrings("fstqyienx", ["n","eeitfns","eqqqsfs","i","feniqis","lhoa","yqyitei","sqtn","kug","z","neqqis"]))
