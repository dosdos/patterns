"""
Word Count Engine - Pramp.com

Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all
unique words in it and their number of occurrences, sorted by the number of occurrences in a descending order.
If two or more words have the same count, they should be sorted according to their order in the original sentence.
Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the
words “Perfect” and “perfect” should be considered the same word.

The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.

Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space
complexity.

Examples:

input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"],
          ["get", "1"], ["by", "1"], ["just", "1"] ]

Important: please convert the occurrence integers in the output list to strings (e.g. "3" instead of 3).
We ask this because in compiled languages such as C#, Java, C++, C etc., it’s not straightforward to
create mixed-type arrays (as it is, for instance, in scripted languages like JavaScript, Python, Ruby etc.).
The expected output will simply be an array of string arrays.
"""

import heapq


def _strip_non_chars(word):
    return ''.join([c for c in word if c == ' ' or 'a' <= c <= 'z'])


def word_count_engine(document):  # "Practice makes perfect. ...""

    document = document.lower()

    # remove puncuations
    document = _strip_non_chars(document)

    # split words.  -> get a list of words
    words = document.split()  # ['practice', 'makes', 'practice']

    # create the dict of occurrencies (save both num of occ and first idx match)
    mapping = dict()
    for idx, w in enumerate(words):
        # "practice": (counter, idx)
        if w in mapping:
            mapping[w] = (mapping[w][0] + 1, mapping[w][1])
        else:
            mapping[w] = (1, idx)
            #  mapping =  mapping = {'practice': (2, 0)]  mapping = {'makes': (1, 1)]]

    # create a heap with priority -> most frequent first
    heap = []
    heapq.heapify(heap)
    for k in mapping.keys():
        counter, first_idx = mapping[k]
        heapq.heappush(heap, (-counter, first_idx, k))  # (-2, 0, 'practice'), (-1, 1, 'makes')

    # pop elements out of the heap and return it
    result = []
    while heap:
        most_frequent = heapq.heappop(heap)
        result.append([most_frequent[2], str(-most_frequent[0])])

    return result


doc = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
print(word_count_engine(doc))
