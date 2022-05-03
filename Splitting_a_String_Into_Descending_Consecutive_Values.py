import os
import sys
from tkinter.tix import Tree

test_data = [
    {
        "s": "1234"
    },
    {
        "s": "050043"
    },
    {
        "s": "9080701"
    },
    {
        "s": "10009998"
    },
    {
        "s": "a10009998"
    },
    {
        "s": "33333333333310009998222222222222"
    },
]

expected_res = [False, True, False, True, False, False]

def finder(s, previous, index, los):
    if (previous != -1 and int(s[index:]) == previous - 1):
        return True
    for i in range(1, los - index):
        current = int(s[index:index + i])
        if (previous == -1):
            if (finder(s, current, index + i, los)):
                return True
        else:
            if (previous == current + 1) and finder(s, current, index + i, los):
                return True
    return False

def splitString(data):
    s = data['s']
    los = len(s)
    # Verify input data
    if (los > 20 or los < 1):
        return False
    chars = set('0123456789')
    if any((c not in chars) for c in s):
        return False
    return finder(s, -1, 0, los)

def testFunc(func, test_data, expected_res):
    for i in range(0, len(test_data)):
        print('Input data: ', test_data[i])
        if(expected_res[i] == func(test_data[i])):
            print('\033[92m' + 'Pass' + '\033[0m')
        else: 
            print('\033[91m' + 'Fail' + '\033[0m')

if __name__ == "__main__":
    testFunc(splitString, test_data, expected_res)