with open ("input.txt") as file:
    rounds = [i for i in file.read().strip().split("\n")]
    
#print(rounds)

outcomes = {
    "A X":4, "A Y":8, "A Z":3,
    "B X":1, "B Y":5, "B Z":9,
    "C X":7, "C Y":2, "C Z":6
}

total_points_p1 = 0
for round in rounds:
    total_points_p1 += outcomes[round]
    
desired_outcomes = {
    "A X":3, "A Y":4, "A Z":8,
    "B X":1, "B Y":5, "B Z":9,
    "C X":2, "C Y":6, "C Z":7
}

total_points_p2 = 0
for round in rounds:
    total_points_p2 += desired_outcomes[round]


print ("Minha pontuação total seria: ", total_points_p1 )

print ("Minha pontuação total seria: ", total_points_p2 )
