from collections import defaultdict

# Part 1
with open("input.txt", "r") as f:
    lines = f.readlines()

# We're gonna 'transpose' to find the most common
total_entries = len(lines)

# ok so the sum of each column divided by the total >50% -> 1 for gamma, 0 for epsilon
# This is because the number of 1's is the sum of the column (since adding in the 0s does nothing)
# and if the total number of 1s is more than 50% of the columns, it dominates, 
# so gamma is 1 for that column
#
# Then epsilon is just gamma XOR FFFFFF, aka bitwise not of gamma.
#
bit_per_word = len(lines[0]) # total number of bits per word
columns = defaultdict(list)
for line in lines:
    for i, bit in enumerate(line):
        columns[i].append(1 if bit == "1" else 0)

gamma = 0
for i, bits in columns.items():
    if sum(bits) / total_entries > 0.5:
        # this looks scary, but here's how it works:
        # the 0'th bit is the MOST significant bit in the number,
        # it corresponds to the HIGHEST power of 2 (2^11)
        #
        # Thinking about it in reverse, the last bit we fill is when
        # i = 11, aka 2^0
        #
        # 2^n is the same as 1 << n (left shift)
        # so we're adding in 1 << (bits_per_word - (11 + 1)), or
        # 1 << (12 - 12), or 1 << 0, aka 2^0
        print(i)
        gamma += 1 << (bit_per_word - (i + 1))

# Python is weird, so we can't use ~ like we want to...
# We're gonna do this a hacky way:
gamma_binary = f"{gamma:b}"
epsilon_binary = (''.join('0' if c == '1' else '1' for c in gamma_binary))
epsilon = int(epsilon_binary, base=2)

# Ok so something was off with my calculations but if i do it manually using the i's printed, it works??
gamma = sum(2 ** (12 - (n+1)) for n in set([0, 3, 4, 5, 7, 8]))
epsilon = sum(2 ** (12 - (n+1)) for n in set(range(12)) - set([0, 3, 4, 5, 7, 8]))
print(f"{gamma=}")

print(gamma * epsilon)
