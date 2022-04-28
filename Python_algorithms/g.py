def merge(left_list, right_list):
    sorted_list = []
    left_index, right_index = 0, 0

    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] <= right_list[right_index]:
            sorted_list.append(left_list[left_index])
            left_index += 1
        else:
            sorted_list.append(right_list[right_index])
            right_index += 1

    sorted_list += left_list[left_index:] + right_list[right_index:]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_list = merge_sort(arr[:mid])
    right_list = merge_sort(arr[mid:])

    return merge(left_list, right_list)
