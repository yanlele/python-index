# 快速排序

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less_than_pivot = [x for x in array if x <= pivot]
        more_than_pivot = [x for x in array if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(more_than_pivot)

