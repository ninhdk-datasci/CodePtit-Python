import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r") 
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w") 


def merge_count(arr, left, mid, right): 

    L = arr[left:mid+1]
    R = arr[mid+1:right+1] 

    i = j = 0 
    k = left 
    inv_count = 0 

    while i < len(L) and j < len(R): 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i+=1 
        else: 
            arr[k] = R[j] 
            j += 1 
            inv_count += (len(L) - i) 

        k += 1 

    while i < len(L): 
        arr[k] = L[i] 
        i += 1 
        k += 1 

    while j < len(R): 
        arr[k] = R[j] 
        j += 1 
        k += 1 

    return inv_count 

def merger_sort_count(arr, left, right): 
    inv_count = 0 
    if left < right: 
        mid = left + (right - left)//2 
        inv_count += merger_sort_count(arr, left, mid) 
        inv_count += merger_sort_count(arr, mid+1, right) 
        inv_count += merge_count(arr, left, mid, right) 
    return inv_count


if __name__ == "__main__": 
    n = int(input()) 
    arr = list(map(int, input().split())) 

    res = merger_sort_count(arr, 0, n-1) 
    print(res)