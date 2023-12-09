with open('inputs.txt', 'r') as f:
    histories = f.read().split('\n')

def getNextNumber(nums):
    differences = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    if any(differences):
        return differences[0] - getNextNumber(differences)
    else:
        return differences[0]

sum = 0
for history in histories:
    history = list(map(int, history.split()))

    sum += history[0] - getNextNumber(history)

print(sum)