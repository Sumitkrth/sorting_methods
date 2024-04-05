from generate_list import generate
from quick_sort import quick
from bubble_sort import bubble
from insertion_sort import insertion
from selection_sort import selection
 
def binary_search(list, value):
    comparisons = 0
    left = 0
    right = len(list) - 1
    ascending = list[0] < list[-1]
    if not ascending:
        list.sort()
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if list[mid] == value:
            return True, comparisons
        elif list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return False, comparisons

data = [78, 47, 54, 19, 11, 77, 77, 23, 39, 80, 95, 64, 31, 48, 17, 56, 58, 30, 52, 82]
#data = generate() #Use this line for list with random value.
data_ascending = selection(data.copy(), "ascending")   
data_descending = selection(data.copy(), "descending")

if __name__ == "__main__":
    print("Original list:", data)
    print("Ascending order:", data_ascending)
    print("Descending order:", data_descending)
    search_value = int(input("For which number in the given list you want to check the number of comparisons: "))
    
    found_original, comparisons_original = binary_search(sorted(data), search_value)
    found_ascending, comparisons_ascending = binary_search(data_ascending, search_value)
    found_descending, comparisons_descending = binary_search(data_descending, search_value)
    
    if found_original:
        print("Number of comparisons in original list:", comparisons_original)
    else:
        print("Value not found in the original list.")        
    if found_ascending:
        print("Number of comparisons in ascending list:", comparisons_ascending)
    else:
        print("Value not found in the ascending list.")       
    if found_descending:
        print("Number of comparisons in descending list:", comparisons_descending)
    else:
        print("Value not found in the descending list.")
