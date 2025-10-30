import random
import time
import matplotlib.pyplot as plt


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def measure_time(sort_function, arr, repeats=5):
    times = []
    for _ in range(repeats):
        arr_copy = arr[:]
        start_time = time.time()
        sort_function(arr_copy)
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times)

sizes = [10000, 50000, 100000, 500000]
results_deterministic = []
results_randomized = []

for size in sizes:
    test_array = [random.randint(0, 1000000) for _ in range(size)]
    time_deterministic = measure_time(deterministic_quick_sort, test_array)
    time_randomized = measure_time(randomized_quick_sort, test_array)
    
    results_deterministic.append(time_deterministic)
    results_randomized.append(time_randomized)
    
    print(f"Розмір масиву: {size}")
    print(f"   Детермінований QuickSort: {time_deterministic:.4f} секунд")
    print(f"   Рандомізований QuickSort: {time_randomized:.4f} секунд\n")

plt.figure(figsize=(10, 6))
plt.plot(sizes, results_deterministic, marker='o', label='Детермінований QuickSort')
plt.plot(sizes, results_randomized, marker='s', label='Рандомізований QuickSort')
plt.xlabel('Розмір масиву')
plt.ylabel('Час виконання (секунди)')
plt.title('Порівняння часу виконання QuickSort')
plt.legend()
plt.grid()
plt.show()
