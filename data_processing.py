def sort_list(input_list, order):
    if order == "asce":
        return sorted(input_list)
    elif order == "desc":
        return sorted(input_list, reverse=True)
    else:
        return "Invalid order. Please use 'asce' or 'desc'."