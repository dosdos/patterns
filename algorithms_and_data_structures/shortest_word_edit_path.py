"""
Shortest Word Edit Path (Pramp.com)

Given two words source and target, and a list of words words, find the length of the shortest series of edits that
transforms source to target. Each edit must change exactly one letter at a time, and each intermediate word (and the
final target word) must exist in words. If the task is impossible, return -1.
"""


def shortest_word_edit_path_original(source, target, words, strategy=1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    wordset = set(words)
    queue = list()
    queue.append((source, 0))
    seen = {source}

    while queue:
        word, depth = queue.pop()
        if word == target:
            return depth
        for i in range(len(word)):

            # First Strategy:
            if strategy == 1:
                for word2 in words:
                    if len(word2) == len(word):
                        diff = 0
                        for j in range(len(word)):
                            if word[j] != word2[j]:
                                diff += 1
                                if diff == 2:
                                    break
                        if diff == 1 and word2 not in seen:
                            queue.append((word2, depth + 1))
                            seen.add(word2)
            else:  # Second Strategy:
                for c in alphabet:
                    word2 = word[:i] + c + word[i + 1:]
                    if word2 in wordset and word2 not in seen:
                        queue.append((word2, depth + 1))
                        seen.add(word2)
    return -1


def shortest_word_edit_path(source, target, words, strategy=1):
    pass


source = "bit"
target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot", "pat"]
print(shortest_word_edit_path(source, target, words))

source = "no"
target = "go"
words = ["to"]
print(shortest_word_edit_path(source, target, words))
