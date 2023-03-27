from typing import List, Tuple

n = 7
arr = [1, 2, 3, 4, 5, 6, 7]
window_size = 4

def moving_average(arr: List[int], window_size: int) -> List[float]:
    t = sum(arr[:window_size])
    res = [t / window_size]
    for i in range(window_size, len(arr)):
        t += arr[i] - arr[i - window_size]
        res.append(t / window_size)
    return res

print(" ".join(map(str, moving_average(arr, window_size))))