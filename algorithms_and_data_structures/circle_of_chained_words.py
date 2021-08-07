"""
Circle of Chained Words  - CodePro problem 51 (www.techseries.dev)
"""


def chained_words(words):
    """
    :param words: list of strings
    :return: True if there is a chain, False otherwise

    'apple', 'eggs', 'snack', 'karat', 'tuna'
     a,e      e,s    s,k    k,t    t,a

    adjacency_map = {
        a: [e],
        e: [s],
        s: [k],
        ...
    }

    """

    # create the adjacency map
    # create a stack to save the current visited
    # create a set to mark the visited
    # start from one word (is not relevant which one we are searching a circle)
    # update the list of visited until we have visited and the path is lower than the num of words (n)
    # if we reached n, then we need to compare first word with last word, if we have a circle return true
    return False


print(chained_words(['apple', 'eggs', 'snack', 'karat', 'tuna']))
# True

print(chained_words(['apple', 'eggs', 'snack', 'karat', 'tunax']))
# False
