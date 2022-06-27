import statistics


def my_min(*args):
    return min(args)


print(my_min(8, 13, 4, 42, 120, 7))


def my_max(*args):
    return max(args)


print(my_max(8, 13, 4, 42, 120, 7))


def my_median(*args):
    return statistics.median(args)


print(my_median(8, 13, 4, 42, 120, 7))
