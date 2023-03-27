from typing import List, Tuple, Optional

# n = 6  # кол-во фишек
# arr = [-1, -1, -9, -7, 3, -6]  # числа на фишках
# target_sum = 2  # сумма которую нужно набрать

n = 10
arr = [-68, 53, -24, 26, -28, -23, 10, -14, 1, -51]
target_sum = -28

def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:

    for i in range(len(arr)):
        for k in range(1, len(arr)):
            if target_sum == (arr[i] + arr[k]):
                if arr[i] == arr[k]:
                    return None
                return arr[i], arr[k]
    else:
        return None



def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))

print_result(two_sum(arr, target_sum))
