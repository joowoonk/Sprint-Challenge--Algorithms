'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # if the length of word is 0 then stop with 0
    # if len(word) == 0:
    #     return 0
    if word == "":
        return 0
    # if a first sliced letter start with t the...
    if word[0] == "t":
        #stops when t is last word..
        if len(word) == 1:
            return 0
        #return 1 if h is the second letter there...
        if word[1] == "h":
            return 1 + count_th(word[1:])
        #if there is more then keep going
        else:
            return 0 + count_th(word[1:])
    #slice the letter to next letter
    return count_th(word[1:])
print(count_th("abcthxyz"))
print(count_th(""))
print(count_th("abcthefthghith"))
print(count_th("thhtthht"))
print(count_th("THtHThth"))