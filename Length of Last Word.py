def lengthOfLastWord(s: str) -> int:
    if not s.split():  # s.strip() как ещё один вариант решения
        return 0
    new_s = s.split()
    return len(new_s[-1])


print(lengthOfLastWord('low rider'))
print(lengthOfLastWord('low fdlkfhdsjfhdsfsd'))
print(lengthOfLastWord(""))
print(lengthOfLastWord("   "))
