#!/bin/python

def bin_search(arr, elem):
    bound_l = 0
    bound_r = len(arr)
    while bound_l < bound_r:
        middle = bound_l + (bound_r - bound_l)//2
        if arr[middle] == elem:
            return middle
        if arr[middle] < elem:
            bound_l = middle + 1
        else:
            bound_r = middle
    return None
    
print(bin_search([1, 3, 5, 7, 10], 0))
print(bin_search([1, 3, 5, 7, 10], 1))
print(bin_search([1, 3, 5, 7, 10], 3))
print(bin_search([1, 3, 5, 7, 10], 11))
