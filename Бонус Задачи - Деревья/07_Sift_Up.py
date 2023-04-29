def sift_up(heap, index):
    if index == 1:
        return index
    parent_index = index // 2
    if heap[parent_index] < heap[index]:
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        return sift_up(heap, parent_index)
    return index