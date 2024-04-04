import random

def generate():
    limit = int(input("How many digits you want in your list?\n"))
    lst = [random.randint(1, 100) for _ in range(limit)]
    return lst

def builtin(list):
    list.sort()
    return list

if __name__=="__main__":
    org =generate()
    print(f"Original list: {org}\nSorted list: {builtin(org)}")
