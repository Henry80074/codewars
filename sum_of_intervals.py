def sum_of_intervals(intervals):
    result = set()
    for ar in intervals:
        for i in range(ar[0], ar[1]):
            result.add(i)
    return len(result)
