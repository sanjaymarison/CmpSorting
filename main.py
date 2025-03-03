import random
import timeit
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


n_values = []
merge_sort_times = []
insertion_sort_times = []

# Initialize the figure
fig, ax = plt.subplots()
ax.set_xlabel("n")
ax.set_ylabel("Time (s)")
ax.set_title("Merge Sort vs Insertion Sort (Live Update)")
ax.legend()
line1, = ax.plot([], [], label="Merge Sort", color='blue')
line2, = ax.plot([], [], label="Insertion Sort", color='red')
ax.legend()

def update(frame):
    global n_values, merge_sort_times, insertion_sort_times
    n = frame + 1  # Increment n step by step
    arr = [random.randint(0, n) for _ in range(n)]
    merge_sort_time = timeit.timeit(lambda: merge_sort(arr), number=1)
    insertion_sort_time = timeit.timeit(lambda: insertion_sort(arr.copy()), number=1)
    
    n_values.append(n)
    merge_sort_times.append(merge_sort_time)
    insertion_sort_times.append(insertion_sort_time)
    
    # Update plot
    line1.set_data(n_values, merge_sort_times)
    line2.set_data(n_values, insertion_sort_times)
    ax.relim()
    ax.autoscale_view()
    return line1, line2

# Run animation
ani = FuncAnimation(fig, update, frames=range(1, 1000), repeat=False, interval=10)
plt.show()
