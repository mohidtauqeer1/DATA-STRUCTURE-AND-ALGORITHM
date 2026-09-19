from funcs import *


# Problem 1
X = [22, 2, 1, 7, 11, 13, 5, 2, 9]

print("Problem 1:")
print(SearchA(X, 2))


# Problem 2
X = [1, 2, 2, 5, 7, 9]

print("Problem 2:")
print(SearchB(X, 2))


# Problem 3
X = [3, 4, 7, 8, 0, 1, 23, -2, -5]

print("Problem 3:")
print(Minimum(X, 4, 7))


# Problem 4
X = [35, -4, 100, 1, -3, 101, 4, 0, -5]

print("Problem 4:")
print(Sort4(X))


# Problem 5
text = "University of Engineering and Technology Lahore"

print("Problem 5:")
print(StringReverse(text, 0, 40))


# Problem 6
print("Problem 6:")
print(SumIterative(1524))
print(SumRecursive(1524))


# Problem 7
A = [
    [1, 13, 13],
    [5, 11, 6],
    [4, 4, 9]
]

print("Problem 7:")
print(RowWiseSum(A))
print(ColumnWiseSum(A))


# Problem 8
A = [0, 3, 4, 10, 11]
B = [1, 8, 13, 24]

print("Problem 8:")
print(SortedMerge(A, B))


# Problem 9
print("Problem 9:")
print(PalindromRecursive("radar"))