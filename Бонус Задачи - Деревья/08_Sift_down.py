def sift_down(heap, index):
    left = 2 * index
    right = 2 * index + 1
    size = len(heap) - 1
    if left > size:
        return index
    if (right <= size) and (heap[left] < heap[right]):
        index_largest = right
    else:
        index_largest = left
    if heap[index] < heap[index_largest]:
        heap[index], heap[index_largest] = heap[index_largest], heap[index]
        return sift_down(heap, index_largest)
    return index