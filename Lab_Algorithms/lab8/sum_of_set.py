# Lab 8: Sum of Subsets Problem – Backtracking

def sum_of_subsets(arr, capacity, index, curr_sum, subset):
    if curr_sum == capacity:
        print("Subset:", subset)
        return
    if index == len(arr) or curr_sum > capacity:
        return

    # include current element
    sum_of_subsets(arr, capacity, index + 1, curr_sum + arr[index], subset + [arr[index]])
    # exclude current element
    sum_of_subsets(arr, capacity, index + 1, curr_sum, subset)

arr = [23, 56, 12, 9, 34, 20, 89]
capacity = 76
print("Subsets with sum", capacity, ":")
sum_of_subsets(arr, capacity, 0, 0, [])
