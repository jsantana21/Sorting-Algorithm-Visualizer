import time # To help us visualize this algorithm step by step

'''
Worst Case Time Complexity [ Big-O ]: O(n^2)

Best Case Time Complexity [Big-omega]: O(n)

Average Time Complexity [Big-theta]: O(n^2)

Space Complexity: O(1)
'''

# Based off of Geeks for Geeks Insertion sort example: https://www.geeksforgeeks.org/insertion-sort/
# Another source: https://www.studytonight.com/data-structures/insertion-sorting
def InsertionSort(data, drawDataArray, sortSpeedTime):
    # Traverse through length of data array
    for i in range (1, len(data)): 
        key = data[i]
        # Move elements of arr[0..i-1], that are > key, to one position ahead of current position
        j = i-1
        while j >= 0 and key < data[j]: 
            data[j + 1] = data[j] 
            j -= 1
            # Blue = Done with Sorted, Red = Unsorted, Purple = Being Swap / Being Sorted
            drawDataArray(data, ['purple' if x == j or x == j + 1 else 'red' for x in range(len(data))])
            time.sleep(sortSpeedTime)
        data[j + 1] = key 
