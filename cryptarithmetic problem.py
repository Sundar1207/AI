from itertools import permutations

def solve_cryptarithmetic(puzzle):
    words = puzzle.split()
    unique_chars = set().union(*words)
    if len(unique_chars) > 10:
        return "Too many unique characters"
    
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    chars = list(first_letters) + list(unique_chars - first_letters)
    
    for perm in permutations('0123456789', len(unique_chars)):
        if '0' in perm[:n]:
            continue
        mapping = {c: p for c, p in zip(chars, perm)}
        nums = []
        for word in words[:-1]:
            num = int(''.join(mapping[c] for c in word))
            nums.append(num)
        total = sum(nums)
        result_word = words[-1]
        result_num = int(''.join(mapping[c] for c in result_word))
        if total == result_num:
            return {c: int(mapping[c]) for c in unique_chars}
    return "No solution found"

print(solve_cryptarithmetic("SEND + MORE = MONEY"))
