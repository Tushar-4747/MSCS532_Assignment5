import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def random_partition(arr, low, high):
    random_pivot = random.randint(low, high)
    arr[random_pivot], arr[high] = arr[high], arr[random_pivot]
    return partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = random_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)