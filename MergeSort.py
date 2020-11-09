import time # To help us visualize this algorithm step by step

def MergeSort(data, drawDataArray, sortSpeedTime):
    MergeSort2(data,0, len(data)-1, drawDataArray, sortSpeedTime)


def MergeSort2(data, left, right, drawDataArray, sortSpeedTime):
    if left < right: # left index has to be at least one smaller than right index
        middle = (left + right) // 2
        # Sort the first half
        MergeSort2(data, left, middle, drawDataArray, sortSpeedTime)
        # Sort the second half
        MergeSort2(data, middle+1, right, drawDataArray, sortSpeedTime)
        # Remerge the two halves back together
        Merge(data, left, middle, right, drawDataArray, sortSpeedTime)

def Merge(data, left, middle, right, drawDataArray, sortSpeedTime):

    # Show all the split up lists of values before merging starts
    drawDataArray(data, getColorArray(len(data), left, middle, right))
    time.sleep(sortSpeedTime)

    leftHalf = data[left:middle+1]
    rightHalf = data[middle+1: right+1]

    leftIndex, rightIndex = 0, 0

    for dataIndex in range(left, right+1):
        
        # Check if both left index and right index are within bounds
        if leftIndex < len(leftHalf) and rightIndex < len(rightHalf):
            
            if leftHalf[leftIndex] <= rightHalf[rightIndex]:
                data[dataIndex] = leftHalf[leftIndex]
                leftIndex += 1
            else: # if rightHalf[rightIndex] > leftHalf[leftIndex]
                data[dataIndex] = rightHalf[rightIndex]
                rightIndex += 1
                
        # Check if left index is within bounds of the leftHalf
        elif leftIndex < len(leftHalf):
            data[dataIndex] = leftHalf[leftIndex]
            leftIndex += 1
            
        # Last case is that the right index is within bounds of the rightHalf
        else: # if rightIndex < len(rightHalf)
            data[dataIndex] = rightHalf[rightIndex]
            rightIndex += 1

    # Highlight all merged parts in blue otherwise highlight the rest in red
    drawDataArray(data, ["purple" if x >= left and x <= right else "red" for x in range(len(data))])
    time.sleep(sortSpeedTime)

# Helps in the visualization part of the algorithm 
def getColorArray(leght, left, middle, right):
    
    colorArray = []

    for i in range(leght):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("orange") # Data values in the left half of the array are highlighted in yellow
            else: # if i >= middleand i <= right:
                colorArray.append("green") # Data values in the right half of the array are highlighted in green
        else:
            colorArray.append("red") # Data values that we aren't currently working with are highlighted in red

    return colorArray
