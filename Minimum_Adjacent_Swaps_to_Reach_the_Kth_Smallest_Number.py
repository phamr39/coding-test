import os
import sys

test_data = [
    {
        "num": "5489355142",
        "k": 4,
    },
    {
        "num": "11112",
        "k": 4,
    },
    {
        "num": "00123",
        "k": 1,
    },
    {
        "num": "98765",
        "k": 2,
    },
    {
        "num": "111111",
        "k": 2,
    },
]

expected_res = [2, 4, 1, -1, -1]

def reverse(nums, begin, end):
    left, right = begin, end-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

def nextPermutation(nums, begin, end):
    k, l = begin-1, begin
    for i in reversed(range(begin, end-1)):
        if nums[i] < nums[i+1]:
            k = i
            break
    else:
        return -1
    for i in reversed(range(k+1, end)):
        if nums[i] > nums[k]:
            l = i
            break
    nums[k], nums[l] = nums[l], nums[k]
    reverse(nums, k+1, end)
    return nums

def getMinSwaps(data):
    num = data["num"]
    k = data["k"]
    new_num = list(num)
    while k:
        new_num = nextPermutation(new_num, 0, len(new_num))
        if new_num == -1:
            return -1
        k = k - 1
    result = 0
    for i in range(0, len(new_num)):
        if new_num[i] == num[i]:
            continue
        for j in range(i+1, len(new_num)):
            if new_num[j] == num[i]:
                break
        result += j-i
        for j in reversed(range(i+1, j+1)):
            new_num[j], new_num[j-1] = new_num[j-1], new_num[j]
    return result

def testFunc(func, test_data, expected_res):
    for i in range(0, len(test_data)):
        print('Input data: ', test_data[i])
        # print(func(test_data[i]))
        if(expected_res[i] == func(test_data[i])):
            print('\033[92m' + 'Pass' + '\033[0m')
        else: 
            print('\033[91m' + 'Fail' + '\033[0m')

if __name__ == "__main__":
    testFunc(getMinSwaps, test_data, expected_res)