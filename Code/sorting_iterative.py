#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so

    # RANGE 
    current = 0
    right = 1
    while right < len(items):
        if items[current] > items[right]:
            return False
        else:
            current += 1
            right += 1
    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    current = 0
    right = 1
    while not is_sorted(items):
        if current == len(items) - 1:
            current = 0
            right = 1

        elif items[current] > items[right]:
            items[current], items[right] = items[right], items[current]
        
        else:
            current += 1
            right += 1

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    current = 0
    minimum = 0
    first = 0
    while not is_sorted(items):
        if items[current] < items[minimum]:
            minimum = current

        elif current == len(items) - 1:
            items[minimum], items[first] = items[first], items[minimum]
            first += 1
            current = first
            minimum = first
        
        else:
            current += 1

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    sorted_index = 1
    while not is_sorted(items):
        num = items.pop(sorted_index)
        
        back_index = sorted_index - 1
        for back_num in items[sorted_index-1::-1]:
            if num > back_num:
                items.insert(back_index + 1, num)
                break

            back_index -= 1
        else:
            items.insert(0, num)
        
        sorted_index += 1