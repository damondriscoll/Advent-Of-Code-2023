with open('inputs.txt', 'r') as f:
    histories = f.read().split('\n')

def getNextNumber(nums):
    differences = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
    if not all([v == 0 for v in differences]):
        return differences[-1] + getNextNumber(differences)
    else:
        return differences[-1]

sum = 0
for history in histories:
    history = list(map(int, history.split()))

    sum += history[-1] + getNextNumber(history)

print(sum)