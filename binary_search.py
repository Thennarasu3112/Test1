
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr,0,mid-1,x)
        else:
            return binary_search(arr,mid-1,high,x)
    else:
        return -1


if __name__ == "__main__":
    arr = [ 3,  8, 16, 19, 20, 21, 38, 38, 41, 47, 51, 53, 53, 60, 63, 65, 65,83, 83, 91]
    x = 38
    result  = binary_search(arr,0,len(arr) -1, x)

    if result != 1:
        print("Match found at index: ",result)
    else:
        print("Match Not found in the given array")