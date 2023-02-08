def find_max_calories(file):
    max_calories = 0
    max_elf = 0
    elf = 0
    calories = 0
    with open(file) as f:
        for line in f:
            line = line.strip()
            if line:
                calories += int(line)
            else:
                if calories > max_calories:
                    max_calories = calories
                    max_elf = elf
                elf += 1
                calories = 0
    return max_elf, max_calories

if __name__ == '__main__':
    elf, calories = find_max_calories('calories.txt')
    print('O Elfo', elf + 1, 'está carregando mais Calorias:', calories)
