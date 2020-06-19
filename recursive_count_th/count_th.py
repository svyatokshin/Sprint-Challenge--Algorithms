'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # if word is less than 2 letters long, we have to return 0 because its not possible for it to have 'th' in it.
    if len(word) < 2:
        return 0

    # must use recursion, so we must call the count_th() function once we find the first 'th'
    # we can do this by specifying what part of the string we are looking at and comparing it to our target 'th'
    # change the scope to the first two letters, add 1 if the th appears and 0 if not, then rerun
    # same word minus the first letter
    if word[:2] == 'th':
        return 1 + count_th(word[1:])
    else:
        return 0 + count_th(word[1:])


print(count_th('slkdjafsldkfjlsthlskdjflsthsdfth'))
