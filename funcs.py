def SearchA(Arr, x):

    indexes = []

    for i in range(len(Arr)):

        if Arr[i] == x:
            indexes.append(i)

    return indexes


def SearchB(Arr, x):

    indexes = []

    for i in range(len(Arr)):

        if Arr[i] == x:
            indexes.append(i)

        elif Arr[i] > x:
            break

    return indexes


def Minimum(Arr, starting, ending):

    min_index = starting

    for i in range(starting, ending + 1):

        if Arr[i] < Arr[min_index]:
            min_index = i

    return min_index


def Sort4(Arr):

    for i in range(len(Arr)):

        min_index = Minimum(Arr, i, len(Arr) - 1)

        temp = Arr[i]
        Arr[i] = Arr[min_index]
        Arr[min_index] = temp

    return Arr


def StringReverse(str, starting, ending):

    return str[starting:ending + 1][::-1]


def SumIterative(number):

    total = 0

    while number > 0:

        digit = number % 10
        total = total + digit
        number = number // 10

    return total


def SumRecursive(number):

    if number == 0:
        return 0

    return (number % 10) + SumRecursive(number // 10)


def RowWiseSum(Mat):

    result = []

    for row in Mat:

        total = 0

        for value in row:
            total = total + value

        result.append(total)

    return result


def ColumnWiseSum(Mat):

    result = []

    number_of_columns = len(Mat[0])

    for column in range(number_of_columns):

        total = 0

        for row in range(len(Mat)):
            total = total + Mat[row][column]

        result.append(total)

    return result


def SortedMerge(Arr1, Arr2):

    result = []

    i = 0
    j = 0

    while i < len(Arr1) and j < len(Arr2):

        if Arr1[i] < Arr2[j]:

            result.append(Arr1[i])
            i = i + 1

        else:

            result.append(Arr2[j])
            j = j + 1

    while i < len(Arr1):

        result.append(Arr1[i])
        i = i + 1

    while j < len(Arr2):

        result.append(Arr2[j])
        j = j + 1

    return result


def PalindromRecursive(str):

    if len(str) <= 1:
        return True

    if str[0] != str[-1]:
        return False

    return PalindromRecursive(str[1:-1])