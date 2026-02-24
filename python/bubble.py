def bubbleSort(numList):
    n = len(numList)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numList[j] > numList[j+1]:   # <-- missing condition
                tmp = numList[j]
                numList[j] = numList[j+1]
                numList[j+1] = tmp


# Example usage
if __name__ == "__main__":
    theNumbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    bubbleSort(theNumbers)
    print("Sorted numbers are:", theNumbers)
