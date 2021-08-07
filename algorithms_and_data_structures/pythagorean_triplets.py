# Find Pythagorean Triplets (from coderpro)

def find_pythagorean_triplets(nums):
    squares = {n ** 2 for n in nums}
    for i, a in enumerate(nums):
        for b in nums[i:]:
            if a ** 2 + b ** 2 in squares:
                return True
    return False


print(find_pythagorean_triplets([3, 5, 12, 5, 13]))
# True
print(find_pythagorean_triplets([13, 5, 12, 5, 3]))
# True
print(find_pythagorean_triplets([3, 5, 11, 5, 13]))
# True
print(find_pythagorean_triplets([3, 5, 11, 5, 13, 4]))
# True
