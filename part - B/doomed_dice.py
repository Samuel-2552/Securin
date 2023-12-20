def probability(dice_a, dice_b):
    prob = {}
    for i in range(6):
        for j in range(6):
            sum = dice_a[i] + dice_b[j]
            prob[sum] = prob.get(sum,0)+1
    return prob

def combination(values, length, unique):

    all_pos = []
    cur = [0]*length

    def helper(x, start=0):
        
        if x == length:
            all_pos.append(cur.copy())
            return
        
        for i in range(start, len(values)):
            cur[x] = values[i]
            helper(x+1, i+unique)

    helper(0)
    return all_pos

def check(possibility1, possibility2, original_prob):
    lis=[]
    for i in range(len(possibility1)):
        for j in range(len(possibility2)):
            prob = probability(possibility1[i],possibility2[j])
            if prob==original_prob:
                lis.append([possibility1[i], possibility2[j]])
    return lis


def undoom_dice(dice_a, dice_b):
    constraint1 = range(0,5)
    constraint2 = range(0,max(dice_a)+max(dice_b))
    original_prob = probability(dice_a, dice_b)
    possibility1 = combination(constraint1, 6, 0)
    possibility2 = combination(constraint2, 6, 1)
    ans = check(possibility1,possibility2, original_prob)
    print("Solutions:", "Dice A\t\t", "Dice B", sep="\t")
    for i in range(len(ans)):
        print(f'Solution {i+1}:', *ans[i], sep='\t')


undoom_dice([1,2,3,4,5,6],[1,2,3,4,5,6])