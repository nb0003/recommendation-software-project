# functions in use in openingRecommender 

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[-1]
    left_list = [word for word in lst if word < pivot]
    right_list = [word for word in lst if word > pivot]
    left_sorted = quick_sort(left_list)
    right_sorted = quick_sort(right_list)
    return left_sorted + [pivot] + right_sorted

def type_dictionary(lst):
    counter = {}
    for type in lst:
        if type[0] in counter.keys():
            counter[type[0]] += [type]
        else:
            counter[type[0]] = [type]
    return counter

def gameplay_dictionary(lst):
    counter = {}
    for gameplay in lst:
        if gameplay[0] in counter.keys():
            counter[gameplay[0]] += [gameplay]
        else:
            counter[gameplay[0]] = [gameplay]
    return counter

def opening_dictionary(lst):
    open_dict = {}
    for opening in lst:
        opening_type = opening[0]
        gameplay_type = opening[1]

        # If the opening_type is not in the dictionary, add it with an empty nested dictionary
        if opening_type not in open_dict:
            open_dict[opening_type] = {}

        # If the gameplay_type is not in the nested dictionary, add it with an empty list
        if gameplay_type not in open_dict[opening_type]:
            open_dict[opening_type][gameplay_type] = []

        # Add the opening to the list corresponding to the gameplay_type
        open_dict[opening_type][gameplay_type].append(opening[2:])
    return open_dict


def display_opening(lst):
    for opening in lst:
        print("===========================================================", end="\n\n")
        print(f"Opening Name: {opening[0]}")
        print(f"Moves: {opening[1]} ")
#        print(f"Name: {opening[2]} ")
#        print(f"Opening Moves: {opening[3]}")
    print("===========================================================", end="\n\n")

if __name__ == "__main__":
    print(type_dictionary(['classic', 'unusual']))
    print(gameplay_dictionary(['open', 'semi-open', 'closed', 'semi-closed']))


