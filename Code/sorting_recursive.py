#!python
from sorting_iterative import is_sorted, bubble_sort, selection_sort, insertion_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    i = 0
    new_list = []
    while len(items1) != 0 and len(items2) != 0:
        if items1[i] < items2[i]:
            new_list.append(items1.pop(i))
        else:
            new_list.append(items2.pop(i))

    if len(items1) == 0:
        new_list.extend(items2)
    
    else:
        new_list.extend(items1)
    
    return new_list

# print(merge([1, 3, 5, 15], [2, 6, 9]))

def bisect_list(items):
    items1 = items[:len(items)//2]
    items2 = items[len(items)//2:]

    return items1, items2


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order

    items1, items2 = bisect_list(items)

    selection_sort(items1)

    insertion_sort(items2)

    return merge(items1,items2)

# print(split_sort_merge([3, 123, 4412, 51, 21, 3,1 ,2]))

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order

    if len(items) == 1:
        return items

    items1, items2 = bisect_list(items)

    return merge(merge_sort(items1), merge_sort(items2))
    
print(merge_sort([12, 21,4124,1 , 124,24, 1241]))






def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
