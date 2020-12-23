# 1678. Goal Parser Interpretation

# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)"
# in some order.
# The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al".
# The interpreted strings are then concatenated in the original order.

# Given the string command, return the Goal Parser's interpretation of command.
def interpret(command):
    mapped = {'G': 'G', '()': 'o', '(al)': 'al'}
    tmp = ''
    res = ''
    for i in command:
        tmp += i
        if tmp in mapped:
            res += mapped[tmp]
            tmp = ''
    return res

# solution 2 return command.replace('()', 'o').replace('(al)', 'al')

print(interpret("G()(al)"))
print(interpret("G()()()()(al)"))
print(interpret("(al)G(al)()()G"))
