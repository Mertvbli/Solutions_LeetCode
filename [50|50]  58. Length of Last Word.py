# Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
# A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord(s: str) -> int:
    if not s.split():  # s.strip() можно заменить на s.split(). Я понял логику так, после долгих размышлений: это если .strip() и .split() могут разделить слова
        return 0       # и убрать пробелы, то от обратного при помощи not невозможно это сделать с просто пробелами без какого-либо текста.
    new_s = s.split()
    return len(new_s[-1])

# examples
print(lengthOfLastWord('low rider'))
print(lengthOfLastWord('low fdlkfhdsjfhdsfsd'))
print(lengthOfLastWord(""))
print(lengthOfLastWord("   "))
