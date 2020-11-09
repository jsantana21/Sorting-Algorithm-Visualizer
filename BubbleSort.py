import time # To help us visualize this algorithm step by step

'''
Worst Case Time Complexity [ Big-O ]: O(n^2)

Best Case Time Complexity [Big-omega]: O(n)

Average Time Complexity [Big-theta]: O(n^2)

Space Complexity: O(1) 
''' 

# Based off of Geeks for Geeks Bubble sort example: https://www.geeksforgeeks.org/bubble-sort/
# Another source: https://www.studytonight.com/data-structures/bubble-sort
def BubbleSort(data, drawDataArray, sortSpeedTime):
    # Traverse through all array elements
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            # Swap if the element found is greater than the next element 
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                # Reflect the swapped values using the drawDataArray function
                # Blue = Done with Sorted, Red = Unsorted, Purple = Being Swap / Being Sorted
                drawDataArray(data, ['purple' if x == j or x == j+1 else 'red' for x in range(len(data))] )
                # Helps us determine how long this function should be asleep for once the user can see each step of this algorithm
                time.sleep(sortSpeedTime)
