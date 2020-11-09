import time # To help us visualize this algorithm step by step

'''
Worst Case Time Complexity [ Big-O ]: O(n^2)

Best Case Time Complexity [Big-omega]: O(n*log n)

Average Time Complexity [Big-theta]: O(n*log n)

Space Complexity: O(n*log n)
'''

# Based off of Geeks for Geeks Bubble sort example
# Another source: https://www.studytonight.com/data-structures/quick-sort
def QuickSort(data, low, high, drawDataArray, sortSpeedTime):

    #Base Case
    if low < high:
        partitionIndex = partition(data, low, high, drawDataArray, sortSpeedTime)

        # Recursive call to quick sort the array to the LEFT of the border
        QuickSort(data, low, partitionIndex-1, drawDataArray, sortSpeedTime)

        # Recursive call to quick sort the array to the RIGHT of the border
        QuickSort(data, partitionIndex+1, high, drawDataArray, sortSpeedTime)

# Takes last element as pivot, places
# the border element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right of pivot
def partition(data, low, high, drawDataArray, sortSpeedTime):
    border = low
    pivot = data[high] #last value in our data array

    # After setting up the border and pivot, show this variables highlighted on the canvas
    drawDataArray(data, getColorArray(len(data), low, high, border, border))
    time.sleep(sortSpeedTime)

    for j in range(low, high):
        if data[j] < pivot:
            
            # See what two elements are going to be swapped in this iteration
            drawDataArray(data, getColorArray(len(data), low, high, border, j, True))
            time.sleep(sortSpeedTime)

            # Swap border value and j value
            data[border], data[j] = data[j], data[border]
            # Move border to the right
            border += 1

        # Reflect the swapped values in this iteration by using the drawDataArray function and time.sleep() 
        drawDataArray(data, getColorArray(len(data), low, high, border, j))
        time.sleep(sortSpeedTime)


    # Swap border value and pivot value
    drawDataArray(data, getColorArray(len(data), low, high, border, high, True))
    time.sleep(sortSpeedTime)

    data[border], data[high] = data[high], data[border]
    
    return border # border should be the middle by the end of this function

#Helps in the visualization part of the algorithm 
def getColorArray(dataLength, low, high, border, currentIndex, isSwaping = False):
    
    colorArray = []
    
    for i in range(dataLength):
        
        # Base Colors for when the array is unsorted
        if i >= low and i <= high:
            colorArray.append('gray') # Current range of elements we are looking at
        else:
            colorArray.append('red') # All other elements we aren't currently looking at; outside of range(low, high+1) 

        if i == high:
            colorArray[i] = 'orange' # the pivot will be highlighted in orange
        elif i == border:
            colorArray[i] = 'green' # the border will be highlighted in green
        elif i == currentIndex:
            colorArray[i] = 'yellow' # the current element will be highlighted in yellow

        if isSwaping:
            if i == border or i == currentIndex:
                colorArray[i] = 'purple' # Element is highlighted in purple if it has been swapped / sorted

    return colorArray
