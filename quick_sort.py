from generate_list import generate

def quick(list, order=None):
    if order is None:
        order = input("Do you want the sorted list in ascending order?(yes/no)\n")
        if order.lower() not in ["ascending", "yes", "descending", "no"]:
            print("Invalid input. Please enter 'yes' or 'no'")
            return None
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        if order == "ascending" or order == "yes":
            lesser_pivot = [x for x in list[1:] if x <= pivot]
            greater_pivot = [x for x in list[1:] if x > pivot]
        elif order == "descending" or order == "no":
            lesser_pivot = [x for x in list[1:] if x >= pivot]
            greater_pivot = [x for x in list[1:] if x < pivot]
        return quick(lesser_pivot, order) + [pivot] + quick(greater_pivot, order)

if __name__ == "__main__":
    org =generate()
    print(f"Original list: {org}\nSorted list: {quick(org)}")

     