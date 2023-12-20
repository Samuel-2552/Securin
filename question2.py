dice_a = 6
dice_b = 6
print('Dice', '|', *range(1,7), sep="\t")
print("--------|","-"*50, sep="")
distribution={}
for i in range(1,dice_a+1):
    print(i ,"|", sep='\t', end="\t")
    for j in range(1,dice_b+1):
        sum = i+j
        distribution[sum] = distribution.get(sum,0)+1
        print(sum, '', sep="\t", end="")
    print()
print("-"*60)
print("The distribution is as follows: ")
print("-"*97)
print("|", *distribution.keys(), sep="\t", end="\t|\n")
print("-"*97)
print("|", *distribution.values(), sep="\t", end="\t|\n")
print("-"*97)