from search.linear_search import linear_search
from search.binary_search import binary_search

from sort.bubble_sort import bubble_sort
from sort.selection_sort import selection_sort
from sort.insertion_sort import insertion_sort
from sort.merge_sort import merge_sort
from sort.quick_sort import quick_sort

arr = [64, 34, 25, 12, 22, 11, 90]

print("Bubble:", bubble_sort(arr.copy()))
print("Selection:", selection_sort(arr.copy()))
print("Insertion:", insertion_sort(arr.copy()))
print("Merge:", merge_sort(arr.copy()))
print("Quick:", quick_sort(arr.copy()))

sorted_arr = sorted(arr)

print("Linear Search:", linear_search(arr, 25))
print("Binary Search:", binary_search(sorted_arr, 25))