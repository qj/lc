# Question from https://www.byte-by-byte.com/findduplicates/

from typing import List 

def findDuplicates(arr: List[int]) -> List[int]:
    result = set()

    for i in range(len(arr)):
        index = abs(arr[i]) - 1
        if arr[index] < 0:
            result.add(arr[i])
        else:
            arr[index] = -arr[index]
        print(arr)

    return list(result)

if __name__ == '__main__':
    arr = [2, 1, 2, 1, 3, 4, 4, 3, 1, 2]
    print(findDuplicates(arr))