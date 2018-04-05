# Note - since this is mostly just a tracking file, imports are within each function.

def split_list_on_value(iterable, splitters):
    # splits list on value, return list of lists
    return [list(g) for k, g in itertools.groupby(iterable, lambda x: x in splitters) if not k]


def asimov_significance(s, b):
    from math import log, sqrt
    # caluclates asmiov significance
    if s == 0:
        return 0
    elif b == 0:
        return 0
    elif (2 * ((s + b) * log(1 + (s / b))) - s < 0):
        print "\n     ERROR! Negative sqrt argument!"
        return 0
    else:
        return (sqrt(2 * (((s + b) * log(1 + (s / b))) - s)))

def get_top_two_idx(input_list):
    #  Returns top two values from input_list

    # get max idx
    max_idx = np.argmax(input_list)
    # clone list, remove highest value
    list_clone = input_list[:]
    list_clone.pop(max_idx)
    # get new max, find it in original list, return
    second_max = max(list_clone)
    second_idx = input_list.index(second_max)
    return max_idx, second_idx
