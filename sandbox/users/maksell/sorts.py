# Bubble sort
# Time complexity O(n^2)
# Space complexity - No need

def bubble(data):
    for i in range(len(data)):
        is_swapped = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                is_swapped = True
                data[j], data[j + 1] = data[j + 1], data[j]

        # Если мы прошли всю итерацию и не нашли нужных элементов для свапа - массив отсортирован
        if not is_swapped:
            break
    return data


print(bubble([99, 5, 2, 4, 6, 72, 3, 5, 7, 3, 5, 8, 3]))
# [2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 72, 99]


# Selection sort
# Time complexity O(n^2)
# Space complexity - O(1)

def selection_sort(data):
    for i in range(len(data)):

        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j

        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]

    return data


print(selection_sort([99, 5, 2, 4, 6, 72, 3, 5, 7, 3, 5, 8, 3]))
# [2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 72, 99]


# Insertion sort
# Time complexity O(n^2)
# Space complexity - O(1)

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


print(insertion_sort([99, 5, 2, 4, 6, 72, 3, 5, 7, 3, 5, 8, 3]))
# [2, 3, 3, 3, 4, 5, 5, 5, 6, 7, 8, 72, 99]

