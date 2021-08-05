searchList = []
def binarySearch(key):
    start, stop = eval(input("Enter the start and stop range values you want to search from:\n"))
    for i in range(start, stop + 1):
        searchList.append(i)
    low = 0
    high = len(searchList) - 1
    while high >= low: 
        mid = (low + high) // 2
        if key < searchList[mid]: 
            high = mid - 1 
        elif key == searchList[mid]:
            return "The key", str(key) + " " + "was found at index", str(mid)
        else: 
            low = mid + 1 
    return "------ Key was not found ------"

def main():
    key = int(input("Enter the number you want to search for:"))
    print(binarySearch(key))

main()



