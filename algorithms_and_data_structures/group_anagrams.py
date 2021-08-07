"""
Group Words that are Anagrams  - CodePro problem 41 (www.techseries.dev)
"""

import collections


def hash_key(word):
    return "".join(sorted(word))


def hash_key_2(word):
    arr = [0] * 26
    for c in word:
        arr[ord(c) - ord('a')] += 1
    return tuple(arr)


def group_anagram_words(words):
    groups = collections.defaultdict(list)
    for w in words:
        groups[hash_key_2(w)].append(w)
    return list(groups.values())


print(group_anagram_words(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# (['abc', 'cba'], ['bcd', 'cbd'], ['efg'])
