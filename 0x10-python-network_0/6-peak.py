#!/usr/bin/python3
def find_peak(list_of_integers):                                    """
    Finds a peak in a list of unsorted integers.

    Args:                                                               list_of_integers (list[int]): The list of unsorted integers to search for a peak.

    Returns:                                                            int: The peak value in the list, or None if the list is empty.

    """
    if not list_of_integers:
        return None
    mid = len(list_of_integers) // 2                                if len(list_of_integers) == 1 or list_of_integers[mid] >= list_of_integers[mid - 1] and list_of_integers[mid] >= list_of_integers[mid + 1]:                                                         return list_of_integers[mid]                                if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid:])
