dice_a = 6
dice_b = 6
possibilites=0
print("Dice A", "Dice B", sep="\t")
print("----"*4)
for i in range(1,dice_a+1):
    for j in range(1,dice_b+1):
        possibilites +=1
        print(i, j, sep="\t")
print("----"*4)
print("Therefore the total no of combinations are: ", possibilites)