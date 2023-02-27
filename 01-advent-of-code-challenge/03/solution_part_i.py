def priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27

with open('input.txt', 'r') as f:
    rucksacks = [line.strip() for line in f]

total_priority = 0

for rucksack in rucksacks:
    first_compartment = rucksack[:len(rucksack)//2]
    second_compartment = rucksack[len(rucksack)//2:]
    common_items = set(first_compartment) & set(second_compartment)
    for item in common_items:
        total_priority += priority(item)

print(total_priority)
