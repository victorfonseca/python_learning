def max_subarray_sum(arr, n):
    subarrays = [arr[i:] for i in range(n)]
    sums = [sum(sub) for sub in zip(*subarrays)]

    return max(sums)

arr = [2, 4, 5, 6, 7, 10, 11, 12, 14]
n = 4

print(max_subarray_sum(arr, n))

def max_subarray_sum(arr, n):
    return max([sum(arr[i:i+n]) for i in range(len(arr)-n+1)])

print(max_subarray_sum(arr, n))