str = " mother was washing a window "


def reverse(mutable, start, end):
    p = start
    q = end
    while p < q:
        mutable[p], mutable[q] = mutable[q], mutable[p]
        p += 1
        q -= 1


def reverseWords(s):
    mutable = list(s)
    start = 0
    for i in range(len(s)):
        if mutable[i] == ' ':
            end = i - 1
            reverse(mutable, start, end)
            start = end + 2

    reverse(mutable, start, len(s)-1) #reverse last word

    reverse(mutable, 0, len(s)-1)
    return ''.join(mutable)


print(reverseWords(str))
