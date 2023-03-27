from typing import List, Tuple, Optional

n = 6
arr = [-9, -7, -6, -1, -1, 3]
target_sum = 2


# n = 10
# arr = [-68, 53, -24, 26, -28, -23, 10, -14, 1, -51]
# target_sum = -28


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    previous = set(arr)
    for i in range(len(arr)):
        y = target_sum - arr[i]
        if y in previous:
            if arr[i] == y:
                return None
            return arr[i], y
        else:
            previous.add(arr[i])
    return None

def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))

print_result(two_sum(arr, target_sum))