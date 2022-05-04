import os
import sys
import heapq

test_data = [
    {
        "intervals": [[1,4],[2,4],[3,6],[4,4]],
        "queries": [2,3,4,5]
    },
    {
        "intervals": [[2,3],[2,5],[1,8],[20,25]],
        "queries": [2,19,5,22]
    },
]

expected_res = [[3,3,1,4],[2,-1,4,6]]

def minInterval(data):
    intervals = data["intervals"]
    queries = data["queries"]
    intervals.sort()
    queries = [(q, i) for i, q in enumerate(queries)]
    queries.sort()
    min_heap = []
    i = 0
    result =[-1]*len(queries)
    for q, idx in queries:
        while i != len(intervals) and intervals[i][0] <= q:
            heapq.heappush(min_heap, [intervals[i][1]-intervals[i][0]+1, i])
            i += 1
        while min_heap and intervals[min_heap[0][1]][1] < q:
            heapq.heappop(min_heap)
        result[idx] = min_heap[0][0] if min_heap else -1
    return result

def testFunc(func, test_data, expected_res):
    for i in range(0, len(test_data)):
        print('Input data: ', test_data[i])
        print(func(test_data[i]))
        if(expected_res[i] == func(test_data[i])):
            print('\033[92m' + 'Pass' + '\033[0m')
        else: 
            print('\033[91m' + 'Fail' + '\033[0m')

if __name__ == "__main__":
    testFunc(minInterval, test_data, expected_res)