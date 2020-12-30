# 1221. Split a String in Balanced Strings

# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
# Given a balanced string s split it in the maximum amount of balanced strings.
# Return the maximum amount of splitted balanced strings.


def balancedStringSplit(s):
    resultat = 0
    count = 0
    for char in s:
        if char == 'L':
            count += 1
        else:
            count -= 1
        if count == 0:
            resultat += 1

    return resultat


print(balancedStringSplit("RLRRLLRLRL"))
print(balancedStringSplit("RLLLLRRRLR"))
print(balancedStringSplit("RLRRRLLRLL"))
print(balancedStringSplit("LLLLRRRR"))
