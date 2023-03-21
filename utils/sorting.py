def _partition_dict(arr_dict, low, high, key, ascending):
    i = low - 1
    pivot = arr_dict[high][key]

    for j in range(low, high):
        condition = (arr_dict[j][key] <= pivot) if ascending else (arr_dict[j][key] >= pivot)

        # condition vary depending on ascending parameter value
        # if ascending=True, put smaller values on the left side and higher values on the right side of the array
        # if ascending=False, put higher values on the right side and smaller values on the right side of the array
        if condition: 
            i = i + 1
            arr_dict[i], arr_dict[j] = arr_dict[j], arr_dict[i]

    # put pivot value in the middle of the array
    arr_dict[i+1], arr_dict[high] = arr_dict[high], arr_dict[i+1]

    # return pivot index
    return i + 1

# low --> should be 0 at the start; starting index for sorting
# high --> last index to be sorted
def _quicksort_dict(arr_dict, low, high, key, ascending):
    
    if len(arr_dict) == 1:
        return arr_dict

    if low < high:
        # get pivot index
        pi = _partition_dict(arr_dict, low, high, key, ascending)

        # sort elements on the left side of the pivot
        _quicksort_dict(arr_dict, low, pi-1, key, ascending)

        # sort elements on the right side of the pivot
        _quicksort_dict(arr_dict, pi + 1, high, key, ascending)

# arr_dict --> array of dictionary to be sorted
# key --> key of the dictionary that will be used as reference for sorting
# ascending --> dictates the order of the sorting
def sort_dict(arr_dict, key, ascending=True):
    _quicksort_dict(arr_dict, 0, len(arr_dict) - 1, key, ascending)
