def insertion_sort2(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge2(arr, l, m, r):
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]
    
    i = j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def tim_sort(arr, k):
    n = len(arr)
    
    # Sort small subarrays using insertion sort
    for i in range(0, n, k):
        insertion_sort2(arr, i, min(i + k - 1, n - 1))
    
    size = k
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge2(arr, left, mid, right)
        size *= 2

import random
import timeit
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Sorting algorithms
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def find_optimal_k(arr):
    best_k = None
    best_time = float('inf')
    for k in range(1, len(arr), 1):
        test_arr = arr[:]
        elapsed_time = timeit.timeit(lambda: tim_sort(test_arr, k), number=1)
        if elapsed_time < best_time:
            best_time = elapsed_time
            best_k = k
    return best_k


n_values = []
merge_sort_times = []
insertion_sort_times = []
tim_sort_times = []
k_values = []

# Initialize the figure
fig, ax = plt.subplots()
ax.set_xlabel("n")
ax.set_ylabel("Time (s)")
ax.set_title("Merge Sort vs Insertion Sort (Live Update)")
ax.legend()
line1, = ax.plot([], [], label="Merge Sort", color='blue')
line2, = ax.plot([], [], label="Insertion Sort", color='red')
line3, = ax.plot([], [], label="Tim Sort", color='green')
ax.legend()

def update(frame):
    global n_values, merge_sort_times, insertion_sort_times
    n = frame + 1  # Increment n step by step
    arr = [random.randint(0, n) for _ in range(n)]
    k = find_optimal_k(arr)
    k_values.append(k)
    merge_sort_time = timeit.timeit(lambda: merge_sort(arr.copy()), number=1)
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
    tim_sort_time = timeit.timeit(lambda: tim_sort(arr.copy(), k), number=1)
    
    n_values.append(n)
    merge_sort_times.append(merge_sort_time)
    insertion_sort_times.append(insertion_sort_time)
    tim_sort_times.append(tim_sort_time)

    # Update plot
    line1.set_data(n_values, merge_sort_times)
    line2.set_data(n_values, insertion_sort_times)
    line3.set_data(n_values, tim_sort_times)
    ax.relim()
    ax.autoscale_view()
    return line1, line2

# Run animation
ani = FuncAnimation(fig, update, frames=range(1, 400), repeat=False, interval=10)
plt.show()
#print average k value
print(sum(k_values) / len(k_values))
