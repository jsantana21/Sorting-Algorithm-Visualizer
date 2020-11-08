import time # To help us visualize this algorithm step by step


def BubbleSort(data, drawDataArray, sortSpeedTime):
    # Traverse through all array elements
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            # Swap if the element found is greater than the next element 
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                # Reflect the swapped values using the drawDataArray function
                # Blue = Sorted, Red = Unsorted
                drawDataArray(data, ['blue' if x == j or x == j+1 else 'red' for x in range(len(data))] )
                # Helps us determine how long this function should be asleep for once the user can see each step of this algorithm
                time.sleep(sortSpeedTime)
                
    # After going through the double for loop, the array should be sorted therefore all bars should be blue
    drawDataArray(data, ['blue' for x in range(len(data))])
