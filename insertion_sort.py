from generate_list import generate

def insertion(list,order=None):
    if order is None:
        order =input("Do you want the sorted list in ascending order?(yes/no)\n")
        if order.lower() not in ["ascending", "yes", "descending", "no"]:
            print("Invalid input. Please enter 'yes' or 'no'")
            return None
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        if order == "ascending" or order == "yes":
            while j >= 0 and key < list[j]:
                list[j + 1] = list[j]
                j -= 1
            list[j + 1] = key
        elif order == "descending" or order == "no":
            while j >= 0 and key > list[j]:
                list[j + 1] = list[j]
                j -= 1
            list[j + 1] = key
    return list

if __name__ == "__main__":
    org =generate()
    print(f"Original list: {org}\nSorted list: {insertion(org)}")
