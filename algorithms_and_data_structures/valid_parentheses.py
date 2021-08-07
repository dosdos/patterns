"""
Valid Parentheses  - CodePro (www.techseries.dev)
"""

mapping = {
    '(': ')',
    '[': ']',
    '{': '}',
}
inv_mapping = {v: k for k, v in mapping.items()}


def is_valid(expression):
    heap = []
    for i in expression:
        if i in mapping:
            heap.append(i)
        elif i in inv_mapping:
            if len(heap) == 0 or mapping[heap[-1]] != i:
                return False
            heap.pop()
    return len(heap) == 0


s = '(()[]){{}[()]}'
print(is_valid(s))
# True

s = '(()[){{}[()]}'
print(is_valid(s))
# False

s = ')]}'
print(is_valid(s))
# False
