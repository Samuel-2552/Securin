dice_a = 6
dice_b = 6
distribution={}
for i in range(1,dice_a+1):
    for j in range(1,dice_b+1):
        sum = i+j
        distribution[sum] = distribution.get(sum,0)+1
        
print("The probability of all possible sums is as follows: ")
print("-"*97)
print("|", *distribution.keys(), sep="\t", end="\t|\n")
print("-"*97)
print("|", *map(lambda x: round(x/36, 2), distribution.values()), sep="\t", end="\t|\n")
print("-"*97)