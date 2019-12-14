#!python

# [1, 0, 44, 1, 0, 1, 0]

# [(0, 1), (1, 1), (44, 1)]

# [(0, 3), (1, 3), (44, 1)]


# [0, 0, 0, 1, 1, 1, 44]

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O (SIZE OF LARGEST NUMBER)
    Memory usage: O (SIZE OF LARGEST NUMBER)"""
    # Find range of given numbers (minimum and maximum integer values)
    minimum = min(numbers)
    maximum = max(numbers)

    # Create list of counts with a slot for each number in input range
    counts_list = [0 for _ in range(minimum, maximum + 1)]
    print(counts_list)
    # Loop over given numbers and increment each number's count
    for number in numbers:
        counts_list[number - minimum] += 1 # account for offset
    

    # Loop over counts and append that many numbers into output list
    output_list = []
    for index, count in enumerate(counts_list):
        if count == 0:
            continue

        number = index + minimum
        output_list.extend([number] * count)
    
    return output_list
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


if __name__ == '__main__':
    unsorted = [1, 0, 44, 1, 0, 1, 0]
    print(counting_sort(unsorted))