import os
import sys

test_data = [
    {
        "nums": [1,2,3,4,5],
        "target": 5,
        "start": 3
    },
    {
        "nums": [1],
        "target": 1,
        "start": 0
    },
    {
        "nums": [1,1,1,1,1,1,1,1,1,1],
        "target": 1,
        "start": 0
    },
    {
        "nums": [1,10001,1,1,1,1,1,1,1,10001],
        "target": 1,
        "start": 0
    },
    {
        "nums": [1,2,3,4,5],
        "target": 7,
        "start": 0
    },
    {
        "nums": [1,2,3,4,5],
        "target": 5,
        "start": 9
    },
    {
        "nums": [1,2,3,4,5],
        "target": 5,
        "start": -1
    }
]

expected_res = [1,0,0,-1,-1,-1,-1]

def getMinDistance(data):
    # Due to 1 <= nums.length <= 1000 and 0 <= start <= nums.length so max of abs(i - start) = 1000
    nums = data["nums"]
    target = data["target"]
    start = data["start"]
    # Verify input data
    isValid = True
    if (len(nums) > 1000 or len(nums) < 1): 
        return -1
    if (start < 0 or start >= len(nums)): 
        return -1
    for num in nums:
        if (num > 10000):
            isValid = False
            break
    if (not isValid):
        return -1
    # Find output
    min_val = 1001
    for i in range(0, len(nums)):
        if ((nums[i] == target) and (abs(i - start) < min_val)):
            min_val = abs(i - start)
    if (min_val > 1000):
        min_val = -1
    return min_val

def testFunc(func, test_data, expected_res):
    for i in range(0, len(test_data)):
        print('Input data: ', test_data[i])
        print(func(test_data[i]))
        if(expected_res[i] == func(test_data[i])):
            print('\033[92m' + 'Pass' + '\033[0m')
        else: 
            print('\033[91m' + 'Fail' + '\033[0m')

if __name__ == "__main__":
    testFunc(getMinDistance, test_data, expected_res)