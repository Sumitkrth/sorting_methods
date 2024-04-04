from generate_list import generate

def selection(list, order=None):
    length=len(list)
    if order is None:
        order=input("Do you want the sorted list in ascending order?(yes/no)\n")
        if order.lower() not in ["ascending", "yes", "descending", "no"]:
            print("Invalid input. Please enter 'yes' or 'no'")
            return None
    for i in range(length-1):
        mini=i
        for j in range(i+1,length):
            if order == "ascending" or order == "yes":
                if list[j]<list[mini]:
                    mini=j
            elif order == "descending" or order == "no":
                if list[j]>list[mini]:
                    mini=j
        list[i],list[mini]=list[mini],list[i]
    return list  
    
if __name__=="__main__":
    org =generate()
    print(f"Original list: {org}\nSorted list: {selection(org,)}")
    
    