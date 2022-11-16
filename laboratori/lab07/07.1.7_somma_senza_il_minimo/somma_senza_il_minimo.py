def sum_without_smallest(v):
    return sum(sorted(v)[1:])


print(sum_without_smallest([1, 2, 3, 4]))
