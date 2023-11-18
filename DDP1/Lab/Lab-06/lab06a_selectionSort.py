# lab06a_selectionSort.py
# *******************************************************************
# Name      : Franky Raymarcell Sinaga
# NPM       : 23xxxxxxxx
# TA Code   : XXX
# Sorting a list of numbers using the Recursive-Selection-Sort Algorithm
# *******************************************************************

##
# Given a list of integers, this program
# sorts the list using the recursive selection sort algorithm.
##


def minIndex(lst: list[int], startIndex: int):
    """
    Finds the smallest element in a tail range of a list

    :param lst: The list to sort
    :type lst: list[int]
    :param startIndex: The first position in lst to compare
    :type startIndex: int
    :returns: The position of the smallest element in 
        the range lst[startIndex]...lst[len(lst) - 1]
    :rtype: int
    """

    # base case: only one element to consider
    if startIndex == len(lst)-1:
        return startIndex

    # Find minimum of remaining elements recursively
    k = minIndex(lst, startIndex+1)

    # Return the minimum of all
    if lst[startIndex] < lst[k]:
        return startIndex
    else:
        return k


def selection_sort(lst: list[int], startIndex: int = 0):
    """
    Sorts a list in place, using selection sort recursively.

    :param lst: The list to sort
    :type lst: list[int]
    :param startIndex: The index of starting element
    :type startIndex: int
    """
    n = len(lst)

    # when starting index and size of list are the same, return;
    # because there is nothing to sort
    if startIndex == len(lst): return

    # find the index of minimum element
    # from startIndex to the end
    k = minIndex(lst, startIndex)

    # Swapping the corresponding elements
    # when the found index and the current minimum
    # index are not the same
    if lst[k] < lst[startIndex]:
        lst[k], lst[startIndex] = lst[startIndex], lst[k]

    # Recursively calling selection sort function for the
    # remaining elements
    selection_sort(lst, startIndex + 1)


def main():
    """
    Demonstrates the selection sort algorithm by sorting a
    list of integer given by user
    """
    input_string = input("Type a sequence of numbers (example: 3,100,-5,3): \n")
    if input_string =='':
        values = []
    else:
        values = input_string.split(",")

    #change each element from str to int
    for i in range(len(values)):
        values[i] = int(values[i])

    print('Input list:\n',values)
    selection_sort(values)
    print('Sorted list:\n',values)

if __name__ == '__main__':
    main()