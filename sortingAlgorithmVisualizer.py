from tkinter import *
from tkinter import ttk
import random # To generate random data values
from BubbleSort import BubbleSort


# Generates a black window; Background for GUI 
root = Tk() # Boots up the tkinter module 
root.title('Sorting Algorithm Visualizer')
root.maxsize(1500, 600)
root.config(bg='black')

#variables & functions
selectedAlgorithm = StringVar()
data = [] # where we'll put in the data values; data is used drawDataArray, GenerateNewArray, & StartSortingAlgorithm 

# Draws the rectangle that represent the data value onto the canvas
def drawDataArray(data, colorArray):
    canvas.delete("all") # Delete data values from canvas from previous use of drawDataArray
    canvas_height = 380
    canvas_width = 1400
    bargraph_width = canvas_width / (len(data) + 1) # Width of each bar in array 
    offset = 5 # needed so that the bars don't start at the border of the screen 
    spacing_between_bars = 5 #in pxiels
    
    normalizedData = [ i / max(data) for i in data] #to make sure the height of the bars are relative and seeable in the GUI 
    
    for i, height in enumerate(normalizedData):
        # x1, y1 are coordinates of the top left  needed to create the rectangle for each data
        x1 = i * bargraph_width + offset + spacing_between_bars
        y1 = canvas_height - height * 340
        # x2, y2 are coordinates of the bottom right needed to create the rectangle for each data
        x2 = (i + 1) * bargraph_width + offset
        y2 = canvas_height

        canvas.create_rectangle(x1, y1, x2, y2, fill=colorArray[i]) #Creates the bar for each data value using the x1,y1 and x2,y2 coordinates
        canvas.create_text(x1, y1, anchor=SW, text=str(data[i])) # Writes the numbers over the bar representing the data

    # Shows how the data array changes step by step once an algorith has started
    root.update()

# Generates a new random array of data values using the constraints of minValue, maxValue, and arraySize
def GenerateNewArray():

    canvas.delete("all") # Delete data values from canvas from previous use of drawDataArray

    global data

    minValue = int(minValueScale.get()) # Recieves the string that the user put in the Min Value box and converts it to an int
    maxValue = int(maxValueScale.get()) # Recieves the string that the user put in the Max Value box and converts it to an int
    arraySize = int(arraySizeScale.get()) # Recieves the string that the user put in the Array Size box and converts it to an int

    data = [] # Empty out data array to get rid of values from previous use of GenerateNewArray

    # Fills in the data array with random values with the range of the minValue and maxValue
    for _ in range(arraySize):
        data.append(random.randrange(minValue, maxValue+1))

    
    drawDataArray(data, ['red' for x in range(len(data))])

# Calls upon the sorting algorithm the user has chosen to use
def StartSortingAlgorithm():
    global data

    BubbleSort(data, drawDataArray, sortingSpeedScale.get())

# Generates the background User Interface area of the GUI
UserInterfaceFrame = Frame(root, width = 1400, height = 200, bg='snow4')
UserInterfaceFrame.grid(row=0, column=0, padx=10, pady=5)

# Generates the background / canvas where the bars of data will be drawn on 
canvas = Canvas(root, width = 1400, height = 380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

# User Interface Area - Text Boxes, Buttons, etc.

# FIRST ROW
# (Top Left Corner); Algorithm Label (where you can choose which sorting algorithm you want to use)
Label(UserInterfaceFrame, text="Sorting Algorithm: ", bg='snow4').grid(row=0, column=0, padx=5, pady=5, sticky=W) # W for west aka left
algorithmList = ttk.Combobox(UserInterfaceFrame, textvariable = selectedAlgorithm, values=['Bubble Sort', 'Quick Sort','Merge Sort'])
algorithmList.grid(row=0, column=1, padx=5, pady=5)
algorithmList.current(0) #chooses Bubble Sort by default since it is in index 0

# Sliding Scale button so the user can adjust how fast or slow the sorting speed of the algorithm is
# The smaller the sorting speed, the faster the sorting will be; The larger the sorting speed, the slower the sorting will be
sortingSpeedScale = Scale(UserInterfaceFrame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.1, orient=HORIZONTAL, label="Sorting Speed [sec]")
sortingSpeedScale.grid(row=0, column=2, padx=5, pady=5)

# Button to Start Sorting Algorithm
Button(UserInterfaceFrame, text="Start Sorting Algorithm", command=StartSortingAlgorithm, bg='white').grid(row=0, column=3, padx=5, pady=5)


# SECOND ROW
# 'Array Size' Label where you can decide how many elements you want to have the array; 
# Label(UserInterfaceFrame, text="Array Size ", bg='snow4').grid(row=1, column=0, padx=5, pady=5, sticky=W)
# arraySizeEntry = Entry(UserInterfaceFrame)
# REPLACED LABEL WITH SLIDING SCALE

arraySizeScale = Scale(UserInterfaceFrame, from_ = 3, to=100, resolution=1, orient=HORIZONTAL, label="Array Size")
arraySizeScale.grid(row=1, column=0, padx=5, pady=5)

# 'Min Value' Label where you can decide what the smallest element in the array is 
# Label(UserInterfaceFrame, text="Min Value ", bg='snow4').grid(row=1, column=2, padx=5, pady=5, sticky=W)
# minValueEntry = Entry(UserInterfaceFrame)
# REPLACED LABEL WITH SLIDING SCALE

minValueScale = Scale(UserInterfaceFrame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minValueScale.grid(row=1, column=1, padx=5, pady=5)

# 'Max Value' Label where you can decide what the biggest element in the array is 
# Label(UserInterfaceFrame, text="Max Value ", bg='snow4').grid(row=1, column=4, padx=5, pady=5, sticky=W)
# maxValueEntry = Entry(UserInterfaceFrame)
# REPLACED LABEL WITH SLIDING SCALE

maxValueScale = Scale(UserInterfaceFrame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxValueScale.grid(row=1, column=2, padx=5, pady=5)

# Button to Generate New Random Array of Data Values
Button(UserInterfaceFrame, text="Generate New Random Array", command=GenerateNewArray, bg='white').grid(row=1, column=3, padx=5, pady=5)


root.mainloop() # tkinter's equivalent of main()
