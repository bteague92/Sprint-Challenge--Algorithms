'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) == 0:
        return 0
    if "th" in word:
        if word[0:2] == "th":
            return count_th(word[2:]) + 1

        return count_th(word[1:])

    return 0
