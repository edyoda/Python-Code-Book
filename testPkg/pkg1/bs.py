"""
Description of module 
Author 
Created date 
Modified date 
version
"""

def binary_search(l,key):
    """
    this is BS implementation whick takes list and key as args and returns True or false
    """
    if not l:
        return False
    else:        
        mid = len(l) // 2
        if key == l[mid]:
            return True
        elif key < l[mid]:
            return binary_search(l[0:mid],key)
        else:
            return binary_search(l[mid+1:],key)

if __name__ == "__main__":        
    print("Inside bs.py")        
    l = [10,15,20,25,40,45]
    key = 100

    print(binary_search(l,key))