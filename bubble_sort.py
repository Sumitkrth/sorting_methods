from generate_list import generate

def bubble(list,order=None):
    length = len(list)
    if order is None:
        order =input("Do you want the sorted list in ascending order?(yes/no)\n")
        if order.lower() not in ["ascending", "yes", "descending", "no"]:
            print("Invalid input. Please enter 'yes' or 'no'")
            return None
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            if order == "yes" or order == "ascending":
                if list[j] > list[j + 1]:
                     list[j], list[j + 1] = list[j + 1], list[j]
            elif order == "no" or order == "descending":
                if list[j] < list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
    return list

if __name__=="__main__":
    org =generate()
    print(f"Original list: {org}\nSorted list: {bubble(org)}")
