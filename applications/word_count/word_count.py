import re

specials = ['"', ':', ';', ',', '.', '-', '+', '=', '/',
            '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']


def replace_specials(string, specials):
    for char in specials:
        if char in string:
            string = string.replace(char, "")
    return string


def word_count(s):
    words_count = {}
    # Your code here
    # res = re.split('[/s:;,.-+=/\|[]/{/}()*^&]', s)
    s = replace_specials(s, specials)
    s = s.split()
    print(s)
    for word in s:
        word = word.lower()
        if word not in words_count:
            words_count[word] = 1
        else:
            words_count[word] += 1
    return words_count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
