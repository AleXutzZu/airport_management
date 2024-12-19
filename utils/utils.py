def merge_sort(container, comparator=lambda x, y: x < y):
    """
    Sorts the given container with the given comparator function.
    :param container: the container to sort
    :type container: list
    :param comparator: the comparator function to use. When called with two arguments, it must return True if the first
    argument is less than the second (i.e. it comes 'before' the second).
    :type comparator: function
    :return: the sorted container
    :rtype: list
    """

    if len(container) < 2:
        return container

    mid = len(container) // 2

    left = container[:mid]
    right = container[mid:]

    left = merge_sort(left, comparator)
    right = merge_sort(right, comparator)

    pos_left, pos_right = 0, 0
    merged = []
    while pos_left < len(left) and pos_right < len(right):
        if comparator(left[pos_left], right[pos_right]):
            merged.append(left[pos_left])
            pos_left += 1
        else:
            merged.append(right[pos_right])
            pos_right += 1

    merged.extend(left[pos_left:])
    merged.extend(right[pos_right:])

    return merged
