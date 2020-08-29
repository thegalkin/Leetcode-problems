def twoSum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i] + numbers[j] == target:
                print(i,j,)
                return [i,j]

print(twoSum([-3,4,3,90], 0))